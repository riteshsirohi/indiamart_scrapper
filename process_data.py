import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
df = pd.read_csv('data/products.csv')
print(f"Loaded {len(df)} products")

# 1. Clean data
# Standardize prices
df['Price'] = df['Price'].str.extract(r'₹ ([\d,]+)/').replace(',', '', regex=True).astype(float)
# Remove duplicates
df = df.drop_duplicates(subset=['Product Name', 'Price', 'Company Name', 'Category'])
# Handle missing values
df['Price'] = df['Price'].fillna(df['Price'].median())
df['Company Name'] = df['Company Name'].fillna('Unknown')
df['Category'] = df['Category'].fillna('Unknown')
print(f"After cleaning: {len(df)} unique products")

# Save cleaned data
df.to_csv('data/products_cleaned.csv', index=False)
print("Saved cleaned data to data/products_cleaned.csv")

# 2. Analyze data
# Summary statistics by category
print("\nSummary statistics by category:")
print(df.groupby('Category')['Price'].describe())

# Top companies
print("\nTop 5 companies by product count:")
print(df['Company Name'].value_counts().head(5))

# 3. Visualize data
# Bar plot: Average price by category
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Price', data=df, estimator=lambda x: x.mean())
plt.title('Average Price by Category')
plt.ylabel('Price (₹)')
plt.xticks(rotation=45)
plt.savefig('data/price_by_category.png')
plt.close()
print("Saved bar plot to data/price_by_category.png")

# Word cloud: Product names
text = ' '.join(df['Product Name'].str.lower())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Product Name Word Cloud')
plt.savefig('data/product_wordcloud.png')
plt.close()
print("Saved word cloud to data/product_wordcloud.png")