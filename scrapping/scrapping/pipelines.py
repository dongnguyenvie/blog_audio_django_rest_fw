# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from audio_src.apps.menus.models import Menu

class ScrappingPipeline:
    def process_item(self, item, spider):
        # print(item)
        # menu = Menu(name="test-menu", type=2)
        # print("=====>> pre ==<<<<<")
        # menu.save()
        # print(menu.name)
        return item
