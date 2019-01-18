from  selenium import  webdriver

browser = webdriver.Chrome("/home/admin1/Desktop/chromedriver")
browser.get('https://book.douban.com/tag/%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6')

imgs  = browser.find_elements_by_xpath('//*[@id="subject_list"]/ul/li/div[@class="pic"]/a/img')
titles = browser.find_elements_by_xpath('//*[@id="subject_list"]/ul/li/div[@class="info"]/h2/a')
zuozhe = browser.find_elements_by_xpath('//*[@id="subject_list"]/ul/li/div[@class="info"]/div[@class="pub"]')
for img in imgs:
    print(img.text)
    print(img.get_attribute('src'))

for title in titles:
    print(title.get_attribute('title'))

for i in zuozhe:
    print(i.text)