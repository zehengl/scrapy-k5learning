import scrapy


class WorksheetsSpider(scrapy.Spider):
    name = "worksheets"

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
        pass
