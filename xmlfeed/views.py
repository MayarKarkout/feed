from xml.sax import SAXException

import feedparser
import requests
from django.shortcuts import render
from requests import exceptions

from xmlfeed.models import ProductFeed


def index(request):
    data = None
    try:
        url = request.GET.get("url")
        if url is not None:

            # requests.get checks if url is valid and available
            request_url = requests.get(url)
            if request_url.status_code == 200:
                feed = feedparser.parse(url)

                if feed.bozo == 1:
                    raise SAXException(msg="")

                if len(feed.entries) == 0:
                    raise ValueError

                product_feed = ProductFeed(feed)
                nr_of_items = product_feed.nr_of_items
                nr_of_in_stock_items = product_feed.nr_of_in_stock_items
                custom_labels_data = product_feed.get_custom_labels_data()

                if not custom_labels_data:
                    custom_labels_data = ""

                data = {
                    'url': url,
                    'nr_of_items': nr_of_items,
                    'nr_of_in_stock_items': nr_of_in_stock_items,
                    'custom_labels_data': custom_labels_data
                }

    except exceptions.MissingSchema:
        data = {'error_msg': 'Please enter a valid URL.'}

    except ValueError:
        data = {'error_msg': 'File formatting error (missing "item" tag).'}

    except SAXException:
        data = {'error_msg': 'The feed data is not well-formed XML.'}

    finally:
        return render(request, 'reader.html', data)
