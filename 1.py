import http.cookiejar
import urllib
from urllib import request
url = "http://www.baidu.com"

print('第一种方法')
response1=request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('第二种方法')
req=request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
response2=request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))

print('第三种方法')
cj=http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3=urllib.request.urlopen(url)
print(response3.getcode())
print(response3.read())
print(cj)

