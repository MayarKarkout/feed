import feedparser
from django.test import TestCase


from xmlfeed.models import ProductFeed

rawdata = """<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">
              <channel><item>
              <g:id>100130</g:id>
              <link><></link>
              <g:price>230.01 PLN</g:price>
              <title>Ręcznik papierowy mała rolka 11 szt</title>
              <g:description><![CDATA[Ręcznik papierowy mała rolka 11 szt]]></g:description>
              <g:brand>Rajapack</g:brand>
              <g:mpn>100130</g:mpn>
              <g:condition>nowy</g:condition>
              <g:multipack></g:multipack>
              <g:custom_label_0></g:custom_label_0>
              <g:custom_label_1></g:custom_label_1>
              <g:custom_label_2></g:custom_label_2>
              <g:custom_label_3>Higiena i bezpieczeństwo</g:custom_label_3>
              </item>"""


class FeedTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.product_feed = ProductFeed(feed=feedparser.parse(rawdata))

    # Example tests

    def test_nr_of_items_is_one_given_one_item(self):
        nr_of_items = self.product_feed.nr_of_items
        self.assertIs(nr_of_items, 1)

    def test_nr_of_in_stock_items_is_empty_given_no_in_stock_tag(self):
        nr_of_in_stock_items = self.product_feed.nr_of_in_stock_items
        self.assertIs(nr_of_in_stock_items, '')
