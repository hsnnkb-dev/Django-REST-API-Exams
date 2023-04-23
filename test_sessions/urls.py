# from django.conf.urls import url
from django.urls import path, include
from .views import ( SessionListApiView )

urlpatterns = [
    path('sessions/',  SessionListApiView.as_view()),
]