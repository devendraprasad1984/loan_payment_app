from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """create custom user model"""


    def create_user(self, email, password=None, **extra_fields):
        """create and save a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    """customer user model that supports using email instead username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
