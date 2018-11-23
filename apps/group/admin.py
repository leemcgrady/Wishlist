from django.contrib import admin
from django.core.cache import cache
from group.models import Group


# class Group(admin.ModelAdmin):
#
#     list_display = ('name', 'detail')
#     search_fields = ('name', )
#     list_per_page = 20


admin.site.register(Group)
