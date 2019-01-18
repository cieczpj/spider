from lxml import etree
import requests
import urllib.parse
import pymongo
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
for j in range(108,1,-1):

    
    reponse = requests.get('http://www.hetaodaxue.com/xyxw/{}.htm'.format(j),headers=headers)
    reponse.encoding="utf8"
    tree = etree.HTML(reponse.text)
    res = tree.xpath('/html/body/div/div[3]/div[1]/div[2]/div/ul/li/a')
    mylist = []
    for a in res:
        href_ = a.xpath('./@href')[0]
        text_ = a.xpath('./text()')[0]
        print(href_,text_)
        if text_ != None:
            mylist.append({text_:href_})
        else:
            break



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["webook"]
mycol = mydb["hetao"]
mycol.insert_many(mylist)
myclient.close() #!!!!!!!!!!!


