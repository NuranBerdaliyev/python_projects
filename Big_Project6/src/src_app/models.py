from django.db import models
from django.contrib.auth.models import User
class Project(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    class Meta:
        ordering=['name']
    def __str__(self):
        return self.name

class Category(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    class Meta:
        ordering=['name']
    def __str__(self):
        return self.name

class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    project=models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tasks'
    )
    category=models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    
    title = models.CharField(max_length=255)
    description= models.TextField(blank=True)
    status=models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', "Done")], 
        default='pending')
    priority=models.CharField(max_length=20, choices=[
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')],
        default='medium')
    created_at=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering=['-created_at']
    def __str__(self):
        return self.title