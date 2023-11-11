from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    data = {
        'title': 'Home',
        'GOOGLE_MAP_API_KEY': settings.GOOGLE_MAP_API_KEY,
    }
    return render(request, 'map/index.html', context=data)


def about(request):
    data = {
        'title': 'About',
    }
    return render(request, 'map/about.html', data)


def page_not_found(request, exception):
    msg = """<title>404</title>
             <style>* { font-family: consolas, monospace; }</style>
             <h1><b>404 PAGE NOT FOUND</b><h1>"""
    return HttpResponseNotFound(msg)
