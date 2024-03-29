from urllib.parse import urljoin

import scrapy

from ..items import K5LearningItem


class KindergartenWorksheetsSpider(scrapy.Spider):
    name = "kindergarten-worksheets"

    def start_requests(self):
        urls = [
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/letters-alphabet",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/phonics",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/vocabulary",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/reading-comprehension",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/shapes",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/writing",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/colors",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/numbers-counting",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/simple-math",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/science",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/social-emotional",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/activities-concepts",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def get_topics(self, response):
        topics = []

        topics.extend(
            [
                urljoin(response.url, href)
                for href in response.css(".blue-subtitle").xpath("./a/@href").getall()
            ]
        )

        topics.extend(
            [
                urljoin(response.url, href)
                for href in response.css("td").xpath("./a/@href").getall()
            ]
        )

        return topics

    def parse(self, response):
        yield from [
            scrapy.Request(url=url, callback=self.parse)
            for url in self.get_topics(response)
        ]

        pdfs = response.css(".additional-links-url").xpath("./a/@href").getall()
        urls = [urljoin(response.url, href) for href in pdfs if href.endswith(".pdf")]
        if urls:
            yield K5LearningItem(file_urls=urls, name=self.name.split("-")[0])
