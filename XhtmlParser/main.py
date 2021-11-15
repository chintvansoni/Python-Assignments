from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if "Current IP Address" in data:
            print(data.split(":")[1])


myparser = MyHTMLParser()

with urllib.request.urlopen('http://checkip.dyndns.org') as response:
    html = str(response.read())

myparser.feed(html)
