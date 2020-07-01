from django.shortcuts import render

from django.http import HttpResponse

import feedparser


def index(request):
    if request.GET.get("url"):

        url = request.GET["url"]  # Getting URL

        feed = feedparser.parse(url)  # Parsing XML data

    else:
        feed = None

    return render(request, 'reader.html', {

        'feed': feed,

    })
