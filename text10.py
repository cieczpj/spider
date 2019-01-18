import requests
from lxml import etree




def Spider_for_OnePiece():
    """
    This function implementation to getting image url,and download image to local.
    Note:
        due the One Piece website too old,so the website coding is gbk.
            Using ".encoding='gbk'"
    """
    for index in range(1,28):
        img_url = 'http://op.hanhande.net/shtml/op_wz/list_2602_{}.shtml'.format(str(index))
        response_for_Onepiece = requests.get(img_url,headers=headers,timeout=3)
        response_for_Onepiece.encoding = 'gbk'
        HTML = response_for_Onepiece.text
        tree = etree.HTML(HTML)
        # Using xpath to get image src,about 1 lines.
        As = tree.xpath('//div[@id="main"]/div[contains(@class,"content")]/div[contains(@class,"show")]/ul[contains(@class,"spic")]/li/a/img/@src')
        for url in As:
            image_name = url.split('/')[-1] # just like before, use split to get image name.
            download_picture(url=url,name=image_name)
        
def download_picture(url,name):
    """
    Parameters:
        url: download image url
        name: image  name.
    """
    response_for_image = requests.get(url=url,headers=headers,timeout=2)
    path = '/Users/huwang/Joker/Case/Spider/07网页解析_xpath/'
    image_path = path + name

    # start write local about 3 lines.
    with open(image_path,'wb') as f:
        f.write(response_for_image.content)
        f.flush()