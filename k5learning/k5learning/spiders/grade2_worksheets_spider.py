import scrapy

from .grade1_worksheets_spider import Grade1WorksheetsSpider


class Grade2WorksheetsSpider(Grade1WorksheetsSpider):
    name = "grade2-worksheets"

    def start_requests(self):
        urls = [
            "https://www.k5learning.com/free-math-worksheets/second-grade-2",
            "https://www.k5learning.com/reading-comprehension-worksheets/second-grade-2",
            "https://www.k5learning.com/vocabulary-worksheets/second-grade-2",
            "https://www.k5learning.com/spelling-worksheets/second-grade-2",
            "https://www.k5learning.com/free-grammar-worksheets/second-grade-2",
            "https://www.k5learning.com/science-worksheets/second-grade-2",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
