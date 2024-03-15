from django.contrib.auth import models as auth_models
from django.db import models

class User(auth_models.AbstractUser):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique=True)
    username = None
    password = models.CharField(max_length = 255)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []