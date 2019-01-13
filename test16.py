import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
url="http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808"
response = requests.get(url)
a=response.text
#print(a)
urls = a.split('\r\n')
print(urls)
for i in urls:
    try:
        response = requests.get(i,timeout=3,allow_redirects=False)
        Zhang=response.content
        # print(Zhang)
        with open('/home/admin1/Desktop/{}'.format(i.split('/')[-1]),'wb') as f:
            f.write(response.content)
            f.flush()
    except Exception as e:
        pass 



