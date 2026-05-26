from django.urls import path
from .views import (TaskListView, 
                    TaskDetailView, 
                    ProjectListView, 
                    ProjectDetailView,
                    CategoryListView,
                    CategoryDetailView)


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='tasks_detail'),
    path('projects/', ProjectListView.as_view(), name='projects_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='projects_detail'),
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='categories_detail'),
]