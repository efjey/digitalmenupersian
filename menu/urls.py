from django.urls import path, include
from .views import * 

urlpatterns = [  
    path('', start, name="home"),
    path('login_user/', login_user, name="login_user"),
    path('logout_user/', logout_user, name="logout_user"),
]
