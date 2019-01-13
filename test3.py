import urllib.request 
import urllib.parse

headers={'Referer':'http://www.baidu.com/','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
parameters = {"wd":"%E8%83%A1%E6%97%BA"}
data =urllib.parse.urlencode(parameters,encoding='utf8')
zhang=urllib.request.Request(url='http://www.baidu.com/s?'+data,method='GET')
response = urllib.request.urlopen(zhang)
html=response.read().decode('utf8')
print(html)
with open("/home/admin1/Desktop/test3.txt",mode='w') as f:
  f.write(html)




