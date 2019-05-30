import scrapy
import urllib.parse as urlparse

class ReviewSpider(scrapy.Spider):
    name = 'review_spider'
    def start_requests(self):
        urls = [
            'https://www.imdb.com/title/tt4154796/reviews?ref_=tt_urv',
            'https://www.imdb.com/title/tt4154796/reviews/_ajax?ref_=undefined&paginationKey=46nfomhqi3gzbjjjx4gf7uh577btckim3ucvflquh4exniquzjshjuqy3tclm5dglxwndc7fi7zyo',
            'https://www.imdb.com/title/tt4154796/reviews/_ajax?ref_=undefined&paginationKey=hbie42yiji5bvkp2gfozn3hrxtyge4jowc5m2yoev5xhgk2v4a7zhimn7h5zkr34stuhqnqbyprdi',
            'https://www.imdb.com/title/tt4154796/reviews/_ajax?ref_=undefined&paginationKey=a62drqxeah4ym27z6rtymjyck53zrcnbgfdfhydsav4eo5unvbdvm3pmf4bw3koshhe6aucu7s42e',
            'https://www.imdb.com/title/tt4154796/reviews/_ajax?ref_=undefined&paginationKey=n7xuwpm666gur3l2mdeqeipgfeu4igje2ddbe4j3j6k5wwkhannlqydycubrkyylejwxjqkimbqno',
            'https://www.imdb.com/title/tt4154796/reviews/_ajax?ref_=undefined&paginationKey=az3ru5k5fum4io3vcr3hikw2jlprbekdc4nzeghgsr3wx5dbgrqd7ic7gy2chbnujf6akdv4vez6q',
            'https://www.imdb.com/title/tt4154796/reviews/_ajax?ref_=undefined&paginationKey=tshcvtkrl7jr46yrcte6ov5bozo6oxjhs266rm3znz7gzrugvahpghqxhcvn5fkroqtstevkya53y',
        ]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
            
            
    def parse(self, response):
        containers = response.css("div.review-container")
        
        for container in containers:
            review_date = container.css("span.review-date::text").get()
            review_title = container.css("a::text").get()
            review = container.xpath('//div[@class = "content"]//div//text()').extract_first()
            temp_cont = container.css("div.display-name-date")
            reviewer_name = temp_cont.css("a::text").get()
            tmp_cont = container.css("span.rating-other-user-rating")
            tmp_cont = tmp_cont.css("span")[1]
            rating = tmp_cont.css("span::text").get()
            
            yield{
                "name":reviewer_name,
                "date":review_date,
                "title":review_title,
                "review":review,
                "rating":rating,
            }
            
      
