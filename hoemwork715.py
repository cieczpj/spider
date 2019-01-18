import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import time

def spider_for_kugou():
    """
    This function implementate "get KuGouTop500",and using us4.
    Note:
        Need split music name from original json data.
    returns:
        music_names: It's a list. 
    """
    
    muisc_names = []
    for index in range(500//22):
        response_for_TOP500 = requests.get('https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(index),headers=headers)
        response_for_TOP500.encoding = 'utf-8'
        HTML = response_for_TOP500.text
        soup = BeautifulSoup(HTML,'lxml')
        LIs = soup.find_all('li',{'class':' '})
        for li in LIs:
                muisc_name = li.attrs['title'].split(' - ')[-1].strip().split(' ')[0] # get rigth music name.
                muisc_names.append(muisc_name)
    print('Okay, Get music names')
    return muisc_names



def handle_kugou_API(music_names):
    """
    Parameters:
        muisc_names: The list of cache music name.
    Note:
        1.Must url encoding at music name. very important.
        2.First step:hash value of music name.
        3.Seocne step: using hash value to request kugou,then get music path.
    return:
        music_paths: The list of cache music path.
        
    """
    music_paths = []
    urlencode_names = [urlencode({'keyword':name}) for name in music_names ]
    for urlencode_name in urlencode_names:
        
        # get hash value, about 4 lines
        get_hash_url = 'http://mobilecdn.kugou.com/api/v3/search/song?format=json&{}&page=1&pagesize=20&showtype=1%20---------------------%20%E4%BD%9C%E8%80%85%EF%BC%9A%E5%85%AC%E4%BC%97%E5%8F%B7%E7%81%AB%E7%82%8E%E4%B8%80%E7%AC%91%E5%80%BE%E5%9F%8E%20%E6%9D%A5%E6%BA%90%EF%BC%9ACSDN%20%E5%8E%9F%E6%96%87%EF%BC%9Ahttps://blog.csdn.net/qq_14955245/article/details/79467618%20%E7%89%88%E6%9D%83%E5%A3%B0%E6%98%8E%EF%BC%9A%E6%9C%AC%E6%96%87%E4%B8%BA%E5%8D%9A%E4%B8%BB%E5%8E%9F%E5%88%9B%E6%96%87%E7%AB%A0%EF%BC%8C%E8%BD%AC%E8%BD%BD%E8%AF%B7%E9%99%84%E4%B8%8A%E5%8D%9A%E6%96%87%E9%93%BE%E6%8E%A5%EF%BC%81'.format(urlencode_name)
        response_for_hash_url = requests.get(get_hash_url,headers=headers)
        hash_json = response_for_hash_url.json()
        music_hash = hash_json.get('data').get('info')[0].get('hash')
        
        # get music path about 5 lines.
        get_music_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}'.format(music_hash)
        response_for_music_url = requests.get(get_music_url,headers=headers)
        music_url_path = response_for_music_url.json()
        music_path = music_url_path.get('data').get('play_url')
        music_paths.append(music_path)
        print('music path is: ',music_path)
    return music_paths

def write_local(path,music_paths):
    """
    There is nothing to say about this.
    """
    open_path = open(path,mode='w')
    for music_path in music_paths:
        open_path.write(music_path)
        open_path.flush()

    open_path.close()
    print('KuGou Spider Over!')


if __name__ == "__main__":
    headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    # write local
    path = '/Users/huwang/Joker/Case/Spider/06网页解析_Bs4/music.txt'
    muisc_names = spider_for_kugou()
    music_paths = handle_kugou_API(muisc_names)
    write_local(path=path,music_paths=music_paths)





