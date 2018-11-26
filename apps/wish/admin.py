from django.contrib import admin
from django.core.cache import cache
from wish.models import Wish


# class GroupAdmin(admin.ModelAdmin):
#
#     list_display = ('name', 'image')
#     search_fields = ('name', )
#     list_per_page = 20


admin.site.register(Wish)
