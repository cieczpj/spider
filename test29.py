import requests
from bs4 import BeautifulSoup
import threading
import urllib.parse
import pymongo
import time

def get_music_name(url_list):
    start = time.time()
    for num in url_list:
        print("开始爬取:",num)
        response = requests.get("https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(num))
        HTML = response.text
        soup = BeautifulSoup(HTML,'lxml')
        LIs = soup.select('#rankWrap .pc_temp_songlist ul li')
        NAMES = [li.attrs['title'].split(' - ')[-1] for li in LIs]
        get_music_hash(NAMES)
    end = time.time()
    print("爬虫完毕",end - start)

def get_music_hash(NAMES):
    muisc_name_hash_list = []
    for name in NAMES:
        hash_url = 'http://mobilecdn.kugou.com/api/v3/search/song?format=json&keyword={}&page=1&pagesize=20&showtype=1%20---------------------%20%E4%BD%9C%E8%80%85%EF%BC%9A%E5%85%AC%E4%BC%97%E5%8F%B7%E7%81%AB%E7%82%8E%E4%B8%80%E7%AC%91%E5%80%BE%E5%9F%8E%20%E6%9D%A5%E6%BA%90%EF%BC%9ACSDN%20%E5%8E%9F%E6%96%87%EF%BC%9Ahttps://blog.csdn.net/qq_14955245/article/details/79467618%20%E7%89%88%E6%9D%83%E5%A3%B0%E6%98%8E%EF%BC%9A%E6%9C%AC%E6%96%87%E4%B8%BA%E5%8D%9A%E4%B8%BB%E5%8E%9F%E5%88%9B%E6%96%87%E7%AB%A0%EF%BC%8C%E8%BD%AC%E8%BD%BD%E8%AF%B7%E9%99%84%E4%B8%8A%E5%8D%9A%E6%96%87%E9%93%BE%E6%8E%A5%EF%BC%81'.format(name)
        response  = requests.get(hash_url) # request 库会自动给你编码
        hash_json = response.json() # 转换成json,就类似于字典
        muisc_name_hash = hash_json.get('data').get('info')[0].get('hash')
        muisc_name_hash_list.append(muisc_name_hash)
    get_music_addr(muisc_name_hash_list,NAMES)

def get_music_addr(muisc_name_hash_list,NAMES):
    ADDRS = []
    for hash_ in muisc_name_hash_list:
        addr_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash='+hash_
        response = requests.get(addr_url)
        addr_json = response.json()
        addr = addr_json.get('data').get('play_url')
        ADDRS.append(addr)
    lock.acquire()  # 锁住mongo
    write_local(NAMES,ADDRS)
    lock.release() # 打开mongo

def write_local(NAMES,ADDRS):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["haha"]
    mycol = mydb["kugou"]
    mylist = []
    for name,addr in zip(NAMES,ADDRS):
        mylist.append({name:addr})
    mycol.insert_many(mylist)
    myclient.close() #!!!!!!!!!!!




if __name__ == "__main__":
    # get_music_name()
    url_list = [i for i in range(1,24)]
    lock = threading.Lock() # 创建线程锁
    thread_1 = threading.Thread(target=get_music_name,args=(url_list[:7],))
   
    thread_2 = threading.Thread(target=get_music_name,args=(url_list[7:14],))

    thread_3 = threading.Thread(target=get_music_name,args=(url_list[14:],))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()
    # thread_num = 4
    # N = len(url_list) // thread_num
    # for i in range(thread_num-1):
    #     start = i*N
    #     end = (i+1) * N
    #     # print(start,end)
    #     print(url_list[start:end])
    # print(url_list[end:])