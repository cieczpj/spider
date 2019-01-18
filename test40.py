from  selenium import  webdriver
from selenium.webdriver.common.keys import Keys

import  time
driver = webdriver.Chrome('/home/admin1/Desktop/chromedriver')
driver.get('http://www.taobao.com')

q = driver.find_element_by_id('q')
q.send_keys('美食')
time.sleep(1)
button = driver.find_element_by_tag_name('button')
button.click()
for i in range(99):

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    prices = driver.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[1]/div[1]/strong')
    for price in prices:
        res_price = price.text
        print(res_price)

    sure = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/input')
    sure.send_keys(Keys.ENTER)