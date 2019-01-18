import requests
import re

response = requests.get('http://zyk.bjhd.gov.cn/zwdt/hdyw')
response.encoding = "utf8"
HTML = response.text

# compile预编译 适用于文本过长
regex = re.compile('.*?if\(!strLink\){document\.write\(\'<a href="\.(.*shtml)".*\'\)}')
result = regex.findall(HTML)
print(result)
url = ['http://zyk.bjhd.gov.cn/zwdt/hdyw/' + i for i in result]
print(url)