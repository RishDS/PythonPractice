import scrapy
from scrapy import Request


class GetbooksSpider(scrapy.Spider):
    name = "getbooks"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response): # Extracting book information from the main page
        books = response.xpath('//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]') 
        
        for book in books:  # Extracting title, price, star rating, and relative URL of each book
            title = book.xpath('article/h3/a/@title').extract_first().strip()
            price = book.xpath('article/div/p[@class="price_color"]/text()').extract_first().strip()
            star = book.xpath('article/p/@class').extract_first()[12:]
            rel_url = book.xpath('article/h3/a/@href').extract_first()
            abs_url = response.urljoin(rel_url)
    
            yield Request(abs_url, callback = self.parse_page, dont_filter = True, meta = {'Title': title, 'Price': price, 'Star Rating': star, 'URL': abs_url}) 
        
        # Moving to the next page
        rel_next_url = response.xpath('//li[@class = "next"]/a/@href').extract_first() #get url for the next page
        abs_next_url = response.urljoin(rel_next_url)
        
        yield Request(abs_next_url, callback =self.parse)
        
    def parse_page(self, response): # Extracting detailed information of each book from its individual page
        desc = response.xpath('//article/p/text()').extract_first().strip()
        availability = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()').extract()[1].strip()
        #Extra - not in assignment requirements
        genre = response.xpath('//*[@id="default"]/div/div/ul/li[3]/a/text()').extract()
        genre = genre[0] if genre and genre[0] != "Add a comment" else None # Handling cases where genre information is not available or meaningless
              
       #retrieve info from higher level page through meta (global variable)
        title = response.meta.get('Title')
        price = response.meta.get('Price')
        star = response.meta['Star Rating']     
        abs_url = response.meta['URL']
        
        yield{'Title': title, 'Price': price, 'Star Rating': star, 'Availability': availability,'Genre': genre, 'Description': desc, 'URL': abs_url}  # Yielding the final output with all extracted information