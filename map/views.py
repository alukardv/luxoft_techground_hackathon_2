from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from map.models import Institution


def index(request):
    posts = Institution.objects.all()
    data = {
        'title': 'Home',
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
