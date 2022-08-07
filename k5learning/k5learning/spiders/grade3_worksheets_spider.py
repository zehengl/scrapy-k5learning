import scrapy

from .grade1_worksheets_spider import Grade1WorksheetsSpider


class Grade3WorksheetsSpider(Grade1WorksheetsSpider):
    name = "grade3-worksheets"

    def start_requests(self):
        urls = [
            "https://www.k5learning.com/free-math-worksheets/third-grade-3",
            "https://www.k5learning.com/reading-comprehension-worksheets/third-grade-3",
            "https://www.k5learning.com/vocabulary-worksheets/third-grade-3",
            "https://www.k5learning.com/spelling-worksheets/third-grade-3",
            "https://www.k5learning.com/free-grammar-worksheets/third-grade-3",
            "https://www.k5learning.com/science-worksheets/third-grade-3",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
