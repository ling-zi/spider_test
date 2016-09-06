from urllib import request
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        #把内容存在response
        response = request.urlopen(url)
        if response.getcode() != 200:
            return  None
        return  response.read()