from django.urls import path
from . import views

urlpatterns = [
    path("letchat", views.letchat, name='letchat')
]
