from xml.sax import SAXParseException, SAXException

from django.shortcuts import render
import requests
from django.http import HttpResponse

import feedparser
from lxml import etree
from requests import exceptions

from xmlfeed.models import ProductFeed


def index(request):

    try:
        url = request.GET.get("url")
        if url is None:
            raise exceptions.MissingSchema

        request_url = requests.get(url)
        if request_url.status_code == 200:
            url = request.GET["url"]

            feed = feedparser.parse(url)
            # validate_xml_scheme(feed)

            if feed.bozo == 1:
                raise SAXException(msg="")

            if len(feed.entries) == 0:
                raise ValueError

            product_feed = ProductFeed(feed)
            nr_of_items = product_feed.nr_of_items
            nr_of_in_stock_items = product_feed.nr_of_in_stock_items

            labels_data = product_feed.get_custom_labels_data()

        return render(request, 'reader.html', {
            'feed': product_feed.feed,
            'nr_of_items': nr_of_items,
            'nr_of_in_stock_items': nr_of_in_stock_items,
            'labels_data': labels_data
        })

    except exceptions.MissingSchema as exception:
        return render(request, 'reader.html', {
            'error_msg': 'Please enter a valid URL.',
        })
    except ValueError as exception:
        return render(request, 'reader.html', {
            'error_msg': 'File formatting error (missing "item" tag).',
        })
    except SAXException as exception:
        return render(request, 'reader.html', {
            'error_msg': 'The feed data is not well-formed XML.',
        })


# def validate_xml_scheme(feed):
#     xmlschema_doc = etree.parse('simple.xml')
#     xmlschema = etree.XMLSchema(xmlschema_doc)
#
#     xml_doc = etree.parse('badsample.xml')
#     result = xmlschema.validate(xml_doc)
#
#     return result

