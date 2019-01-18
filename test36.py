from  selenium import  webdriver
from selenium.webdriver import  ActionChains
from selenium.webdriver.common.alert import Alert
browser = webdriver.Chrome('/home/admin1/Desktop/chromedriver')

browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult') # 切换到框架
target = browser.find_element_by_id('droppable')
source = browser.find_element_by_id('draggable')
actions = ActionChains(browser) # 初始化一个行动链
actions.drag_and_drop(source=source,target=target) # 拖到目标并释放鼠标左键
actions.perform() # 执行

# 解决alter弹窗
alter_ = Alert(browser)  # 初始化一个Alter
alter_.accept() # 接受,类似于点击确定
browser.switch_to.parent_frame() # 找回父框
print(browser.find_element_by_id('submitBTN'))