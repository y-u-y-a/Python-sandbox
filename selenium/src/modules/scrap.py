import time
import requests
from bs4 import BeautifulSoup


class ScrapHTML(object):

    def __init__(self, url):
        self.html = self.get_html(url)
        return

    def get_html(self, url):
        time.sleep(1)
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        html = BeautifulSoup(res.text, 'html.parser')
        return html


    def get_h1(self) -> dict:
        h1_list = self.html.select('h1')
        el = h1_list[0]
        return {
            'el': el,
            'text': el.getText()
        }
