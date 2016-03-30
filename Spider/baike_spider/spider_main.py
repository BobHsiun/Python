from Spider.baike_spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count=1
        self.urls.add_new_url(root_url)
        print("开始URL：",root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('第%d次抓取，抓取地址: %s' %(count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 100:
                    break
                count+=1
            except Exception as e:
                print(e)
                print ('爬取失败')
        self.outputer.output_html()


if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_speder = SpiderMain()
    obj_speder.craw(root_url)
