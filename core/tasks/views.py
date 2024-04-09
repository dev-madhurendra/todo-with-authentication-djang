from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from tasks.utils import check_authentication
from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer

class TaskView(APIView):
    def get(self, request, pk=None):
        payload = check_authentication(request)
        tasks = Task.objects.filter(user__id=payload['id'])
        if pk is not None:
            try:
                task = next((task for task in tasks if task.id == pk), None)
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            except Task.DoesNotExist:
                return Response({"message": "Task not found"}, status=404)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        payload = check_authentication(request)
        request.data['user'] = payload['id']
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        payload = check_authentication(request)
        tasks = Task.objects.filter(user__id=payload['id'])
        task = next((task for task in tasks if task.id == pk), None)
        if task is not None:
            request.data['user']=payload['id']
            serializer = TaskSerializer(task, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Task not found"}, status=404)
        

    def delete(self, request, pk):
        payload = check_authentication(request)
        tasks = Task.objects.filter(user__id=payload['id'])
        task = next((task for task in tasks if task.id == pk), None)
        if task is not None:
            task.delete()
            return Response({'message': 'Task deleted successfully'}, status=204)
        return Response({"message": "Task not found"}, status=404)


def product_list(request):
    products = [
        {'name': 'Product 1', 'price': 10.99, 'description': 'Description for Product 1'},
        {'name': 'Product 2', 'price': 20.49, 'description': 'Description for Product 2'},
        {'name': 'Product 3', 'price': 15.99, 'description': 'Description for Product 3'},
    ]
    
    return render(request, 'tasks/product_list.html', {'products': products})
