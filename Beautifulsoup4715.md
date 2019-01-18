# Beautifulsoup4

适合懂HTML的人员

### 基本使用

- python标准库 BeautifulSoup(markup,'html.parser')
- lxml HTML解析器 BeautifulSoup（markup，‘lxml’） 最常用
- lxml XML 解析器 BeautifulSoup（markup，‘xml’）
- html5lib 解析器 BeautifulSoup（markup，‘html5lib）

###  标签选择器

- 选择元素

  ```python
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <title>百度一下，你就知道 </title><style
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.title)  # 直接返回标签
  print(type(soup.title))  #标签的类型，返回tag
  print(soup.meta)  # 当有多个标签的时候返回第一个找到的，
  print(soup.link)
  print(soup.p)  # 若无则返回None获取名称
  ```

- 获取名称

  ```python
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <title>百度一下，你就知道 </title><style
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.title.name)    # 获取标签的名称
  print(soup.meta.attrs) # 获取该标签的所有属性
  ```

- 获取属性

  ```python
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <title>百度一下，你就知道 </title><style
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.meta['content'])    # 获取标签的属性，若获取不到则crash
  print(soup.meta.attrs['content'])    # 获取标签的属性，若获取不到则crash
  ```

- 获取内容

  ```python
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <title>百度一下，你就知道 </title><style
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.title.string)    # 获取标签的内容
  print(soup.meta.string)    # 获取不到返回None
  print(soup.title.text) # 高级获取方法,标签里还有标签
  print(soup.title.get_text())# 高级获取方法,标签里还有标签
  ```

- 嵌套选择

  ```python
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <head><title>百度一下，你就知道 </title></head><style
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.head.title.string)    # 嵌套获取标签的内容
  print(soup.head.p.string)    # 获取不到crash
  ```

- 子节点和子孙节点

  ```python
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <head><title>百度一下，你就知道 </title></head><style
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.head.contents)    # 获取某以节点下的子节点，以列表形式返回，包含换行符
  print(list(soup.head.descendants)) # 获取所有的子孙节点
  
  ```

  ```python
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <head><title>百度一下，你就知道 </title></head><style
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.head.children)    # 获取某以节点下的子节点,返回的是一个迭代对象
  for i,child in enumerate(soup.head.children):  # 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
      print(i,child)
  ```

  ```python
  # 获取子孙节点
  
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <a><p>hahah</p></a>
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <p><title>百度一下，你就知道 </p></head><style>
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.prettify)
  print(soup.head.descendants)    # 获取某以节点下的子节点和孙节点,返回的是一个迭代对象
  for i,child in enumerate(soup.head.descendants):  # 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
      print(i,child)
  ```

- 父节点和主父节点

  ```python
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <a><p>hahah</p></a>
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <p><title>百度一下，你就知道 </p></head><style>
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.p.parent)  # 找到第一个p标签返回父节点
  ```

  ```python
  # 祖先节点
  
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <a><p>hahah</p></a>
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <p><title>百度一下，你就知道 </p></head><style>
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.p.parents)  # 找到第一个p标签返回祖父节点，类似于一层一层往外打印
  print(list(enumerate(soup.p.parents)))
  ```

- 兄弟节点

  ```python
  html="""
  
  <html xmlns=http://www.w3.org/1999/xhtml><head>  
  <meta http-equiv=Content-Type content="text/html;charset=utf-8">
  <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">
  <a><p>hahah</p></a>
  <meta content=always name=referrer> 
  <link rel="shortcut icon" href=/favicon.ico type=image/x-icon>
  <link rel=icon sizes=any mask href=//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg>
  <p><title>百度一下，你就知道 </p></head><style>
  """
  
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(list(enumerate(soup.meta.next_siblings))) # 获取下一个兄弟节点，sibilings包括符号
  print(list(enumerate(soup.meta.previous_siblings))) # 获取上一个兄弟节点
  ```

  ------

  ### 标准选择器

  find_all(name,attrs,recursive,text,**kwargs)

  可根据标签名、属性、内容查找文档

  ```python
  # name
  html='''
  <div class="s-pic-content"> 
  <ul class="s-news-content-imgs clearfix">
  <li class="item-img-wrap"> 
  <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1047039477,1284324308&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=37819A40541111CC44336FB30300C00A" height="119" width="179"> </a> 
  </li><li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话">
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=586689194,1936681765&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=D4834AB61046C4EC0CBF2AA20300701E" height="119" width="179"> </a> 
  </li><li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3859052939,833161477&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=AAD05B876B72128450B06DB303001091" height="119" width="179"> </a>  
  </li>
  </ul>
  </div>
  '''
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  print(soup.find_all('p')) # 找出所有ul标签,无则返回空的列表
  print(type(soup.find_all('ul')[0]))
  print('------------')
  for ul in soup.find_all('ul'):
      print(ul)
      print(ul.find_all('li'))  # 找到ul结果下的所有li
      
  # # a_obj = soup.find_all('a')
  # print(a_obj) # 列表中的都是对象
  # print(a_obj[0]['href'])
  # print(a_obj[0].text)
  # a_obj = soup.find_all(['a','li']) # 找到所有的a和li
  # print(a_obj)
  # a_obj = soup.find_all('a',limit=2) # 找到前两个a
  # print(a_obj)
  ```

