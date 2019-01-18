import re
content='type="submit" id="su" value="百度一下" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>输入法</span></div><ul id="mMenu">'
res4=re.match('type="submit" id="su" value="(百度一下)" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>(输入法)</span></div><ul id="mMenu">',content)
res=re.match('.*value="(\w\w\w\w).*<span>(输\w\w).*',content)
print(res4.group(1,2))
print(res.group(1,2))
