from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from map.models import Institution

menu = [{'title': "main", 'url_name': 'main'},
        {'title': "about", 'url_name': 'about'},
        ]


def index(request):
    posts = Institution.objects.all()
    data = {'title': 'Main page',
            'menu': menu,
            'map': posts,
            }
    return render(request, 'map/index.html', context=data)


def about(request):
    data = {'title': 'about',
            'menu': menu,
            }
    return render(request, 'map/about.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound(f"page not found")
