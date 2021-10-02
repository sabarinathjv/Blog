from django.contrib import admin
from .models import *

# admin.site.register(Article)



@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')#to add  filter on right
    list_display = ('title', 'description')#to add list view with data 
