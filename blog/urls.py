from django.urls import path
from .migrations import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
