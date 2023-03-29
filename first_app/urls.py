from django.urls import path
from . import views

app_name = 'first_app'
urlpatterns = [
    path('', views.app_index, name='app_index'),
    path('home/', views.home, name='home'),
    path('form/', views.forms, name='form'),
    path('testform/', views.test_forms, name='testforms'),
    path('handleform/', views.handle_forms, name='handleform'),
    path('modifyuser/', views.modify_user, name='modifyuser')
]
