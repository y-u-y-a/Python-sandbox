# PyPIライブラリ
import requests
from bs4 import BeautifulSoup


class Scrap(object):

    # インスタンス生成時に実行(return不要)
    def __init__(self, url: str):
        # インスタンス変数
        self.html = self.getHTML(url)

    # __init__で利用
    def getHTML(self, url: str):
        res = requests.get(url)
        res.encoding = res.apparent_encoding

        html = BeautifulSoup(res.text, "html.parser")
        return html


    def getElementById(self, id_name: str):

        element = self.html.select("#" + id_name)
        return element


    def getElementsByClass(self, class_name: str):

        elements = self.html.select("." + class_name)
        return elements


    def getTextListByClass(self, class_name: str) -> list:

        text_list = []
        elements = self.getElementsByClass(class_name)

        for el in elements:
            text_list.append(el.text)

        return text_list
