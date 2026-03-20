from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager
from apps.core.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.role = "admin"
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("vendor", "Vendor"),
        ("customer", "Customer"),
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.name