- atters

  ```python
  html='''
  <div class="s-pic-content"> 
  <ul class="s-news-content-imgs clearfix">
  <li class="item-img-wrap"> 
  <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1047039477,1284324308&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=37819A40541111CC44336FB30300C00A" height="119" width="179"> </a> 
  </li><li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话">
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=586689194,1936681765&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=D4834AB61046C4EC0CBF2AA20300701E" height="119" width="179"> </a> 
  </li><li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3859052939,833161477&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=AAD05B876B72128450B06DB303001091" height="119" width="179"> </a>  
  </li>
  </ul>
  </div>
  '''
  from bs4 import BeautifulSoup
  
  soup = BeautifulSoup(html,'lxml')
  print(soup.find_all(attrs={'class':'s-news-img'}))  # 直接带入属性名和属性值查找
  for attr in soup.find_all(attrs={'class':'s-news-img'}):
      print('\n')
      print(attr)
  ```

  ```python
  html='''
  <div class="s-pic-content"> 
  <ul class="s-news-content-imgs clearfix">
  <li class="item-img-wrap"> 
  <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1047039477,1284324308&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=37819A40541111CC44336FB30300C00A" height="119" width="179"> </a> 
  </li><li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话">
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=586689194,1936681765&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=D4834AB61046C4EC0CBF2AA20300701E" height="119" width="179"> </a> 
  </li><li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3859052939,833161477&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=AAD05B876B72128450B06DB303001091" height="119" width="179"> </a>  
  </li>
  </ul>
  </div>
  '''
  from bs4 import BeautifulSoup
  
  soup = BeautifulSoup(html,'lxml')
  print(soup.find_all(class_='item-img-wrap'))  # 可以直接带入通用属性名查找，但是class与系统名冲突，所以规定class_
  
  ```

  ```python
  html='''
  <div class="s-pic-content"> 
  <ul class="s-news-content-imgs clearfix">
  <li class="item-img-wrap"> 
  <p>Joker</p>
  <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1047039477,1284324308&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=37819A40541111CC44336FB30300C00A" height="119" width="179"> </a> 
  </li>
  <li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话">
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=586689194,1936681765&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=D4834AB61046C4EC0CBF2AA20300701E" height="119" width="179"> </a> 
  </li>
  <li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3859052939,833161477&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=AAD05B876B72128450B06DB303001091" height="119" width="179"> </a>  
  </li>
  </ul>
  </div>
  '''
  from bs4 import BeautifulSoup
  
  soup = BeautifulSoup(html,'lxml')
  print(soup.find_all(text='Joker'))  # 查找文本内容，若无返回空列表
  li_obj=soup.find_all('li',{'class':"item-img-wrap"})
  print(li_obj)
  
  ```

  find(name,attrs,recursive,**kwargs) 返回第一个元素，与find_all用法相同

### CSS选择器

- select 返回的是列表

  ```python
  html='''
  <div class="s-pic-content"> 
  <ul class="s-news-content-imgs clearfix">
  <li class="item-img-wrap"> 
  <p id="name">Joker</p>
  <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1047039477,1284324308&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=37819A40541111CC44336FB30300C00A" height="119" width="179"> </a> 
  </li>
  <li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话">
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=586689194,1936681765&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=D4834AB61046C4EC0CBF2AA20300701E" height="119" width="179"> </a> 
  </li>
  <li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3859052939,833161477&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=AAD05B876B72128450B06DB303001091" height="119" width="179"> </a>  
  </li>
  </ul>
  </div>
  '''
  
  from bs4 import BeautifulSoup
  
  soup = BeautifulSoup(html,'lxml')
  print(soup.select('.s-pic-content'))  # 类选择器
  print(soup.select('#name')) # id选择器 ，返回带标签的列表
  print(soup.select('.item-img-wrap #name'))  # 一般的选择器写法都支持
  ```

