from  selenium import  webdriver
from  selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time
driver = webdriver.Chrome('/home/admin1/Desktop/chromedriver')
driver.get('http://www.taobao.com')
wait = WebDriverWait(driver,10)

q = wait.until(EC.presence_of_element_located((By.ID,'q')))
q.send_keys('美食')
time.sleep(1)
q.send_keys(Keys.ENTER)
for i in range(99):

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    prices = driver.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[1]/div[1]/strong')
    for price in prices:
        res_price = price.text
        print(res_price)

    sure = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]')
    print(sure)
    time.sleep(2)
    sure.click()