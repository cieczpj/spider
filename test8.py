import queue
import requests
import re
from func_timeout import func_set_timeout
import func_timeout



def Spider_for_email():
    """
    Breadth traversal with baidu.com
    """
    parameters = {
        'wd':'留下邮箱'
    }
    headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    base_url = 'http://www.baidu.com/s?'
    response  = requests.get(url=base_url,params=parameters,headers=headers)
    # get response text
    Html = response.text
    regex = re.compile('.*?href="([a-zA-z]+://[^\s]*)"')
    URLS = regex.findall(Html)  # get urls using regex.
    for url in URLS:
        queue_url.put(url)  # input url to queue.

    # if not empty in queue,then get url and request.
    while not queue_url.empty():
        url = queue_url.get()
        try:
            reponse_for_url = requests.get(url=url,timeout=2)
            HTML = reponse_for_url.text
        except Exception: # get Error.
            print('Requtest Error.')
    
        try:
            spider_for_re(HTML)
        except func_timeout.exceptions.FunctionTimedOut:
            print('Re Failed')



@func_set_timeout(5)  # set timeout with this functin.
def spider_for_re(HTML):
    """
    Parameters:
        HTML: html code.
    return:
        None
    """
    regex_url = re.compile('.*?href="([a-zA-z]+://[^\s]*)"')
    regex_email = re.compile("[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?")
    urls = regex_url.findall(HTML) # get urls again
    emails = regex_email.findall(HTML) # get emial
    print(emails)
    for url in urls:
        queue_url.put(url) # input url in queue
    write_local(emails=emails)  # wirte emial in local
    

def write_local(emails):
    """
    Parameters:
        email: target email.
    return:
        None.
    """
    path = '/Users/huwang/Joker/Case/Spider/05网页解析_Re/emial.txt'
    open_file = open(path,mode='a') # The mode is 'a' must.

    for emial in emails:
        open_file.write(emial + '\n')
        open_file.flush()

    open_file.close()
        


if __name__ == "__main__":
    
    queue_url = queue.Queue()
    Spider_for_email()
