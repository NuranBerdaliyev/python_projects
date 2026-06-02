
#from django.shortcuts import render, redirect, get_object_or_404
#from django.forms import modelform_factory
#from django.urls import reverse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Task, Category, Project
from .forms import TaskForm, CategoryForm, ProjectForm
class UserQuerySetMixin(LoginRequiredMixin):
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class UserQuerySetTaskMixin(LoginRequiredMixin):
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).select_related('project', 'category')

class UserFormValidMixin(LoginRequiredMixin):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskFormUserFilterMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["project"].queryset = Project.objects.filter(
            user=self.request.user
        )
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form

class RegisterFormView(FormView):
    template_name='registration/register.html'
    form_class=UserCreationForm

    def form_valid(self, form):
        user=form.save()
        login(self.request, user)
        return redirect('tasks_list')
    

class TaskListView(UserQuerySetTaskMixin, ListView):
    model=Task
    template_name='tasks/tasks_list.html'
    context_object_name='tasks'

class TaskDetailView(UserQuerySetTaskMixin, DetailView):
    model=Task
    template_name='tasks/tasks_detail.html'

class TaskCreateView(UserFormValidMixin, TaskFormUserFilterMixin, CreateView):
    model=Task
    template_name='tasks/tasks_form.html'
    form_class=TaskForm
    success_url=reverse_lazy('tasks_list')

class TaskUpdateView(UserFormValidMixin, TaskFormUserFilterMixin, UserQuerySetTaskMixin, UpdateView):
    model=Task
    template_name='tasks/tasks_form.html'
    form_class=TaskForm
    success_url=reverse_lazy('tasks_list')
    
    
class TaskDeleteView(UserQuerySetTaskMixin, DeleteView):
    model=Task
    template_name='tasks/tasks_delete.html'
    success_url=reverse_lazy('tasks_list')

class ProjectListView(UserQuerySetMixin, ListView):
    model=Project
    template_name='projects/projects_list.html'
    context_object_name='projects'

class ProjectDetailView(UserQuerySetMixin, DetailView):
    model=Project
    template_name='projects/projects_detail.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=Task.objects.filter(project=self.object)
        return context
    
class ProjectCreateView(UserFormValidMixin, CreateView):
    model=Project
    template_name='projects/projects_form.html'
    form_class=ProjectForm
    success_url=reverse_lazy('projects_list')
    
class ProjectUpdateView(UserQuerySetMixin, UpdateView):
    model=Project
    template_name='projects/projects_form.html'
    form_class=ProjectForm
    success_url=reverse_lazy('projects_list')   

class ProjectDeleteView(UserQuerySetMixin, DeleteView):
    model=Project
    template_name='projects/projects_delete.html'
    success_url=reverse_lazy('projects_list')

class CategoryListView(UserQuerySetMixin, ListView):
    model=Category
    template_name='categories/categories_list.html'
    context_object_name='categories'

class CategoryDetailView(UserQuerySetMixin, DetailView):
    model=Category
    template_name='categories/categories_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']=Task.objects.filter(category=self.object)
        return context
    
class CategoryCreateView(UserFormValidMixin, CreateView):
    model=Category
    template_name='categories/categories_form.html'
    form_class=CategoryForm
    success_url=reverse_lazy('categories_list')

class CategoryUpdateView(UserQuerySetMixin, UpdateView):
    model=Category
    template_name='categories/categories_form.html'
    form_class=CategoryForm
    success_url=reverse_lazy('categories_list')

class CategoryDeleteView(UserQuerySetMixin, DeleteView):
    model=Category
    template_name='categories/categories_delete.html'
    success_url=reverse_lazy('categories_list')