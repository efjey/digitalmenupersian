from django.urls import path, include
from .views import start

urlpatterns = [  
    path('', start)
]
