from bs4 import BeautifulSoup
import requests

url= "http://books.toscrape.com/catalogue/sophies-world_966/index.html"
page = requests.get(url)
#print(page)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_='col-sm-6 product_main')
price = lists.find('p', class_='price_color')
print(price)

