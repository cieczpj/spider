
import requestsfrom bs4 import BeautifulSoup
# dingyi jianxiqi
soup = BeautifulSoup(html,'lxml')
print(soup.title)  # 直接返回标签
print(type(soup.title))  #标签的类型，返回tag
print(soup.meta)  # 当有多个标签的时候返回第一个找到的，
print(soup.link)
print(soup.p)  # 若无则返回None获取名称

html="""
<html xmlns=http://www.w3.org/1999/xhtml><head>  
<meta http-equiv=Content-Type content="text/html;charset=utf-8">
<meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
<meta content=always name=referrer> 
<link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
<link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
<title>百度一下，你就知道 </title><style
"""



#html="""

#<html xmlns=http://www.w3.org/1999/xhtml><head>  
#<meta http-equiv=Content-Type content="text/html;charset=utf-8">
#<meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
#<meta content=always name=referrer> 
#<link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
#<link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
#<title>百度一下，你就知道 </title><style
#"""