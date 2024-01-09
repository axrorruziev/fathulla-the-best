from django.shortcuts import render
from newsapi import NewsApiClient


# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key='c77dfbc6c74b47e18b81ed5f9d3ffc54')
    top = newsapi.get_top_headlines(sources='tech-crunch')

    l = top['articles']
    dsc = []
    nws = []
    im = []

    for i in range(len(l)):
        f = l[i]
        nws.append(f['title'])
        dsc.append(f['description'])
        im.append(f['urlToImage'])
        mylist = zip(nws, dsc, im)

        return render(request, 'index.html', context={'mylist': mylist})
