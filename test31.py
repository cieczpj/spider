from lxml import etree
import requests
import urllib.parse
import pymongo
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
for j in range(5):
    reponse = requests.get('http://v.7192.com/movie_0_0_0_0_{}'.format(j),headers=headers)
    reponse.encoding="gbk"
    tree = etree.HTML(reponse.text)
    res = tree.xpath('//div[@class="result_right_list"]/ul/li/div/a')
    #print(res)
    mylist = []
    for a in res:
        href1_ = a.xpath('./@href')[0]
        href_ = ('http://v.7192.com'+href1_)
        title_ = a.xpath('./@title')[0]
        src_ = a.xpath('./img/@data-original')[0]
        print(src_)
        print(href_,title_)
        #text_=href_+title_+src_
        reponse1 = requests.get('http://v.7192.com'+href1_,headers=headers)
        reponse1.encoding="gbk"
        tree1 = etree.HTML(reponse1.text)
        res2 = tree1.xpath('//div[@class="show_information"]/table[@id="mv_play_list"]/tr/th[@width="180px"]/a')
        #res2 = tree1.xpath('//div[@class="result_right_list"]/ul/li/div/a')
        #mylist = []
        for b in res2:
            href2= b.xpath('./@rel')[0]
            print(href2)
            mylist.append({"src_":src_,"href_":href_,"title_":title_,"href2":href2})

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["wemovie"]
mycol = mydb["movie"]
mycol.insert_many(mylist)
myclient.close() #!!!!!!!!!!!


    
    

