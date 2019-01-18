import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
for i in range(0,50):
    if i==0:
        reponse = requests.get('http://zyk.bjhd.gov.cn/zwdt/hdyw/index.shtml',headers=headers)
    else:
        reponse = requests.get('http://zyk.bjhd.gov.cn/zwdt/hdyw/index_{}.shtml'.format(i),headers=headers)
# print(reponse.status.code)
print(reponse.text)
#reponse.encoding="utf8"
with open("/home/admin1/Desktop/test7.txt",mode='w') as zhang:
    zhang.write(reponse.text)
    #print(reponse.url)