import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
#a = requests.get('https://book.douban.com/tag/%E6%95%A3%E6%96%87',headers=headers)
for j in range(0,980,20):
    if j == 0:
        a = requests.get('https://book.douban.com/tag/%E6%95%A3%E6%96%87',headers=headers)
    else:
        a = requests.get('https://book.douban.com/tag/%E6%95%A3%E6%96%87?start={}&type=T'.format(j),headers=headers)
    a.encoding = 'utf8'
    HTML = a.text
    soup = BeautifulSoup(HTML,'lxml')
    res_img = soup.select('#subject_list .subject-list li div a img')
    res_a = soup.select('#subject_list .subject-list li div a')
    res_title = soup.select('#subject_list .subject-list li .info .pub')
    for img in res_img:
        print(img.attrs['src'])
    print('---------------')
    for a in res_a:
        print(a.attrs['href'])
    print('---------------')
    for title in res_title:
        print(title.text.strip().split(' / ')[0])
