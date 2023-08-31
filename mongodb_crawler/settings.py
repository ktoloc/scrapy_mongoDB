BOT_NAME = 'mongodb_crawler'

SPIDER_MODULES = ['mongodb_crawler.spiders']
NEWSPIDER_MODULE = 'mongodb_crawler.spiders'

ITEM_PIPELINES = {
  "mongodb_crawler.pipelines.MongoDBPipeline": 500
}
MONGO_URI = 'mongodb+srv://cluster0.mdmu8oy.mongodb.net/" --apiVersion 1 --username test'
MONGO_DATABASE = 'phone_data'

ROBOTSTXT_OBEY = True
