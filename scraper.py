import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json
import logging
import re

# Set up logging
logging.basicConfig(
    filename='data/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# List of categories to scrape (name and URL)
categories = [
    {"name": "Industrial Machinery", "url": "https://dir.indiamart.com/impcat/industrial-machinery.html"},
    {"name": "Electronics & Electrical", "url": "https://dir.indiamart.com/impcat/electronic-products.html"},
    {"name": "Medical & Healthcare", "url": "https://dir.indiamart.com/impcat/medical-equipment.html"},
    {"name": "Agriculture & Farming", "url": "https://dir.indiamart.com/impcat/agricultural-equipment.html"}
]

# Number of pages to scrape per category
num_pages = 10

# User-agent header to avoid being blocked
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# List to store all products
all_products = []

try:
    for category in categories:
        category_name = category["name"]
        base_url = category["url"]
        logging.info(f"Starting to scrape category: {category_name}")
        print(f"\nScraping category: {category_name}")

        for page in range(1, num_pages + 1):
            # Construct URL for the current page
            url = f"{base_url}?page={page}" if page > 1 else base_url
            print(f"Scraping page {page}: {url}")

            # Send request
            try:
                response = requests.get(url, headers=headers, timeout=10)
                print(f"Status Code: {response.status_code}")
                logging.info(f"Page {page} of {category_name} - Status Code: {response.status_code}")

                if response.status_code == 200:
                    print("Successfully fetched the page!")
                    # Save HTML for debugging
                    html_file = f'data/{category_name.replace(" ", "_")}_page_{page}.html'
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(response.text)
                    print(f"Saved webpage HTML to {html_file}")

                    # Parse HTML with BeautifulSoup
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Find all product title elements
                    product_elements = soup.find_all('a', class_='fs18 ptitle')
                    if not product_elements:
                        print("No product elements found on this page.")
                        logging.warning(f"No product elements found on page {page} of {category_name}")
                        continue

                    for product_element in product_elements:
                        product_data = {
                            'Category': category_name,
                            'Product Name': '',
                            'Price': '',
                            'Company Name': '',
                            'Product URL': '',
                            'Description': ''
                        }

                        # Get product name
                        h3_tag = product_element.find('h3')
                        if h3_tag:
                            product_name = h3_tag.text.strip()
                            product_data['Product Name'] = product_name

                        # Get price
                        parent_container = product_element.find_parent('div', class_='rht pnt flx')
                        if parent_container:
                            price_element = parent_container.find('span', class_='prc cur tcur')
                            if price_element:
                                price_text = price_element.text.strip()
                                # Clean price: remove "Get Latest Price"
                                if 'Get Latest Price' in price_text:
                                    price_text = price_text.replace('Get Latest Price', '').strip()
                                product_data['Price'] = price_text

                        # Get company name
                        product_card = product_element.find_parent('li', class_='lst')
                        if product_card:
                            company_element = product_card.find('h2', class_='lcname')
                            if company_element:
                                company_name = company_element.text.strip()
                                product_data['Company Name'] = company_name
                                # Clean product name: remove company name if present
                                if product_name and company_name:
                                    # Case-insensitive match
                                    clean_name = re.sub(rf'^{re.escape(company_name)}\s*', '', product_name, flags=re.IGNORECASE).strip()
                                    product_data['Product Name'] = clean_name or product_name

                        # Get product URL
                        if product_element.get('href'):
                            product_data['Product URL'] = product_element['href']

                        # Get description
                        if parent_container:
                            desc_element = parent_container.find('div', class_='desc des_p elps3l')
                            if desc_element:
                                # Extract text from description table
                                desc_text = ' '.join([t.text.strip() for t in desc_element.find_all(['td', 'span']) if t.text.strip()])
                                product_data['Description'] = desc_text

                        # Only add if we have a product name
                        if product_data['Product Name']:
                            all_products.append(product_data)

                    print(f"Found {len(product_elements)} product elements on page {page}.")

                else:
                    print(f"Failed to fetch page {page}. Status code: {response.status_code}")
                    logging.error(f"Failed to fetch page {page} of {category_name}. Status code: {response.status_code}")
                    continue

            except requests.RequestException as e:
                print(f"Request error on page {page}: {e}")
                logging.error(f"Request error on page {page} of {category_name}: {e}")
                continue

            # Delay to avoid rate-limiting
            time.sleep(2)

    # Deduplicate products (based on Product Name, Price, Company Name, Category)
    if all_products:
        df = pd.DataFrame(all_products)
        df = df.drop_duplicates(subset=['Product Name', 'Price', 'Company Name', 'Category'], keep='first')
        # Save to CSV
        df.to_csv('data/products.csv', index=False)
        # Save to JSON
        df.to_json('data/products.json', orient='records', lines=True)
        print(f"\nSaved {len(df)} unique products to data/products.csv and data/products.json")
        # Print sample for confirmation
        print("Sample products:")
        for _, product in df.head(3).iterrows():
            print(f"- {product['Category']} | {product['Product Name']} | {product['Price']} | {product['Company Name']} | {product['Product URL']} | {product['Description'][:50]}...")
        logging.info(f"Saved {len(df)} unique products")
    else:
        print("\nNo products found across all categories. Check the HTML files in data/ for clues.")
        logging.warning("No products found across all categories")

except Exception as e:
    print(f"An error occurred: {e}")
    logging.error(f"Main script error: {e}")