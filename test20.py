import re
content='Extra stings Hello 2134567 World_This is a Regex Demo Extra stings'
res=re.search('Extra stings Hello 2134567 (.*?) is a (.*?) (.*?) Extra stings',content)
print(res.group(1,2,3))