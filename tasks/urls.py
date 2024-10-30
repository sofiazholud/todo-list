# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/update/<int:pk>/', views.task_update, name='task_update'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tag/create/', views.tag_create, name='tag_create'),
    path('tag/update/<int:pk>/', views.tag_update, name='tag_update'),
    path('tag/delete/<int:pk>/', views.tag_delete, name='tag_delete'),
]
