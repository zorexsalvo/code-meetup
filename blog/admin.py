from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('title', 'author__username', 'published_date')
    search_fields = ('title', 'author__username', 'published_date')
