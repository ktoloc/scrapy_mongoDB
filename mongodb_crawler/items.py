from scrapy.item import Item, Field


class PhonesItem(Item):

    """This class defines data we need to scrape from website to DB """

    product_name = Field()
    brand = Field()
    description = Field()
    storage = Field()
    battery = Field()
    operating_system = Field()
    display_technology = Field()
    image_url = Field()
