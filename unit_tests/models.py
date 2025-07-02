from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=18)
    birth_date = models.DateField(null=True)
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'