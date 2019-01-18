import requests
import re
content = requests.get('https://book.douban.com/').text
print(content)
regex = re.compile('<a href="(\S+)"\stitle="(.*?)">',re.S)
result = re.findall(regex,content)
print(result)