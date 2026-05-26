from unicodedata import category

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Task, Category, Project
'''
def tasks_list(request):
    tasks=Task.objects.all()
    return render(request, 'tasks/tasks_list.html', {"tasks": tasks})

'''
class TaskListView(ListView):
    model=Task
    template_name='tasks/tasks_list.html'
    context_object_name='tasks'
'''
def tasks_detail(request, task_id):
    task=get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/tasks_detail.html', {"task": task})
'''
class TaskDetailView(DetailView):
    model=Task
    template_name='tasks/tasks_detail.html'
    context_object_name='task'

'''
def projects_list(request):
    projects=Project.objects.all()
    return render(request, 'projects/projects_list.html', {"projects": projects})
'''

class ProjectListView(ListView):
    model=Project
    template_name='projects/projects_list.html'
    context_object_name='projects'

'''
def projects_detail(request, project_id):
    project=get_object_or_404(Project, id=project_id)
    tasks=Task.objects.filter(project=project)
    return render(request, 'projects/projects_detail.html', {
        "project": project,
        "tasks": tasks
    })
'''
class ProjectDetailView(DetailView):
    model=Project
    template_name='projects/projects_detail.html'
    context_object_name='project'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=Task.objects.filter(project=self.object)
        return context
'''
def categories_list(request):
    categories=Category.objects.all()
    return render(request, 'categories/categories_list.html', {"categories": categories})
'''
class CategoryListView(ListView):
    model=Category
    template_name='categories/categories_list.html'
    context_object_name='categories'

'''
def categories_detail(request, category_id):
    category=get_object_or_404(Category, id=category_id)
    tasks=Task.objects.filter(category=category)
    return render(request, 'categories/categories_detail.html', {
        "category": category,
        "tasks": tasks
    })
'''

class CategoryDetailView(DetailView):
    model=Category
    template_name='categories/categories_detail.html'
    context_object_name='category'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']=Task.objects.filter(category=self.object)
        return context
    
    