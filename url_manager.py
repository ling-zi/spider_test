class UrlManager(object):
    def __init__(self):
        #两个列表
        self.new_urls = set()
        self.old_urls = set()
    #添加新的url
    def add_new_url(self, url):
        if url is None:
            return
        #如果这个url不在待爬取的url列表里面，也不在爬取过的url列表里面
        #就把它添加到待爬取里面
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    #添加新的批量url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in  urls:
            self.add_new_url(url)

    #判断管理器中是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls)!= 0
    #从url管理器中获取新的待爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
