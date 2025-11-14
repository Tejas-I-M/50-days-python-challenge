
# Day 1: News Headline Scraper + Keyword Analyzer


# Import required libraries
import requests                     # To fetch the website content
from bs4 import BeautifulSoup       # For parsing HTML
import csv                          # To save data into CSV files
from collections import Counter     # To count keyword frequency
import re                           # For text cleaning

# STEP 1: Fetch the HTML content of Hacker News front page
url = "https://news.ycombinator.com/"
response = requests.get(url)
html = response.text

# STEP 2: Parse HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# STEP 3: Extract all headline texts (links inside <a class='titleline'>)
titles = []
for tag in soup.select(".titleline a"):
    titles.append(tag.text)

# STEP 4: Clean and tokenize words from titles
words = []
for title in titles:
    # Convert to lowercase
    title = title.lower()
    # Remove special characters (keep only letters, digits, spaces)
    title = re.sub(r'[^a-z0-9\s]', ' ', title)
    # Split title into words and add to the list
    for w in title.split():
        # Skip very small words like 'is', 'at', 'on'
        if len(w) > 2:
            words.append(w)

# STEP 5: Count most common words
top_words = Counter(words).most_common(10)

# STEP 6: Save all headlines into a CSV file
with open("headlines.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Headline"])
    for t in titles:
        writer.writerow([t])

# STEP 7: Print summary output
print("✅ Scraped Headlines:", len(titles))
print("\nTop 10 Keywords Found:")
for word, count in top_words:
    print(f"{word:15s} -> {count}")

print("\nAll headlines saved to 'headlines.csv' successfully!")
