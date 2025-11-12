# ==========================================
# Q1. Books to Scrape
# ==========================================
import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
prices = []
availabilities = []
ratings = []
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for page in range(1, 51):
    url = base_url.format(page)
    res = requests.get(url)
    if res.status_code != 200:
        break
    soup = BeautifulSoup(res.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        titles.append(book.h3.a['title'])
        prices.append(book.find('p', class_='price_color').text)
        availabilities.append(book.find('p', class_='instock availability').text.strip())
        ratings.append(book.p['class'][1])

df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Availability': availabilities,
    'Star Rating': ratings
})
df.to_csv('books.csv', index=False)
print("✅ Books data saved successfully to books.csv")


# ==========================================
# Q2. IMDb Top 250 Movies
# ==========================================
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top/")
time.sleep(3)

movies = driver.find_elements(By.CSS_SELECTOR, 'li.ipc-metadata-list-summary-item')

ranks, titles, years, ratings = [], [], [], []

for movie in movies:
    try:
        title_block = movie.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text
        if '.' in title_block:
            rank = title_block.split('.')[0].strip()
            title = title_block.split('. ')[1].strip()
        else:
            continue

        year = movie.find_elements(By.CSS_SELECTOR, '.cli-title-metadata-item')[0].text
        rating = movie.find_element(By.CSS_SELECTOR, '.ipc-rating-star--rating').text

        ranks.append(rank)
        titles.append(title)
        years.append(year)
        ratings.append(rating)

    except Exception:
        continue

df = pd.DataFrame({
    'Rank': ranks,
    'Movie Title': titles,
    'Year of Release': years,
    'IMDB Rating': ratings
})

df.to_csv('imdb_top250.csv', index=False)
driver.quit()

print("✅ IMDb data saved successfully to imdb_top250.csv")
