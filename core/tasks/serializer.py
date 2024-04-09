from rest_framework import serializers
from .models import Task, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
class TaskSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True) 
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'user', 'categories']
