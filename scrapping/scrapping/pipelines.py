# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from audio_src.apps.categories.models import Category

class ScrappingPipeline:
    def process_item(self, item, spider):
        print(item)
        cate = Category(title="test-category", description="description", status="publish")
        cate.save()
        print(cate.id)
        return item
