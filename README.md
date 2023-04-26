<div align="center">
    <img src="https://www.k5learning.com/sites/default/files/k5logo.png" alt="logo" width="128">
</div>

# scrapy-k5learning

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

A scrapy app to crawl worksheets from [k5learning.com][1]

## Getting Started

    python -m venv .venv
    .\.venv\Scripts\activate
    python -m pip install -U pip
    pip install -r requirements.txt
    cd k5learning
    scrapy crawl kindergarten-worksheets
    scrapy crawl grade1-worksheets
    scrapy crawl grade2-worksheets
    scrapy crawl grade3-worksheets
    scrapy crawl grade4-worksheets
    scrapy crawl grade5-worksheets
    scrapy crawl grade6-worksheets

> Use `pip install -r requirements-dev.txt` for development.

## Credits

- [k5learning.com][1]

[1]: https://www.k5learning.com
