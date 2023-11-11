from django.contrib import admin

from .models import TypeStreet, ObjectOnMap


class TypeStreetAdmin(admin.ModelAdmin):
    model = TypeStreet
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('id', 'title')
    list_filter = ('title',)


class ObjectOnMapAdmin(admin.ModelAdmin):
    model = ObjectOnMap
    list_display = ('id', 'name_object', 'type_object', 'x_coord', 'y_coord')
    list_display_links = ('name_object',)
    search_fields = ('id', 'name_object', 'type_object',)
    list_filter = ('type_object',)


admin.site.register(TypeStreet, TypeStreetAdmin)
admin.site.register(ObjectOnMap, ObjectOnMapAdmin)
