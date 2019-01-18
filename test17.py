import requests
import threading   # 多线程


def request_Image(path):
    """
    请求源网址
    """
    headers={}
    urls = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808"
    response = requests.get(url=urls)
    HTML = response.text
    url_son = HTML.split('\r\n')[:-1]
    
    request_iamge(url_son,path)

def request_iamge(url_son,path):
    """
    请求小图片并下载
    """
    headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    for url in url_son:
        try:
            resposnse_for_image = requests.get(url,headers=headers,timeout=1,allow_redirects=False)
            content = resposnse_for_image.content
            if b"html" not in content and resposnse_for_image.status_code == 200:
                path_total = path + url.split('/')[-1]
                print("成功图片:",path_total)
                # 没加线程锁
                with open(path_total,mode='wb') as Joker:
                    Joker.write(content)
                    Joker.flush()
            
        except Exception as e:
            print(e)