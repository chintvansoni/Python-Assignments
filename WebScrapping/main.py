import ssl
import urllib.request
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    colorDict = {}
    inTable = False
    inRow = False
    aTagFound = False
    colorName = None

    def handle_starttag(self, tag, attrs):
        if tag == "table" and len(attrs) == 1 and attrs[0] == ('class', 'color-list'):
            self.inTable = True

        elif self.inTable and tag == "tr":
            self.inRow = True

        elif self.inTable and tag == 'a':
            self.aTagFound = True

    def handle_endtag(self, tag):
        if self.inTable and tag == "tbody":
            self.inTable = False

        elif self.inTable and tag == "tr":
            self.inRow = False

        elif self.inTable and tag == "a":
            self.aTagFound = False

    def handle_data(self, data):
        if self.inTable and self.aTagFound:

            if self.colorName is None:
                self.colorName = data

            elif self.colorName is not None:
                self.colorDict.update({self.colorName: data})
                self.colorName = None


myparser = MyHTMLParser()

ssl._create_default_https_context = ssl._create_unverified_context

with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
    html = str(response.read())

myparser.feed(html)

for colorName, hexValue in myparser.colorDict.items():
    print(colorName, hexValue)

print("There are total of", len(myparser.colorDict), "colors.")
