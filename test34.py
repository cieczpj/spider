from selenium import webdriver

driver = webdriver.Chrome("/home/admin1/Desktop/chromedriver")
driver.get('https://book.douban.com/tag/%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6')
imgs = driver.find_elements_by_xpath(
    '//*[@id="subject_list"]/ul/li/div[1]/a/img')
titles = driver.find_elements_by_xpath(
    '//*[@id="subject_list"]/ul/li/div[2]/h2/a')
auths = driver.find_elements_by_xpath(
    '//*[@id="subject_list"]/ul/li/div[2]/div[1]')
for img, title, auth in zip(imgs, titles, auths):
    print(title.get_attribute('title'), img.get_attribute(
        'src'), auth.text.split(' / ')[0])