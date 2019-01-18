import requests
import re


def spider_for_17K():
    url = "http://www.17k.com/list/2933095.html"
    
    response = requests.get(url,headers=headers)
    response.encoding = 'utf8'
    HTML = response.text
    regex  = re.compile('.*<a\starget="_blank"\shref="(.*?)"\stitle.*')
    con_url = regex.findall(HTML)  #找到所有的页面详情的a链接
    all_con_url = ['http://www.17k.com'+url_ for url_ in con_url][1:]
    # 开始爬取页面详情
    get_content(all_con_url)

def get_content(all_con_url):
    for url in all_con_url:
        response  =  requests.get(url)
        response.encoding = 'utf8'
        HTML = response.text
        regex_html = re.compile('.*?&#12288;&#12288;(.*?)<br /><br />')
        result = regex_html.findall(HTML)[:-1]
        title = re.search('.*<h1>\n(.*)</h1>',HTML).group(1).strip()
        
        xiaoshuo = ''.join(result) # 将正则匹配到的列表子元素拼接,就成了完整的内容
        # 写入本地
        write_local(xiaoshuo,title)
        

def  write_local(xiaoshuo,title):
    path = 'xxxxx' + title
    with open(path,mode='w') as f:
        f.write(xiaoshuo)
     



if __name__ == "__main__":
    headers = {
        'Referer':'http://www.17k.com/list/2933095.html',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    spider_for_17K()