import re
import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import multiprocessing


def Spider_for_dytt(queue):
    """
    processing 1:
        Responsible for getting all the a links of all pages
    :param queue: processing queue

    """
    driver = webdriver.Chrome() # create a web driver.
    waite = WebDriverWait(driver,10) # set web waite.
    url = 'http://www.ygdy8.net/html/gndy/oumei/index.html' # initial url.

    # request initial url. about 2lines.
    driver.get(url=url)
    get_a_links(waite, queue)

    # get all page in target HTML.about 4 lines.
    for index in range(2,208):
        # using selenium method "Select" to change page index.
        select_index = Select(driver.find_element_by_xpath('//div[@class="co_content8"]/div[1]/select'))
        select_index.select_by_visible_text(str(index))
        get_a_links(waite,queue)
    driver.close()

def get_a_links(waite,queue):
    """
    :param waite: web waite, waite time is 10 sec.
    :param queue: processing queue.

    """
    # get all a links in current page.
    a_links = waite.until(EC.presence_of_all_elements_located((By.XPATH,
                                                               '//div[@class="co_content8"]/ul/table/tbody/tr[2]/td[2]/b/a[2]')))
    # get movie url and movie name in current a link.
    movie_urls = [movie_url.get_attribute('href') for movie_url in a_links]
    movie_names = [movie_url.text for movie_url in a_links]

    # zip for urls and names. like ('url','name')
    for m_url_name in zip(movie_urls,movie_names):
        print(m_url_name)
        queue.put(m_url_name) # put in queue.


def get_thunder_url(queue):
    """
    processing 2:
        Responsible for getting all the movie thunder url of current page.
        writing in mongo at movie name and thunder url.
    :param queue:
    :return:
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,10)

    while True:
        movie_url,movie_name = queue.get() # process wait until have any elements in queue.

        # start get thunder url.about 6 lines.
        driver.get(movie_url)
        movie_xpath = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@id="Zoom"]/span/table/tbody/tr/td/a')))
        thunder_url_HTML = movie_xpath.get_attribute('outerHTML')
        regex_thunder = re.compile('(thunder://.*?==)')
        try:
            thunder_url = regex_thunder.findall(thunder_url_HTML)[0] # get thunder url,using re.
            results = {'movie_name':movie_name,'thunder_url':thunder_url}

            # start write to mongo
            write_to_mongo(results)
        except:
            print('thunder_url Failed')
        if queue.empty(): # break while loop, if have not any elements in this queue.
            break
    driver.close()


def write_to_mongo(results):
    """
    write to mongodb
    :param results: have movie name and movie thunder url.
    :return:
    """
    mongoClient = pymongo.MongoClient('mongodb://localhost:27017/')
    db = mongoClient['dytt']
    col = db["result"]
    col.insert(results)
    mongoClient.close()





if __name__ == "__main__":

    queue = multiprocessing.Queue() # create process queue.

    # start P1,P2,about 4 lines.
    P_Spider_for_dytt = multiprocessing.Process(target=Spider_for_dytt,args=(queue,))
    P_get_ftp_url = multiprocessing.Process(target=get_thunder_url,args=(queue,))
    P_Spider_for_dytt.start()
    P_get_ftp_url.start()

    # join process.
    P_Spider_for_dytt.join()
    P_get_ftp_url.join()