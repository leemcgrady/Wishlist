from django.contrib import admin
from django.core.cache import cache
from group.models import Group


class GroupAdmin(admin.ModelAdmin):

    list_display = ('name', 'image')
    search_fields = ('name', )
    list_per_page = 20


admin.site.register(Group,GroupAdmin)
