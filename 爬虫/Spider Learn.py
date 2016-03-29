#都是基于Python2.# 爬虫：一段自动抓取互联网信息的从程序
# 价值：互联网数据为我所用！

# 爬虫架构
# 爬虫调度端：URL管理器，网页下载器，网页解析器。

#URL管理器：管理待抓取URL集合和已抓取URL集合
#-防止重复抓取、防止循环抓取。
#实现方式
#1）内存：set（）
#2）关系数据库，Mysql
#3）缓存数据库，redis

#网页下载器：URL对应的网页下载到本地的工具
#urllib2 Python官方基础模块
#requests第三方包更强大

#urllib2使用方法
#方法1：
#import urllib2
#response = urllib2.urlopen（"http://www.baidu.com"）   直接请求
#print(response.getcode())   获取状态码，如果是200表示获取成功
#cont = =response.read()    读取内容
#方法2：添加data、http header
#import urllib2
#request = =urllib2.Request(url)    创建Requestd对象
#request.add_data('a','1')    添加数据
#request.add_header('User-Agent','Mozilla/5.0')    添加http的header
#response = urllib2.urlopen（request）   发送请求获取结果
#方法3：添加特殊情景的处理器
#import urllib2 cookielib
#cj = cookielib.CookieJar()    创建cookie
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))    创建1个opener
#urllib2.instanll_opener(opener)    给urllib2安装opener
#response = urllib2.urlopen（"http://www.baidu.com"）   使用带有cookie的urllib2访问网页


