import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
response = requests.get("http://hiphotos.baidu.com/%C9%F1%CA%A5%B7%C9%BB%A22/pic/item/e83aeb19db212b4242a9ad39.jpg",headers=headers)
print(response.content)
with open('/home/admin1/Desktop/test14.jpg','wb') as f:
    f.write(response.content)