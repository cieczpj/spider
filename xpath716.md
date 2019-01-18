# xpath

适合小白人员

### XPath概览

XPath 的选择功能十分强大，它提供了非常简洁明了的路径选择表达式，另外它还提供了超过 100 个内建函数用于字符串、数值、时间的匹配以及节点、序列的处理等等，几乎所有我们想要定位的节点都可以用XPath来选择。

XPath 于 1999 年 11 月 16 日 成为 W3C 标准，它被设计为供 XSLT、XPointer 以及其他 XML 解析软件使用，更多的文档可以访问其官方网站：<https://www.w3.org/TR/xpath/>。



### XPath常用规则

我们现用表格列举一下几个常用规则：

表达式描述
nodename选取此节点的所有子节点
/从当前节点选取直接子节点
//从当前节点选取子孙节点
.选取当前节点
..选取当前节点的父节点
@选取属性

在这里列出了XPath的常用匹配规则，例如 / 代表选取直接子节点，// 代表选择所有子孙节点，. 代表选取当前节点，.. 代表选取当前节点的父节点，@ 则是加了属性的限定，选取匹配属性的特定节点。

```xml
//title[@lang=’eng’]
```

这就是一个 XPath 规则，它就代表选择所有名称为 title，同时属性 lang 的值为 eng 的节点。

在后文我们会介绍 XPath 的详细用法，通过 Python 的 LXML 库利用 XPath 进行 HTML 的解析。

**注意:**

​	- 可以把xpath理解为一层一层的捕获

### 实例引入

```python
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
```

我们也可以直接读取文本文件进行解析，示例如下：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

"""
test.html
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
"""
```

### 所有节点

我们一般会用 // 开头的 XPath 规则来选取所有符合要求的节点，以上文的 HTML 文本为例，如果我们要选取所有节点，可以这样实现：

```python
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)
```

此处匹配也可以指定节点名称，如果我们想获取所有 li 节点

```python
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')
print(result)
print(result[0])
```

### 子节点

我们通过 / 或 // 即可查找元素的子节点或子孙节点，加入我们现在想选择 li 节点所有直接 a 子节点，可以这样来实现：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)


## 此处的 / 是选取直接子节点，如果我们要获取所有子孙节点就该使用 // 了，例如我们要获取 ul 节点下的所有子孙 a 节点，可以这样来实现：
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//ul//a')
print(result)

#我们用 //ul/a 就无法获取任何结果了，因为 / 是获取直接子节点，而在 ul 节点下没有直接的 a 子节点，只有 li 节点，所以无法获取任何匹配结果
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//ul/a')
print(result)
```

### 父节点

我们现在首先选中 href 是 link4.html 的 a 节点，然后再获取其父节点，然后再获取其 class 属性，代码如下：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/../@class')
print(result)

# 我们也可以通过 parent:: 来获取父节点，
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/parent::*/@class')
print(result)
```

### 属性匹配

在选取的时候我们还可以用 @ 符号进行属性过滤，比如在这里如果我们要选取 class 为 item-1 的 li 节点，可以这样实现

```python
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)
```

### 文本获取

 XPath 中的 text() 方法可以获取节点中的文本

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
```

