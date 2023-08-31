BOT_NAME = 'mongodb_crawler'

SPIDER_MODULES = ['mongodb_crawler.spiders']
NEWSPIDER_MODULE = 'mongodb_crawler.spiders'

ITEM_PIPELINES = {
  "mongodb_crawler.pipelines.MongoDBPipeline": 500
}

ROBOTSTXT_OBEY = True
