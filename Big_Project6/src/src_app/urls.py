from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='tasks_detail'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:project_id>/', views.projects_detail, name='projects_detail'),
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/<int:category_id>/', views.categories_detail, name='categories_detail'),
]