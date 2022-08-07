import scrapy

from .grade1_worksheets_spider import Grade1WorksheetsSpider


class Grade5WorksheetsSpider(Grade1WorksheetsSpider):
    name = "grade5-worksheets"

    def start_requests(self):
        urls = [
            "https://www.k5learning.com/free-math-worksheets/fifth-grade-5",
            "https://www.k5learning.com/reading-comprehension-worksheets/fifth-grade-5",
            "https://www.k5learning.com/vocabulary-worksheets/fifth-grade-5",
            "https://www.k5learning.com/spelling-worksheets/fifth-grade-5",
            "https://www.k5learning.com/free-grammar-worksheets/fifth-grade-5",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
