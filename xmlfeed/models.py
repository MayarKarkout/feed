# from django.db import models

# Create your models here.
import feedparser


class ProductFeed:
    def __init__(self, feed: feedparser.FeedParserDict):
        self.feed = feed
        self.nr_of_items = len(feed.entries)
        self.nr_of_in_stock_items = self.count_in_stock_items()

    def count_in_stock_items(self):
        nr_of_in_stock_items = 0
        for entry in self.feed.entries:
            if entry.g_availability == "in stock":
                nr_of_in_stock_items = nr_of_in_stock_items + 1
        return nr_of_in_stock_items

