# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem


class ValidationPipeline(object):
    '''
    Itemを検証するPipeline
    '''

    def process_item(self, item, spider):
        if not item['title']:  # titleフィールドが取得できていない場合は破棄
            raise DropItem('Missing title')  # 破棄する理由を表すメッセージ
        return item
