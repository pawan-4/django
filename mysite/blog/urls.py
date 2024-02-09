from django.urls import path
from . import views
#app_name ='blog'
urlpatterns = [
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    ]
