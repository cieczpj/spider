import requests
data = {'name':'Joker','age':19}
response = requests.post('http://httpbin.org/post',data=data)
print(response.text)