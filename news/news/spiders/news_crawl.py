from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news.items import Headline


class NewsCrawlSpider(CrawlSpider):
    name = 'news_crawl'  # Spiderの名前
    allowed_domains = ['news.yahoo.co.jp', 'news.goo.ne.jp']  # クロール対象とするドメインのリスト
    start_urls = ['http://news.yahoo.co.jp/', 'http://news.goo.ne.jp/']  # クロールを開始するURLのリスト
    rules = [
        Rule(LinkExtractor(allow=r'/pickup/\d+$'), callback='parse_yahoo'),
        Rule(LinkExtractor(allow=r'/topstories/\w+', deny='/topstories/today/'), callback='parse_goo'),
    ]

    def parse_yahoo(self, response):
        '''
        Yahoo!ニューストピックスページからタイトルと要約を抜き出す
        '''

        item = Headline()
        item['title'] = response.css('#uamods-pickup > div > a > p::text').extract_first()
        item['summary'] = response.css('#uamods-pickup > div > p')[-1].xpath('string()').extract_first()
        yield item

    def parse_goo(self, response):
        '''
        gooニューストピックスページからタイトルと要約を抜き出す
        '''

        item = Headline()
        item['title'] = response.css('.heading-title-topics::text').extract_first()
        item['summary'] = response.css('.topics-text').xpath('string()').extract_first()
        yield item
