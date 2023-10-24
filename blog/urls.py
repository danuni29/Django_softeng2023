from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]