- 获取属性

  ```python
  html='''
  <div class="s-pic-content"> 
  <ul class="s-news-content-imgs clearfix">
  <li class="item-img-wrap"> 
  <p id="name">Joker</p>
  <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1047039477,1284324308&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=37819A40541111CC44336FB30300C00A" height="119" width="179"> </a> 
  </li>
  <li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话">
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=586689194,1936681765&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=D4834AB61046C4EC0CBF2AA20300701E" height="119" width="179"> </a> 
  </li>
  <li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3859052939,833161477&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=AAD05B876B72128450B06DB303001091" height="119" width="179"> </a>  
  </li>
  </ul>
  </div>
  '''
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  for ul in soup.select('ul'):
      print(ul['class'])
      print(ul.attrs['class'])
  ```

- 获取内容

  ```python
  html='''
  <div class="s-pic-content"> 
  <ul class="s-news-content-imgs clearfix">
  <li class="item-img-wrap"> 
  <p id="name">Joker</p>
  <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=1047039477,1284324308&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=37819A40541111CC44336FB30300C00A" height="119" width="179"> </a> 
  </li>
  <li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话">
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=586689194,1936681765&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=D4834AB61046C4EC0CBF2AA20300701E" height="119" width="179"> </a> 
  </li>
  <li class="item-img-wrap"> <a href="https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_12701422858420441605%22%7D&amp;n_type=0&amp;p_from=1" target="_blank" data-click="LOG_LINK" title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话" data-title="十三届全国人大一次会议在京闭幕 习近平发表重要讲话"> 
  <img class="s-news-img" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3859052939,833161477&amp;fm=173&amp;app=12&amp;f=JPEG?w=218&amp;h=146&amp;s=AAD05B876B72128450B06DB303001091" height="119" width="179"> </a>  
  </li>
  </ul>
  </div>
  '''
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html,'lxml')
  for i in soup.select('p'):
      print(i.get_text())  # 直接获得标签文本内容
     
  ```

---

# 总结

- 推荐使用lxml解析库
- 标签选择筛选功能弱,但是速度快
- 建议使用find(),find_all()查询匹配单个结果或者多个结果
- 如果对CSS选择器熟悉建议使用select()
- 记住常用的获取属性和文本的方法



# Homework

1.爬取[酷狗音乐TOP500](https://www.kugou.com/yy/rank/home/1-8888.html?from=rank)歌曲名称

2.两个选择获取音乐地址

- 1.破解酷狗网页端JS

- 2.手机端抓包获取api地址

  - ```python
    
    # 获得hash json
    http://mobilecdn.kugou.com/api/v3/search/song?format=json&keyword=url编码的歌名&page=1&pagesize=20&showtype=1%20---------------------%20%E4%BD%9C%E8%80%85%EF%BC%9A%E5%85%AC%E4%BC%97%E5%8F%B7%E7%81%AB%E7%82%8E%E4%B8%80%E7%AC%91%E5%80%BE%E5%9F%8E%20%E6%9D%A5%E6%BA%90%EF%BC%9ACSDN%20%E5%8E%9F%E6%96%87%EF%BC%9Ahttps://blog.csdn.net/qq_14955245/article/details/79467618%20%E7%89%88%E6%9D%83%E5%A3%B0%E6%98%8E%EF%BC%9A%E6%9C%AC%E6%96%87%E4%B8%BA%E5%8D%9A%E4%B8%BB%E5%8E%9F%E5%88%9B%E6%96%87%E7%AB%A0%EF%BC%8C%E8%BD%AC%E8%BD%BD%E8%AF%B7%E9%99%84%E4%B8%8A%E5%8D%9A%E6%96%87%E9%93%BE%E6%8E%A5%EF%BC%81
            
    # 获得音乐地址
    http://www.kugou.com/yy/index.php?r=play/getdata&hash=上面得到的hash值
    ```

进阶：

​	爬取[统计年鉴2018](http://www.stats.gov.cn/tjsj/ndsj/2018/indexch.htm)

​	注意,由于爬取下来的是图片,你需要调用接口将图片转换为文字然后清洗数据存为CSV模式.

​	提供百度API接口(http://ai.baidu.com/tech/ocr/)

​	API文档(https://ai.baidu.com/docs#/OCR-API/top)

