from django.test import TestCase
from django.urls import reverse
from .models import Task, Category, Project
from django.contrib.auth.models import User

class TaskViewsTest(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='TestUser', password='123456')
    

    def test_tasks_list_page(self):
        response=self.client.get(reverse('tasks_list'))
        self.assertEqual(response.status_code, 200)

    def test_projects_list_page(self):
        response=self.client.get(reverse('projects_list'))
        self.assertEqual(response.status_code, 200)

    def test_categories_list_page(self):
        response=self.client.get(reverse('categories_list'))
        self.assertEqual(response.status_code, 200)

    def test_task_detail_page(self):
        task=Task.objects.create(
            user=self.user,
            title="Test Task",
            description="Test Description",
            status="pending",
            priority="low"
        )
        response=self.client.get(reverse('tasks_detail', args=[task.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_project_detail_page(self):
        project=Project.objects.create(
            user=self.user,
            name='Test Name'
        )
        response=self.client.get(reverse('projects_detail', args=[project.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_category_detail_page(self):
        category=Category.objects.create(
            user=self.user,
            name='Test Name'
        )
        response=self.client.get(reverse('categories_detail', args=[category.id]))
        self.assertEqual(response.status_code, 200)