import re
import requests
from bs4 import BeautifulSoup
link= "https://www.espncricinfo.com/india/content/player/253802.html"
page = requests.get(link)
content = BeautifulSoup(page.content, "html.parser")

title = content.find(text = "Virat Kohli" )
print(title)
subtitle = content.find('h3')
subtitle = subtitle.text
print(subtitle)
print("******************************")
pinfo = content.find_all('p', {"class": "ciPlayerinformationtxt"})
for info in pinfo:
    if info.b.text == "Playing role":
        print("\n", info.b.text.strip(), end = " :")
        print(info.span.text.strip())
        continue
    print(info.b.text.strip(), end =" : ")
    if info.b.text == "Major teams":
        info = content.find_all('span', {"style": "white-space: nowrap"})
        for i in info:
            print(i.text.strip(), end ="")
    else:
        print(info.span.text.strip())

