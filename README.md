# MongoDB & Scrapy 

Repository of scrapy spider that scrapes phone data from the website https://www.productindetail.com/ and stores the collected data in a MongoDB database. You can follow the accompanying tutorial to [Build a Web Scraper with MongoDB](https://www.mongodb.com/basics/how-to-use-mongodb-to-store-scraped-data).

## Get started

Clone the repository:

```
git clone https://github.com/ktoloc/scrapy_mongoDB.git
```

Install requirements file:
```
pip install -r requirements.txt
cd scrapy_mongoDB
```

Go to the `scrape` folder and start the crawler:
```
cd mongodb_crawler
scrapy crawl phone_data -s MONGODB_URI="mongodb+srv://test:test123@cluster0.mdmu8oy.mongodb.net/" -s MONGODB_DATABASE="phone_data"
```

Open your `scrapy` database with Compass, there should be 110 documents in the `scrapy_items` collection.