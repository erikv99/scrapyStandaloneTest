import scrapy

class bookScrapingPracticeItem(scrapy.Item):

    # define the fields for your item here
    title = scrapy.Field()
    price = scrapy.Field()