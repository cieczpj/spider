import requests
import re
from bs4 import BeautifulSoup
url="http://www.17k.com/list/2933095.html"
headers={
    'Referer':'http://www.17k.com/list/2933095.html',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
response=requests.get(url,headers=headers)
response.encoding='utf-8'
HTML=response.text
print(HTML)
soup = BeautifulSoup(HTML,'lxml')
print(soup.find.all('a'))
