from django.contrib import admin
from django.urls import include, path

from map.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('map.urls')),
]

handler404 = page_not_found
