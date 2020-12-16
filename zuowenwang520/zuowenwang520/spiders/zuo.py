import scrapy


class ZuoSpider(scrapy.Spider):
    name = 'zuo'
    # allowed_domains = ['zuowen.com']
    start_urls = ['https://www.520z-2.com/']

    def parse(self, response):
        links = response.xpath('//div[@class="nav"]/ul/li/a/@href').getall()
        for link in links:
            yield response.follow(url=link, callback=self.parse_type_list)
            
    def parse_type_list(self, response):
        # print(response.url)
        detail_links = response.xpath('//div[@class="pageleft fl"]//ul/li//h3/a/@href').getall()
        for det in detail_links:
            yield response.follow(url=det, callback=self.parse_detail)
        
        next_pages = response.xpath('//div[@class="pageurl"]/a/@href').getall()
        for one_next_page in next_pages:
            yield response.follow(url=one_next_page, callback=self.parse_type_list)
            
    def parse_detail(self, response):
        title = response.xpath('//div[@class="viewtitle"]/h1/text()').get()
        print(title)
        release_time = response.xpath('//div[@class="viewinfo pos-r clearfix"]/span/i[1]/text()').get()
        print(release_time)
