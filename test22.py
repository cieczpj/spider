import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
#response = requests.get('http://zyk.bjhd.gov.cn/zwdt/hdyw/')
response = requests.get('http://zyk.bjhd.gov.cn/zwdt/hdyw/')
response.encoding = "utf8"
HTML = response.text

# compile预编译 适用于文本过长
#regex = re.compile('.*?if\(!strLink\){document\.write\(\'<a href="\.(.*shtml)".*\'\)}')
regex = re.compile('.*?if\(!strLink\){document\.write\(\'<a href="\.(.*shtml)".*\'\)}') 

result  = regex.findall(HTML,re.S)
#print(result)
url = ['http://zyk.bjhd.gov.cn/zwdt/hdyw/' + i for i in result]
#print(url)
#urls = url.split('\r\n')
#print(urls)
for i in url:
    response = requests.get(i)
    response.encoding = 'utf8'
    Zhang=response.text
    s=re.findall('<p align="justify">(.*)</p>',Zhang)
    #print(s)
    print(i)
    with open('/home/admin1/Desktop/1.14/'+i.split('/')[-1][0:17]+'.txt','w',) as f:
                f.writelines(s)
                #f.flush()
    