import json

from random import choices
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from map.models import ObjectOnMap


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


def get_objects_on_map(request):
    data = ""
    for _obj in choices(ObjectOnMap.objects.all().values(), k=5):  # hotfix TODO replace by real data
        data += f'<h5>{_obj['name_object']}</h4>' \
                  f"<h6>{dict(ObjectOnMap.TYPE_OBJECT_CHOICES)[_obj['type_object']]}</h6><br>"
    return HttpResponse(
        json.dumps({
            'data': data,
        })
    )


def page_not_found(request, exception):
    msg = """<title>404</title>
             <style>* { font-family: consolas, monospace; }</style>
             <h1><b>404 PAGE NOT FOUND</b><h1>"""
    return HttpResponseNotFound(msg)
