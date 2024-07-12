from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list_and_review, name='about'),
]