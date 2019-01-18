import requests
from bs4 import BeautifulSoup
import threading
import urllib.parse
import pymongo

def get_music_name():

    response = requests.get("https://www.kugou.com/yy/rank/home/1-8888.html?from=rank")
    HTML = response.text
    soup = BeautifulSoup(HTML,'lxml')
    LIs = soup.select('#rankWrap .pc_temp_songlist ul li')
    NAMES = [li.attrs['title'].split(' - ')[-1] for li in LIs]
    get_music_hash(NAMES)

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

    write_local(NAMES,ADDRS)

def write_local(NAMES,ADDRS):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["wedata"]
    mycol = mydb["kugou"]
    mylist = []
    for name,addr in zip(NAMES,ADDRS):
        mylist.append({name:addr})
    mycol.insert_many(mylist)
    myclient.close() #!!!!!!!!!!!



if __name__ == "__main__":
    get_music_name()