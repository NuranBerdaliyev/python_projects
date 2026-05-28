
#from django.shortcuts import render, redirect, get_object_or_404
#from django.forms import modelform_factory
#from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
def tasks_create(request):
    TaskForm=modelform_factory(
        Task, 
        fields=['title', 'description', 'status', 'priority', 'deadline', 'project', 'category']
    )
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks_list'))
    elif request.method=='GET':
        form=TaskForm()
    context={'form': form}
    return render(request, 'tasks/task_form.html', context)
'''
class TaskCreateView(CreateView):
    model=Task
    template_name='tasks/tasks_form.html'
    fields=['title', 'description', 'status', 'priority', 'deadline', 'project', 'category']
    success_url=reverse_lazy('tasks_list')

'''
def tasks_update(request, task_id):
    task=get_object_or_404(Task, id=task_id)
    TaskForm=modelform_factory(
        Task,
        fields=['title', 'description', 'status', 'priority', 'deadline', 'project', 'category']
    )
    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    elif request.method=='GET':
        form=TaskForm(instance=task)
    context={
        'form': form,
        'task': task
    }
    return render(request, 'tasks/task_form.html', context)
'''
class TaskUpdateView(UpdateView):
    model=Task
    template_name='tasks/tasks_form.html'
    fields=['title', 'description', 'status', 'priority', 'deadline', 'project', 'category']
    success_url=reverse_lazy('tasks_list')

'''
def tasks_delete(request, task_id):
    task=get_object_or_404(Task, id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect(reverse('tasks_list'))
    context={'task': task}
    return render(request, 'tasks/tasks_delete.html', context)
'''
class TaskDeleteView(DeleteView):
    model=Task
    template_name='tasks/tasks_delete.html'
    success_url=reverse_lazy('tasks_list')

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
    
class ProjectCreateView(CreateView):
    model=Project
    template_name='projects/projects_form.html'
    fields=['name']
    success_url=reverse_lazy('projects_list')

class ProjectUpdateView(UpdateView):
    model=Project
    template_name='projects/projects_form.html'
    fields=['name']
    success_url=reverse_lazy('projects_list')

class ProjectDeleteView(DeleteView):
    model=Project
    template_name='projects/projects_delete.html'
    success_url=reverse_lazy('projects_list')

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
    
class CategoryCreateView(CreateView):
    model=Category
    template_name='categories/categories_form.html'
    fields=['name']
    success_url=reverse_lazy('categories_list')

class CategoryUpdateView(UpdateView):
    model=Category
    template_name='categories/categories_form.html'
    fields=['name']
    success_url=reverse_lazy('categories_list')

class CategoryDeleteView(DeleteView):
    model=Category
    template_name='categories/categories_delete.html'
    success_url=reverse_lazy('categories_list')