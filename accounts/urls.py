from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [ # login - logout - sign up (registration) & ...
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
    path('reset', reset_view, name='reset'),
    path('change', change_password, name='change'),
]