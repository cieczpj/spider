import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

for i in range(0,50):
    if i == 0:
        response = requests.get('http://zyk.bjhd.gov.cn/zwdt/hdyw/index.shtml',headers=headers)
    else:
        response = requests.get('http://zyk.bjhd.gov.cn/zwdt/hdyw/index_{}.shtml'.format(i),headers=headers)
    with open(xxxx,mode='w') as f:
        f.write(response.text)
    # print(response.url)