import requests
import re
from bs4 import BeautifulSoup
url="https://docs.scipy.org/doc/scipy/reference/"
headers={
    'Referer':'https://docs.scipy.org/doc/scipy/reference/',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
a=requests.get(url,headers=headers)
a.encoding='utf-8'
HTML=a.text
# print(HTML)
soup = BeautifulSoup(HTML,'lxml')
#print(soup.find_all('attrs'))
res=soup.find_all('a',{'class':'reference internal'})
print(res)
for i in res:
    print(i.text)
    print(i.attrs['href'])




