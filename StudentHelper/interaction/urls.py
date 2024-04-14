from django.urls import path
from . import views

urlpatterns = [
    path("showque", views.showque, name="showque"),
    path("addquestion", views.addquestion, name="addquestion"),
    path("showque", views.showque, name="showque"),
    path("addans/<int:queid>/", views.addans, name="addans"),
]
