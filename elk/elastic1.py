import requests
from bs4 import BeautifulSoup

url_vn='https://vnexpress.net/category/day?cateid=1001005&fromdate=1601510400&todate=1602201600&allcate=1001005&page='
i = 1
is_break = False
while not is_break:
    url = url_vn + str(i)
    print("URL: {}".format(url))
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    #article = soup.find('article', class_='item-news item-news-common')
    #if article is None:
    if not soup.find('article', class_='item-news item-news-common'):
        print("het roi nhe")
        is_break = True
    else:
        try:
            datas= soup.find_all('h3', class_='title-news')
            for data in datas:
                title = data.find('a')
                if title:
                    print(title.get('title'))
                else:
                    print('d co gi ca')
        except:
            print('co loi: {}'.format(url))
            #ghi log ra file
        i+=1
        
    