### 属性获取

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
```

### 属性多值匹配

```python
from lxml import etree
text = '''
<li class="li li-first"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result)

#################
from lxml import etree
text = '''
<li class="li li-first"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
```

### 多属性匹配

```python
from lxml import etree
text = '''
<li class="li li-first" name="item"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)
```

**注意:**

```tex
这里的 and 其实是 XPath 中的运算符，另外还有很多运算符，如 or、mod 等等，在此总结如下：

运算符描述实例返回值
or或price=9.80 or price=9.70如果 price 是 9.80，则返回 true。如果 price 是 9.50，则返回 false。
and与price>9.00 and price<9.90如果 price 是 9.80，则返回 true。如果 price 是 8.50，则返回 false。
mod计算除法的余数5 mod 21
\计算两个节点集//book \//cd返回所有拥有 book 和 cd 元素的节点集
+加法6 + 410
-减法6 - 42
*乘法6 * 424
div除法8 div 42
=等于price=9.80如果 price 是 9.80，则返回 true。如果 price 是 9.90，则返回 false。
!=不等于price!=9.80如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。
<小于price<9.80如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。
<=小于或等于price<=9.80如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。
>大于price>9.80如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。
>=大于或等于price>=9.80如果 price 是 9.90，则返回 true。如果 price 是 9.70，则返回 false。

此表参考来源：http://www.w3school.com.cn/xpath/xpath_operators.asp。
```

### 按序选择

```python
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)
```



### Xpath 高阶

```python
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
# 第一次选择我们调用了 ancestor 轴，可以获取所有祖先节点，其后需要跟两个冒号，然后是节点的选择器，这里我们直接使用了 *，表示匹配所有节点，因此返回结果是第一个 li 节点的所有祖先节点，包括 html，body，div，ul。
result = html.xpath('//li[1]/ancestor::*')
print(result)
# 第二次选择我们又加了限定条件，这次在冒号后面加了 div，这样得到的结果就只有 div 这个祖先节点了。
result = html.xpath('//li[1]/ancestor::div')
print(result)
# 第三次选择我们调用了 attribute 轴，可以获取所有属性值，其后跟的选择器还是 *，这代表获取节点的所有属性，返回值就是 li 节点的所有属性值。
result = html.xpath('//li[1]/attribute::*')
print(result)
# 第四次选择我们调用了 child 轴，可以获取所有直接子节点，在这里我们又加了限定条件选取 href 属性为 link1.html 的 a 节点。
result = html.xpath('//li[1]/child::a[@href="https://ask.hellobi.com/link1.html"]')
print(result)
# 第五次选择我们调用了 descendant 轴，可以获取所有子孙节点，这里我们又加了限定条件获取 span 节点，所以返回的就是只包含 span 节点而没有 a 节点。
result = html.xpath('//li[1]/descendant::span')
print(result)
# 第六次选择我们调用了 following 轴，可以获取当前节点之后的所有节点，这里我们虽然使用的是 * 匹配，但又加了索引选择，所以只获取了第二个后续节点。
result = html.xpath('//li[1]/following::*[2]')
print(result)
# 第七次选择我们调用了 following-sibling 轴，可以获取当前节点之后的所有同级节点，这里我们使用的是 * 匹配，所以获取了所有后续同级节点。
result = html.xpath('//li[1]/following-sibling::*')
print(result)
```

[更多关于轴参考](http://www.w3school.com.cn/xpath/xpath_axes.asp)

# Homework

1.使用xpath爬取[海贼王漫画图片](http://op.hanhande.net/shtml/meitu.shtml)中的所有图片,并写入本地

- 进阶:
  -  搭建一个通用爬虫爬取北京天津安徽市政府网站,爬取内容：文章标题,文章内容，文章时间，文章作者.
  - 以json文件配置
    - 也就是说json文件中放入的是xpath或者bs4或者re的匹配规则,这样的话到如果后面还有相似的政府类网站只需要配置json文件就可以了.
  - 网址:
    - 1-5页
      - http://tjbdfy.chinacourt.org/article/index/id/MzQ3MjAwNjAwNCACAAA/page/1.shtml 
    - 1-6页
      - http://bjdxfy.chinacourt.org/public/more.php?p=1&LocationID=0201000000&sub=
    - 2-20页
      - http://www.czfy.gov.cn/html/tpcz/index_2.html

- Json文件类似于

  ```json
  {
      "website": "大兴区法院",
      "type": "要闻",
      "table_name":"newscourt",
      "articleProvinceid":"1",
      "articleCentralid":"435",
      "spider_url": "http://bjdxfy.chinacourt.org/public/more.php?p=[]&LocationID=0201000000&sub=",
      "strat_page":"1",
      "max_page": "1",
      "spider_method": "0",
      "threading_num": "1",
      "encoding": "gbk",
      "headers": "0",
      "strip_url":"",
      "plus_url":"http://bjdxfy.chinacourt.org",
      "conten_list_rule": {
          "method": "xpath",
          "args": "//table/tr/td[@class=\"td_line\"]/a/@href"
      },
      "target": {
          "articleTitle": {
              "method": "xpath",
              "args": "//p[@align=\"center\"]/font/b/text()"
          },
          "articleTime": {
              "method": "re",
              "args": ".*?发布时间：(\\d{4}-\\d{2}-\\d{2}).*?"
          },
          "articleAuthor": {
              "method": "re",
              "args": "作者：(.*)&nbsp;&nbsp;发布时间"
          },
  }
  ```


​	

​	