import urllib.request
import urllib.parse
url = 'http://www.17k.com/chapter/2933095/36699279.html'
response =urllib.request.urlopen(url)
#print(response.read().decode('utf8'))
HTML=response.read().decode('utf8')
with open("/home/admin1/Desktop/test6.txt",mode='w') as f:
    f.write(HTML)
