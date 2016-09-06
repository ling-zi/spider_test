#coding:utf-8
from baike_spider import url_manager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer
class SpiderMain(object):
    #在每个模块中创建好了所需的class
    #需要在各个函数中初始化这些模块
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    #爬虫的调度程序
    def craw(self,root_url):
        count = 1
        #将入口url放进url管理器
        self.urls.add_new_url(root_url)
        #当url管理器中有待爬取的url时，就获取一个url
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw%d:%s'%(count,new_url ))
                #获取到待爬取的url之后，就启动下载器来下载这个页面
                #结果存储在html_cont中
                html_cont = self.downloader.download(new_url)
                #下载好了页面，就用解析器解析，就得到新的url列表
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                #补充新的url
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                #控制抓取url数为100
                if count == 100:
                    break
                count = count + 1
            #异常处理
            except Exception as f:
               print('crew failed: ', f)
        #输出
        self.outputer.output_html()

if __name__=="__main__":
    #设置入口url
    root_url = "http://baike.baidu.com/view/21087.htm"
    #创建一个spider
    obj_spider = SpiderMain()
    #调用Spider的craw方法来启动爬虫
    obj_spider.craw(root_url)