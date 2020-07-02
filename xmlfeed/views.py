from django.shortcuts import render
import requests
from django.http import HttpResponse

import feedparser
from requests import exceptions

from xmlfeed.models import ProductFeed


def index(request):

    try:
        url = request.GET.get("url")
        if url is None:
            raise exceptions.MissingSchema
        testerino = requests.get(url)

        if testerino.status_code is 200:
            url = request.GET["url"]

            feed = feedparser.parse(url)
            product_feed = ProductFeed(feed)
            nr_of_items = product_feed.nr_of_items
            nr_of_in_stock_items = product_feed.nr_of_in_stock_items

        return render(request, 'reader.html', {
            'feed': product_feed.feed,
            'nr_of_items': nr_of_items,
            'nr_of_in_stock_items': nr_of_in_stock_items,
        })

    except exceptions.MissingSchema as exception:
        return render(request, 'reader.html', {
            'error_msg': 'Please enter a valid URL.',
        })