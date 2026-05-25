from django.shortcuts import render, get_object_or_404
from .models import Task, Category, Project

def tasks_list(request):
    tasks=Task.objects.all()
    return render(request, 'tasks/tasks_list.html', {"tasks": tasks})

def tasks_detail(request, task_id):
    task=get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/tasks_detail.html', {"task": task})

def projects_list(request):
    projects=Project.objects.all()
    return render(request, 'projects/projects_list.html', {"projects": projects})

def projects_detail(request, project_id):
    project=get_object_or_404(Project, id=project_id)
    tasks=Task.objects.filter(project=project)
    return render(request, 'projects/projects_detail.html', {
        "project": project,
        "tasks": tasks
    })

def categories_list(request):
    categories=Category.objects.all()
    return render(request, 'categories/categories_list.html', {"categories": categories})

def categories_detail(request, category_id):
    category=get_object_or_404(Category, id=category_id)
    tasks=Task.objects.filter(category=category)
    return render(request, 'categories/categories_detail.html', {
        "category": category,
        "tasks": tasks
    })