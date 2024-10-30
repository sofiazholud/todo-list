# tasks/urls.py
from django.urls import path

from . import views
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TagListView, TagCreateView, TagDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/create/', TagCreateView.as_view(), name='tag_create'),
    path('tag/update/<int:pk>/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag/delete/<int:pk>/', TagDeleteView.as_view(), name='tag_delete'),
]
