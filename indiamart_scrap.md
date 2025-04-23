IndiaMart Data Scraping and Analysis Project
Overview
This project scrapes product data from IndiaMart.com across multiple categories and performs exploratory data analysis (EDA) to uncover market trends. Developed as part of my application for the Data Extraction Engineering Intern role at SnapWrite AI, it demonstrates skills in web scraping, data cleaning, and analysis using Python.
Objectives

Scrape Data: Build a crawler to extract product names, prices, company names, and categories from IndiaMart (categories: Industrial Machinery, Agriculture & Farming, Medical & Healthcare).
Perform EDA: Analyze the data to derive insights on pricing, category distribution, and supplier trends.
Share Insights: Present findings to guide data-driven decisions, such as market prioritization or AI-driven categorization.

Implementation

Scraper (scraper.py):
Built with Python, requests, and BeautifulSoup.
Scrapes 5 pages per category, extracting:
Product Name (<a class="fs18 ptitle">)
Price (<span class="prc cur tcur">, cleaned to remove “Get Latest Price”)
Company Name (<h2 class="lcname">)
Category (from URL)


Saves 274 unique products to products.csv.
Features error handling, pagination, and a 1-second delay to avoid rate-limiting.


EDA (process_data.py):
Cleans data (standardizes prices, removes duplicates, handles missing values).
Generates:
Summary statistics (price mean, max, etc. per category).
Top companies by product count.
Visualizations: Bar plot (price_by_category.png), word cloud (product_wordcloud.png).


Saves cleaned data to products_cleaned.csv.



Key Insights
From analyzing 274 products across three categories:

Price Trends:
Industrial Machinery: Highest average price (~₹775,993, max ₹12M), reflecting premium equipment.
Agriculture & Farming: ~₹112,250, max ₹1.25M, targeting small-scale farmers.
Medical & Healthcare: ~₹117,709, max ₹1.25M, for specialized devices.
Takeaway: Industrial Machinery is a high-value market, while Agriculture and Medical are cost-sensitive.


Category Distribution:
Industrial Machinery: 149 products (54%), dominant market.
Agriculture & Farming: 92 (34%).
Medical & Healthcare: 33 (12%), possibly niche.
Takeaway: Prioritize Industrial Machinery for broad data coverage; Medical offers niche opportunities.


Company Landscape:
Top suppliers: ASV Engineering (10 products), JVA Smt Traders (9), H.S. Overseas (9).
Competitive market, no single dominant player.
Takeaway: Diverse supplier data ensures comprehensive market insights.


Product Patterns:
Keywords like “machine,” “automatic” dominate Industrial Machinery and Agriculture (per word cloud).
Medical likely includes “surgical,” “diagnostic.”
Takeaway: Keywords can enhance AI-driven product categorization.



Detailed insights are in indiamart_insights.md.
File Structure

Code:
scraper.py: Scrapes IndiaMart data.
process_data.py: Cleans data and performs EDA.


Data:
products.csv: Raw scraped data (274 products).
products_cleaned.csv: Cleaned data with numeric prices.


Outputs:
price_by_category.png: Bar plot of average prices by category.
product_wordcloud.png: Word cloud of product names.
indiamart_insights.md: Detailed insights report.


Debugging (optional):
data/[Category]_page_[N].html: Saved HTML pages (e.g., Industrial_Machinery_page_1.html).
data/scraper.log: Error logs (if generated).



Setup and Usage
Prerequisites

Python 3.8+
Virtual environment (recommended): python -m venv venv

Dependencies
Install required libraries:
pip install requests beautifulsoup4 pandas matplotlib seaborn wordcloud

Running the Project

Clone or unzip the project to a directory (e.g., D:\python\indiamart_scrap).

Activate virtual environment (if used):
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac


Scrape Data (optional, as products.csv is included):
python scraper.py


Outputs: products.csv, HTML files in data/.


Perform EDA:
python process_data.py


Outputs: products_cleaned.csv, price_by_category.png, product_wordcloud.png.


Review Insights:

Open indiamart_insights.md for detailed findings.
View price_by_category.png and product_wordcloud.png for visualizations.



Notes

The dataset includes 275 products (150 Industrial Machinery, 92 Agriculture & Farming, 33 Medical & Healthcare). An earlier dataset had 414 products, but was updated to focus on these categories.
Electronics & Electrical data is absent due to intentional dataset changes.
Scraping more categories or pages is possible by modifying scraper.py (e.g., update categories list or num_pages).


