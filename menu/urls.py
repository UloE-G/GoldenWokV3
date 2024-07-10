from . import views
from django.urls import path

urlpatterns = [
    path('', views.my_menu, name='menu'),
]