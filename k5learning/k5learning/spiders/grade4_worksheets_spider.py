import scrapy

from .grade1_worksheets_spider import Grade1WorksheetsSpider


class Grade4WorksheetsSpider(Grade1WorksheetsSpider):
    name = "grade4-worksheets"

    def start_requests(self):
        urls = [
            "https://www.k5learning.com/free-math-worksheets/fourth-grade-4",
            "https://www.k5learning.com/reading-comprehension-worksheets/fourth-grade-4",
            "https://www.k5learning.com/vocabulary-worksheets/fourth-grade-4",
            "https://www.k5learning.com/spelling-worksheets/fourth-grade-4",
            "https://www.k5learning.com/free-grammar-worksheets/fourth-grade-4",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
