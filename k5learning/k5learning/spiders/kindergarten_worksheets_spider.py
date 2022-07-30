import scrapy
from urllib.parse import urljoin
from ..items import K5LearningItem


class WorksheetsSpider(scrapy.Spider):
    name = "kindergarten-worksheets"

    def start_requests(self):
        urls = [
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/science",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/vocabulary",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/reading-comprehension",
            "https://www.k5learning.com/free-preschool-kindergarten-worksheets/numbers-counting",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        topics = response.css(".blue-subtitle").xpath("./a/@href").getall()
        for href in topics:
            url = urljoin(response.url, href)
            yield scrapy.Request(url=url, callback=self.parse)

        topics = response.css("td").xpath("./a/@href").getall()
        for href in topics:
            url = urljoin(response.url, href)
            yield scrapy.Request(url=url, callback=self.parse)

        pdfs = response.css(".additional-links-url").xpath("./a/@href").getall()
        urls = [urljoin(response.url, href) for href in pdfs if href.endswith(".pdf")]
        if urls:
            yield K5LearningItem(file_urls=urls, name="kindergarten")
