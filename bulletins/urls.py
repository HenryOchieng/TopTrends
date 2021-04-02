from django.urls import path
from bulletins import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('', views.loadcontent, name="Loadcontent"),
]