from turtle import title
from django.contrib import admin
from .models import Post

# Register your models here.
class PostDB(admin.ModelAdmin):
    list_display = [
        "title", "text", "author", "created_date", "published_date"
    ]

admin.site.register(Post, PostDB)
