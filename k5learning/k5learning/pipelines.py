# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os

from scrapy.pipelines.files import FilesPipeline


class K5LearningPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return os.path.join(item["name"], os.path.basename(request.url))
