import scrapy

from .grade1_worksheets_spider import Grade1WorksheetsSpider


class Grade6WorksheetsSpider(Grade1WorksheetsSpider):
    name = "grade6-worksheets"

    def start_requests(self):
        urls = [
            "https://www.k5learning.com/free-math-worksheets/sixth-grade-6",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
