import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
print(response.status_code)
print(soup.title.text)

quote_blocks = soup.find_all("div", class_="quote")

for quote in quote_blocks:
  text = quote.find("span", class_= "text").text
  author = quote.find("small", class_= "author").text

  print(f"{text} - {author}")