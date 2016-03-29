import urllib2
url = "http://www.baidu.com"
print("第一种方法")

response1 = urllib.urlopen(url)
#直接请求
print(response1.getcode())
#获取状态码，如果是200表示获取成功