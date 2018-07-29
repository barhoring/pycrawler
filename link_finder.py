from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, msg):
        print('pycrawler error')

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attr, val) in attrs:
                if attr == 'href':
                    url = parse.urljoin(self.base_url, val)
                    print(url)
                    self.links.add(url)

    def page_links(self):
        return self.links

finder = LinkFinder('http://some/xxx/', '/')
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1><a href="jj">Parse me!</a></h1><a href="/fis.js" >ffishfish</a></body></html>')
links = finder.page_links()
print(links)
#input('wait..')
