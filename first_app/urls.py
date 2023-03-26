from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_index, name='app_index'),
    path('home/', views.app_home, name='app_home')
]
