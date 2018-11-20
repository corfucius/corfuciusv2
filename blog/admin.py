from django.contrib import admin
from .models import Posts
from django.contrib import admin

class blogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    list_per_page = 25

admin.site.register(Posts, blogAdmin)
