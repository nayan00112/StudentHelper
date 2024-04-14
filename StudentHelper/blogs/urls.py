from django.urls import path
from . import views
urlpatterns = [
    path("faqs/", views.faqs, name="faqs"),
    path("about_us/", views.about_us, name="about_us"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("motivation/", views.motivation, name="motivation"),
    path("articalsread/", views.articalsread, name="articalsread"),
    path("getbookdetails/", views.getbookdetails, name="getbookdetails"),
    path("time_management/", views.time_management, name="time_management"),
]