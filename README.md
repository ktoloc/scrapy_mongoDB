# MongoDB & Scrapy 

Repository of scrapy spider that scrapes phone data from the website https://www.productindetail.com/ and stores the collected data in a MongoDB database. You can follow the accompanying tutorial to [Build a Web Scraper with MongoDB](https://www.mongodb.com/basics/how-to-use-mongodb-to-store-scraped-data).

## Create MongoDB 

Start by creating a free unified account for MongoDB and create cluster using these [instructions](https://www.mongodb.com/docs/guides/atlas/account/). 
To connect to your cluster you need to follow this connection using [Connect to your application](https://www.mongodb.com/docs/atlas/tutorial/connect-to-your-cluster/#connect-to-your-atlas-cluster).
There you can find your connection string and start the crawler.
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
scrapy crawl phones -s MONGODB_URI="mongodb+srv://<YOUR_CONNECTION_STRING>" -s MONGODB_DATABASE="phone_data"
```

## Documentation

- [MongoDB](https://www.mongodb.com)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [Scrappy](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [Web Scraping with Scrapy and MongoDB](https://realpython.com/web-scraping-with-scrapy-and-mongodb/#pymongo)

