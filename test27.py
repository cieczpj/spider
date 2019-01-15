import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
# 获得hash json
a = requests.get('https://www.kugou.com/yy/rank/home/1-8888.html?from=rank',headers=headers)
a.encoding = 'utf8'
HTML = a.text
#print(HTML)
soup = BeautifulSoup(HTML,'lxml')
#print(soup.find_all('a'))
music = soup.select('.pc_temp_songlist ul li .pc_temp_songname')
for img in music: 
    res_music = img.attrs['href']
    #print(res_music)
    songname = img.attrs['title']
    #print(songname)
    print(res_music + songname)

    
    
    
#http://mobilecdn.kugou.com/api/v3/search/song?format=json&keyword=url编码的歌名&page=1&pagesize=20&showtype=1%20---------------------%20%E4%BD%9C%E8%80%85%EF%BC%9A%E5%85%AC%E4%BC%97%E5%8F%B7%E7%81%AB%E7%82%8E%E4%B8%80%E7%AC%91%E5%80%BE%E5%9F%8E%20%E6%9D%A5%E6%BA%90%EF%BC%9ACSDN%20%E5%8E%9F%E6%96%87%EF%BC%9Ahttps://blog.csdn.net/qq_14955245/article/details/79467618%20%E7%89%88%E6%9D%83%E5%A3%B0%E6%98%8E%EF%BC%9A%E6%9C%AC%E6%96%87%E4%B8%BA%E5%8D%9A%E4%B8%BB%E5%8E%9F%E5%88%9B%E6%96%87%E7%AB%A0%EF%BC%8C%E8%BD%AC%E8%BD%BD%E8%AF%B7%E9%99%84%E4%B8%8A%E5%8D%9A%E6%96%87%E9%93%BE%E6%8E%A5%EF%BC%81