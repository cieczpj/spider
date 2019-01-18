import urllib.request  # Python的基础爬虫库，后面不会用,但是必须要会！！！
import urllib.parse

headers={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
parameters = {
    "wd":"胡旺",
}
# post 加 bytes
# get 不需要
data =  urllib.parse.urlencode(parameters)
print(data)
# wd=English
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E8%83%A1%E6%97%BA&oq=%2526gt%253Bnglish&rsv_pq=b80ca9950001107f&rsv_t=4ddeh63ph5R6UKDOKzotHDKpBUNptQLVmtkl9ARHmoQJOJ5kmzWNxGR%2BWEQ&rqlang=cn&rsv_enter=1&rsv_sug3=9&rsv_sug1=8&rsv_sug7=101&rsv_sug2=0&inputT=2206&rsv_sug4=1249690&rsv_sug=1
# https://www.baidu.com/s?wd=English
# http://www.baidu.com

# data 只是接受POST 参数
# get请求的时候要拼接路径
# request_ = urllib.request.Request(url='http://www.baidu.com/s?'+data
# ,method="GET")
# response = urllib.request.urlopen(request_)
# print(response.url)
# HTML=response.read().decode()
# print(HTML)
# with open("/Users/huwang/Desktop/test.txt",mode='w') as f:
#     f.write(HTML)