from openpyxl import Workbook
from itemadapter import ItemAdapter
from pymongo import MongoClient


class EbookScraperPipeline:
    def open_spider(self, spider):
        pass
        # self.client = MongoClient(
        #     host="mongodb+srv://kieuvandoanit:TCxU3hpeepIfgDEe@singapore-cluster.i1gcg.mongodb.net/?retryWrites=true&w=majority&appName=Singapore-Cluster",
        #     connect=False,
        # )
        # self.collection = self.client.get_database("ebook").get_collection('travel')

    def process_item(self, item, spider):
        # self.collection.insert_one(
        #     ItemAdapter(item).asdict()
        # )
        pass
        # return item

    def close_spider(self, spider):
        # self.client.close()
        pass