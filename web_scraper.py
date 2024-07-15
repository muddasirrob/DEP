import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'


response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')


    articles_container = soup.find('ol', class_='row')

    titles = []
    prices = []

    # Loop through each article entry and extract the desired information
    for article in articles_container.find_all('li'):
        title = article.find('h3').find('a')['title']
        price = article.find('p', class_='price_color').get_text(strip=True)

        # Append the data to the lists
        titles.append(title)
        prices.append(price)

    df = pd.DataFrame({
        'Title': titles,
        'Price': prices
    })


    df.to_csv('books.csv', index=False)

    print('Data has been successfully scraped and saved to books.csv')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
