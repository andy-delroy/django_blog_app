from csv import list_dialects
from email.mime import image
from django.contrib import admin
from .models import BlogPost, Image

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    #either list or tuple works?
    list_display = ('title', 'slug', 'date_created')
    search_fields = ('title', 'text'),
    ordering = ('date_created',)
    prepopulated_fields = {'slug': ['title']}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Image)