# from django.conf.urls import url
from django.urls import path, include
from .views import ( SessionListApiView )

urlpatterns = [
    path('api',  SessionListApiView.as_view()),
]