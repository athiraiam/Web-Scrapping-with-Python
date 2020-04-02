from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://nishantranjan.in/').text
soup = BeautifulSoup(source, 'lxml')
csv_file = open("all_post.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Article Name", "Posted On", "Summary", "Article Link Reference"])
for article in soup.find_all('article'):
    content = article.header
    headline = content.a.text
#    print(headline)
    date_info = content.small.text
    date_info = date_info.split(",")
    date_info = date_info[0] + "," +date_info[1][:5]
#    print(date_info)
    summary = content.p.text
 #   print(summary)
    plink = "https://nishantranjan.in"
    clink = article.find('a')['href']
    clink = clink.replace(" ", "%20")
    link = plink + clink
#    print(link)
    csv_writer.writerow([headline, date_info, summary, link])
    print("*************************")
csv_file.close()












"""
content = soup.article.header
headline = content.a.text
print(headline)
#date_info = content.small.text
#date_info = date_info.split(",")
#date_info = date_info[0] + "," +date_info[1][:5]
#print(date_info)
#summary = content.p.text
#print(summary)
"""


"""
title = soup.title.text
print(title)
"""
"""
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
#print(article.prettify())
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
#print(vid_id)
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except:
        yt_link = None
    print(yt_link)
    print("*********************")

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

"""
