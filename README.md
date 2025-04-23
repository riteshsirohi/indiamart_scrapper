# IndiaMart Data Scraping and Analysis Project

## 📌 Overview

This project scrapes product data from **IndiaMart.com** across key market categories and performs **exploratory data analysis (EDA)** to uncover pricing trends, product distribution, and supplier insights. Developed as part of my application for the **Data Extraction Engineering Intern** role at **SnapWrite AI**, it showcases hands-on skills in **web scraping, data cleaning, and data analysis using Python**.

---

## 🎯 Objectives

- **Scrape Data**: Extract product details (name, price, company, category) from IndiaMart categories:
  - Industrial Machinery
  - Agriculture & Farming
  - Medical & Healthcare

- **Perform EDA**: Analyze the dataset to understand:
  - Price distribution
  - Category-wise product trends
  - Supplier dominance

- **Share Insights**: Present actionable findings to guide:
  - Market prioritization
  - AI-powered product categorization

---

## 🛠️ Implementation

### 🔍 Scraper (`scraper.py`)
- Built using `requests` and `BeautifulSoup`.
- Scrapes 5 pages per category.
- Extracts:
  - **Product Name** (`<a class="fs18 ptitle">`)
  - **Price** (`<span class="prc cur tcur">`, cleaned of "Get Latest Price")
  - **Company Name** (`<h2 class="lcname">`)
  - **Category** (parsed from the URL)

- Outputs:
  - `products.csv` with 274 unique products
  - Saves raw HTML for debugging
  - Includes pagination support and 1-second delay for rate-limiting

---

### 📊 EDA & Data Cleaning (`process_data.py`)
- Standardizes prices, removes duplicates, handles missing values
- Generates:
  - Summary statistics (mean, max prices by category)
  - Top companies by product count
  - Visualizations:
    - 📈 `price_by_category.png` (bar plot)
    - ☁️ `product_wordcloud.png` (product name word cloud)

- Outputs:
  - `products_cleaned.csv` (cleaned dataset)

---

## 📈 Key Insights

### 💰 Price Trends
| Category               | Avg. Price (₹) | Max Price (₹) |
|------------------------|----------------|----------------|
| Industrial Machinery   | ~775,993       | 12,000,000     |
| Agriculture & Farming  | ~112,250       | 1,250,000      |
| Medical & Healthcare   | ~117,709       | 1,250,000      |

> 🧠 **Takeaway**: Industrial Machinery is high-value. Agriculture and Medical cater to cost-sensitive markets.

---

### 📦 Category Distribution
- **Industrial Machinery**: 150 products (54%)
- **Agriculture & Farming**: 92 (34%)
- **Medical & Healthcare**: 33 (12%)

> 📌 **Takeaway**: Focus on Industrial Machinery for broader coverage. Medical is a niche, specialized domain.

---

### 🏢 Company Landscape
- Top suppliers:
  - ASV Engineering (10 products)
  - JVA SMT Traders (9)
  - H.S. Overseas (9)
- No single dominant supplier → highly competitive

> 🧠 **Takeaway**: Diverse supplier data enables comprehensive insights.

---

### 🔑 Product Keyword Patterns
- Industrial & Agriculture: keywords like “machine”, “automatic”
- Medical: includes “surgical”, “diagnostic”

> 🤖 **Takeaway**: Product names provide valuable clues for AI-based categorization.

---

## 📁 Project Structure

```
indiamart_scrap/
├── scraper.py                 # Web scraper
├── process_data.py           # EDA and data cleaning
├── products.csv              # Raw scraped data
├── products_cleaned.csv      # Cleaned dataset
├── price_by_category.png     # Bar plot of average prices
├── product_wordcloud.png     # Word cloud of product names
├── indiamart_insights.md     # Detailed EDA insights
├── data/
│   ├── [Category]_page_[N].html  # Saved HTML pages
│   └── scraper.log               # Error log (if any)
└── README.md                # Project documentation
```

---

## ⚙️ Setup & Usage

### ✅ Prerequisites
- Python 3.8+
- Virtual environment (recommended)
  
```bash
python -m venv venv
```

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

If no `requirements.txt` file is present, install manually:
```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn wordcloud
```

### 🚀 Run the Project

#### 1. Activate Virtual Environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

#### 2. Scrape Data (Optional — already included):
```bash
python scraper.py
```

- Output: `products.csv`, HTML files in `/data`

#### 3. Perform EDA:
```bash
python process_data.py
```

- Output: `products_cleaned.csv`, plots

#### 4. View Results:
- Visuals: `price_by_category.png`, `product_wordcloud.png`
- Detailed insights: `indiamart_insights.md`

---

## 🧩 Notes

- Dataset includes 275 products:
  - 150 Industrial Machinery
  - 92 Agriculture & Farming
  - 33 Medical & Healthcare
- Original dataset (414 products) trimmed for focused analysis.
- Want more data? Modify `scraper.py` to expand categories or page depth.

---
For any questions or collaboration, feel free to reach out!

---
