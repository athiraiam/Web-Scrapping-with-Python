import requests
from bs4 import BeautifulSoup
link = "https://scrapingclub.com/exercise/detail_basic/"
page = requests.get(link)
content = BeautifulSoup(page.content, "html.parser")

title = content.find('h3',{"class":"card-title"})
print("Title: " , title.text)
d = content.find(text = "$12.99")
print("Price: " , d)
summary = content.find('p', {"class" : "card-text"})
print("Product summary: ", summary.text)
