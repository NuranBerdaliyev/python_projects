from django.test import TestCase
from django.urls import reverse
from .models import Task, Category, Project
from django.contrib.auth.models import User

class ModelsViewsTest(TestCase):
    def setUp(self):
        self.username='TestUser'
        self.password='123456'
        self.user=User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)
    

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
    
    def test_task_create_page(self):
        data={
            'title': 'test title',
            'description': 'test description',
            'status': 'in_progress', 
            'priority': 'low', 
            'deadline': '2026-05-30 19:07:36',
        }

        response = self.client.post(reverse('tasks_create'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='test title').exists())

    def test_project_create_page(self):
        data={
            'name': 'test name',
        }

        response = self.client.post(reverse('projects_create'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Project.objects.filter(name='test name').exists())
    
    def test_category_create_page(self):
        data={
            'name': 'test name',
        }

        response = self.client.post(reverse('categories_create'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='test name').exists())
    
    def test_task_update_page(self):
        task=Task.objects.create(
            user=self.user,
            title="Test Task",
            description="Test Description",
            status="pending",
            priority="low"
        )
        data={
            'title': 'test task',
            'description': 'test descripter',
            'status': 'done',
            'priority': 'high',
        }
        response=self.client.post(reverse('tasks_update', args=[task.pk]), data=data)
        self.assertEqual(response.status_code, 302)

        task.refresh_from_db()

        self.assertEqual(task.title, 'test task')
        self.assertEqual(task.status, 'done')

    def test_project_update_page(self):
        project=Project.objects.create(
            user=self.user,
            name='Test Name'
        )
        data={
            'name': 'test name',
        }
        response=self.client.post(reverse('projects_update', args=[project.pk]), data=data)
        self.assertEqual(response.status_code, 302)

        project.refresh_from_db()

        self.assertEqual(project.name, 'test name')

    def test_category_update_page(self):
        category=Category.objects.create(
            user=self.user,
            name='Test Name'
        )
        data={
            'name': 'test name',
        }
        response=self.client.post(reverse('categories_update', args=[category.pk]), data=data)
        self.assertEqual(response.status_code, 302)

        category.refresh_from_db()

        self.assertEqual(category.name, 'test name')

    def test_task_delete_page(self):
        task=Task.objects.create(
            user=self.user,
            title="Test Task",
            description="Test Description",
            status="pending",
            priority="low"
        )
        response=self.client.post(reverse('tasks_delete', args=[task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
    
    def test_project_delete_page(self):
        project=Project.objects.create(
            user=self.user,
            name='Test Name'
        )
        response=self.client.post(reverse('projects_delete', args=[project.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=project.id).exists())
    
    def test_category_delete_page(self):
        category=Category.objects.create(
            user=self.user,
            name='Test Name'
        )
        response=self.client.post(reverse('categories_delete', args=[category.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=category.id).exists())

class PermissionTest(TestCase):
    def setUp(self):
        self.password='123456'

        self.user1=User.objects.create_user(
            username='user1',
            password=self.password
        )

        self.user2=User.objects.create_user(
            username='user2',
            password=self.password
        )

    def test_anonymous_tasks_list(self):
        response=self.client.get(reverse('tasks_list'))
        self.assertRedirects(
        response,
        f"{reverse('login')}?next={reverse('tasks_list')}"
        )

    def test_anonymous_task_detail(self):
        task=Task.objects.create(
            user=self.user1,
            title="Test Task",
            description="Test Description",
            status="pending",
            priority="low"
        )
        response=self.client.get(reverse('tasks_detail', args=[task.id]))
        self.assertRedirects(
        response,
        f"{reverse('login')}?next={reverse('tasks_detail', args=[task.id])}"
        )

    def test_anonymous_task_create(self):
        data={
            'title': 'test task',
            'description': 'test descripter',
            'status': 'done',
            'priority': 'high',
        }

        response = self.client.post(reverse('tasks_create'), data=data)
        self.assertRedirects(
        response,
        f"{reverse('login')}?next={reverse('tasks_create')}"
        )
        self.assertFalse(Task.objects.filter(title='test title').exists())
    def test_anonymous_task_update(self):
        task=Task.objects.create(
            user=self.user1,
            title="Test Task",
            description="Test Description",
            status="pending",
            priority="low"
        )

        data={
            'title': 'test task',
            'description': 'test descripter',
            'status': 'done',
            'priority': 'high',
        }

        response = self.client.post(reverse('tasks_update', args=[task.id]), data=data)
        self.assertRedirects(
        response,
        f"{reverse('login')}?next={reverse('tasks_update', args=[task.id])}"
        )
        self.assertEqual(task.title, 'Test Task')
    
    def test_anonymous_task_delete(self):
        task=Task.objects.create(
            user=self.user1,
            title="Test Task",
            description="Test Description",
            status="pending",
            priority="low"
        )
        response=self.client.post(reverse('tasks_delete', args=[task.id]))
        self.assertRedirects(
        response,
        f"{reverse('login')}?next={reverse('tasks_delete', args=[task.id])}"
        )
        self.assertTrue(Task.objects.filter(id=task.id).exists()) 

    def test_user_cannot_see_another_users_task(self):
        task=Task.objects.create(
            user=self.user2,
            title="Test Task",
            description="Test Description",
            status="pending",
            priority="low"
        )
        self.client.login(username='user1', password=self.password)
        response=self.client.get(reverse('tasks_detail', args=[task.pk]))
        self.assertEqual(response.status_code, 404)
    
    def test_user_cannot_see_another_users_project(self):
        project = Project.objects.create(
            user=self.user2,
            name='Secret Project'
        )

        self.client.login(username='user1', password=self.password)

        response = self.client.get(reverse('projects_detail', args=[project.pk]))

        self.assertEqual(response.status_code, 404)


    def test_user_cannot_see_another_users_category(self):
        category = Category.objects.create(
            user=self.user2,
            name='Secret Category'
        )

        self.client.login(username='user1', password=self.password)

        response = self.client.get(reverse('categories_detail', args=[category.pk]))

        self.assertEqual(response.status_code, 404)
            