import requests
import re
url="http://www.17k.com/list/2933095.html"
headers={
    'Referer':'http://www.17k.com/list/2933095.html',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
response=requests.get(url)
response.encoding='utf-8'
# r=respose.text
HTML=response.text
# print(HTML)
# compile预编译 适用于文本过长
regex=re.compile('.*(/chapter/2933095/\d{8}.html).*')
result=regex.findall(HTML)
# print(result)
url = ['http://www.17k.com' + i for i in result]
#print(url)
print()
for j in url:
    respose = requests.get(j)
    respose.encoding='utf8'
    r=respose.text
    title=re.compile('<h1>\n(.*)</h1>')
    result1=title.findall(respose.text,re.S)
    file=re.compile('&#12288;&#12288;(.*?)<br /><br />')
    result2=file.findall(respose.text,re.S)
    temp=result1+result2
    title2=re.compile('<title>(.*-.*? .*?)-')
    result3=title2.findall(respose.text,re.S)
    #print(temp)
    with open('/home/admin1/Desktop/1.14(2)/.txt'.format(result3[0]),mode='w',encoding='utf8')as f:
        for k in temp:
            f.write(k)