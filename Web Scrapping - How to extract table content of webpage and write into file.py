import requests
from bs4 import BeautifulSoup

link = "https://www.espn.in/nba/player/_/id/3992/james-harden"

response = requests.get(link)
headers = {'User-Agent': 'Chrome/80.0.3987.162'}
soup = BeautifulSoup(response.content, "html.parser")
tables = soup.find_all("table", class_= "Table Table--align-right")# All the table in webpage will be stored in table
fw = open("table.txt", "w")#Open a file in write mode to write the extracted table content
for table in tables:#Loop over individual table
    for row in table.find_all('tr'): # Loop over each row
        for cell in row:# Loop over each cell 
            fw.write(cell.text.ljust(10))# ljust is a string method to introduce padding between cells
        fw.write("\n")
    fw.write("\n\n\n")
fw.close()



