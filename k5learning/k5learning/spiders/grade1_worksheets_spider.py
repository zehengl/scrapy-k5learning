from urllib.parse import urljoin

import scrapy

from .kindergarten_worksheets_spider import KindergartenWorksheetsSpider


class Grade1WorksheetsSpider(KindergartenWorksheetsSpider):
    name = "grade1-worksheets"

    def start_requests(self):
        urls = [
            "https://www.k5learning.com/free-math-worksheets/first-grade-1",
            "https://www.k5learning.com/reading-comprehension-worksheets/first-grade-1",
            "https://www.k5learning.com/vocabulary-worksheets/first-grade-1",
            "https://www.k5learning.com/spelling-worksheets/first-grade-1",
            "https://www.k5learning.com/free-grammar-worksheets/first-grade-1",
            "https://www.k5learning.com/science-worksheets/first-grade-1",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def get_topics(self, response):
        topics = super().get_topics(response)

        topics.extend(
            [
                urljoin(response.url, href)
                for href in response.css(".two-columns").xpath("./p/a/@href").getall()
            ]
        )

        return topics
