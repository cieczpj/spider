import requests
from  selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymongo

def get_lianjie():    
    driver = webdriver.Chrome('/home/admin1/Desktop/chromedriver')
    driver.get("https://www.taobao.com/")
    elem = driver.find_element_by_css_selector("#q")
    # print(elem)
    # elem.clear()
    elem.send_keys("美食")
    elem.send_keys(Keys.ENTER) # 模拟按下回车
    for i in range(100):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        prices=driver.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[1]/div[1]/strong')
        names=driver.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[2]/a')
        for price ,name in zip(prices,names):
            
            pri=price.text
            na=name.text
            write_local(pri,na)
        
        sure = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]')  
        sure.send_keys(Keys.ENTER)
    
       
def write_local(price,name):
     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
     mydb = myclient["wetaobao"]
     mycol = mydb["taobaomeishi"]
     mycol.insert_one({'name':name,'price':price})
     myclient.close() #!!!!!!!!!!!
if __name__ == "__main__":
    get_lianjie()