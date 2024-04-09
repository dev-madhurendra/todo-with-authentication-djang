from django.urls import path
from .views import TaskView, product_list

urlpatterns = [
    path('tasks', TaskView.as_view(), name='task-list'),
    path('tasks/<int:pk>', TaskView.as_view(), name='task-detail'),
    path('products', product_list, name='product_list'),
]
