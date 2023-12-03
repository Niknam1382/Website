from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = ('created_at')
    empty_value_display = ('-empty-')
    list_display = ['title','author','created_at','published_at','status']
    list_filter = ['status']
    search_fields = ['title','content','author']

    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)