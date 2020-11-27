from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager,PermissionsMixin
from django.db import models

# Create your models here.
class Account(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=200,unique=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()


    def __str__(self):
        return self.username

