from django.urls import path
from accounts.views import *

app_neme = 'accounts'

urlpatterns = [ # login - logout - sign up (registration) & ...
    path('login', login_view, name='login'),
]