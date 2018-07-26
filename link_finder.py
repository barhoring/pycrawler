from html.parser import HTMLParser
# from urllib import parser

class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()

    def error(self, msg):
        print('pycrawler error')

    def handle_starttag(self, tag, attr):
        print(tag)

finder = LinkFinder()
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
#input('wait..')
