import time
import scrapy

from src.items import Post


class CorpSpider(scrapy.Spider):
    name = 'corp_spider'
    allowed_domains = ['job.mynavi.jp']
    start_urls = ['https://job.mynavi.jp/']


    # レスポンスを受け取ると実行
    def parse(self, response):
        print('Success')
        # corp_list = response.css('.corp')
        # print('-'*50, len(corp_list))
        yield Post(
            url='localhost:8000',
            title='タイトル',
            data='サンプルデータ'
        )
        return
