from django.contrib import admin
from website.models import Contact
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = ('created_at')
    empty_value_display = ('-empty-')
    list_display = ['first_name', 'last_name', 'subject', 'email']
    list_filter = ['email']
    search_fields = ['email', 'subject']

admin.site.register(Contact, PostAdmin)