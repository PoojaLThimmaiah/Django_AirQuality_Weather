from django.urls import path
from airquality_app import views

urlpatterns = [
    path("",views.home,name="home")
]
