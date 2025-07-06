import requests 
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
print(response.status_code)
print(soup.title.text)

book_blocks = soup.find_all("article", class_="product_pod")

for book in book_blocks:
  title = book.find("h3").find("a")["title"]
  price = book.find("p", class_="price_color").text
  rating = book.find("p", class_="star-rating")["class"]

  print(f"{title} - {price} - Rating: {rating} Stars")
