import scrapy
from ..items import PhonesItem


class PhonesSpider(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['productindetail.com']
    start_urls = ['https://www.productindetail.com/phones']

    def parse(self, response):

        """Select all phone containers"""

        all_phones = response.xpath("//div[@class='card-body text-center d-flex flex-column']")

        for phone in all_phones:
            item = PhonesItem()

            """Extract product name and image link."""

            item['product_name'] = phone.xpath('.//p/a/strong/text()').get()
            item['image_url'] = phone.xpath('.//a[@class="text-decoration-none"]/img/@src').get()

            product_url = phone.xpath('.//a[@class="text-decoration-none"]/@href').get()
            yield response.follow(product_url, callback=self.parse_product, meta={'item': item})

        """Find and follow the next page link"""

        next_page = response.xpath('//li[@class="page-item"]/a[@aria-label="Next"]/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_product(self, response):
        product_item = response.meta['item']

        """Here is extraction of each phone items details"""

        product_item['brand'] = response.xpath('/html/body/div[3]/div[1]/nav/ol/li[2]/a/small/text()').get()
        product_item['description'] = response.xpath('//*[@id="recenze"]/div/div/div/p/text()').get()
        product_item['storage'] = response.xpath(
            '//*[@id="memory"]/div[1]/table/tbody/tr[2]/td[1]/small/text()').get()
        product_item['battery'] = response.xpath(
            '//*[@id="battery-and-charging"]/div[1]/table/tbody/tr[1]/td[1]/small/text()').get()
        product_item['operating_system'] = response.xpath(
            '//*[@id="cellular"]/div[1]/table/tbody/tr[3]/td[1]/small/text()').get()
        product_item['display_technology'] = response.xpath(
            '//*[@id="display"]/div[1]/table/tbody/tr[2]/td[1]/small/text()').get()

        yield product_item
