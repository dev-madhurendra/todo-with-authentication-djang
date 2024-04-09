from django.db import models
from tasks.utils import STATUS_CHOICES
from users.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    categories = models.ManyToManyField(Category, related_name='tasks')
    
    def __str__(self) -> str:
        return self.title