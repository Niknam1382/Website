from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('',index_view, name='index'),
    path('about-us',aboutus_view, name='about-us'),
    path('services', services_view, name='services'),
    path('about-me',aboutme_view, name='about-me'),
    path('team', team_view, name='team'),
    path('projects', project_view, name='projects'),
    path('contact', contact_view, name='contact'),
]