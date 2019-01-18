from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/home/admin1/Desktop/chromedriver")
driver.get("http://www.taobao.com")
elem = driver.find_element_by_css_selector("#q")
elem.clear()
elem.send_keys("美食")
search = driver.find_element_by_css_selector("button")
search.click()
#elem.send_keys(Keys.RETURN)
print(driver.page_source)
#driver.save_screenshot("text.png")
