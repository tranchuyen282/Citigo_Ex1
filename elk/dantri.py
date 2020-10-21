import requests
from bs4 import BeautifulSoup

url = 'https://dantri.com.vn/xa-hoi/bao-so-8-do-thang-vao-mien-trung-pham-vi-anh-huong-rat-rong-20201021104528371.htm'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.find('h1', {'class':'dt-news__title'}).text.strip()

#summary
summary = soup.find('div', {'class':'dt-news__sapo'}).find('h2').get_text().strip()

#time public
time = soup.find('span', attrs={'class':'dt-news__time'}).get_text()

#content
content = ""
tag_p = soup.find('div', {'class':'dt-news__content'}).findAll('p')
size = len(tag_p)
author = ""
i=1
for p in tag_p:
    if i < size:
        content += p.get_text().strip()
        i += 1
    else:
        author = p.get_text().strip()

#tag
tag=''
tags = soup.find('ul', {'class':'dt-news__tag-list'}).findAll('li')
for t in tags:
    tag = tag + t.text.strip() + ';'
print(tag)

# print(title)
# print(time)
# print(summary)
# print(content)
# print(author)
