from django import forms
from .models import Task, Category, Project

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=[
            'title',
            'description',
            'status',
            'priority',
            'deadline',
            'project',
            'category',
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=[
            'name',
        ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=[
            'name',
        ]

