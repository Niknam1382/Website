from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('',index_view, name='index'),
    path('about-me',aboutme_view, name='about-me'),
    path('projects', project_view, name='projects'),
    path('contact', contact_view, name='contact'),
]

