from django.contrib import admin
from .models import *
class HashTagAdmin(admin.ModelAdmin):
    list_display=('HashTag','TimeStamp')
admin.site.register(QueryHashTag,HashTagAdmin)