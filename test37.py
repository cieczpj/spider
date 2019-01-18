from  selenium import  webdriver
from selenium.webdriver import  ActionChains
from selenium.webdriver.common.alert import Alert
import  time


browser = webdriver.Chrome('/home/admin1/Desktop/chromedriver')
for j in range(1,11):
    if j == 1:
        browser.get('https://www.dytt8.net/html/gndy/dyzz/index.html')
    else:
        browser.get('https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(j))
        time.sleep(1)
        #input.send_keys('电影')  # 输入python
        #time.sleep(1)  
        #input.send_keys(Keys.ENTER) # 模拟按下回车
        
    #driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   
    #time.sleep(1)    
    res = browser.find_elements_by_xpath('//*[@id="header"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/ul/table/tbody/tr[2]/td[2]/b/a')
    for a in res:
        titles = a.text
        print(a.get_attribute('href')+"    "+titles)
        #print(a.get_attribute('href'))
        #print(titles)


browser.get('https://www.dytt8.net/html/gndy/dyzz/20190117/58089.html')
res1 = browser.find_elements_by_xpath('//*[@id="Zoom"]/span/font[1]/a')
for b in res1:
    print(b.get_attribute('href'))










