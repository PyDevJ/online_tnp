from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class UserRole(models.TextChoices):
    USER = "user"
    ADMIN = "admin"


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    first_name = models.CharField(max_length=100, verbose_name="имя", **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name="фамилия", **NULLABLE)
    role = models.CharField(choices=UserRole.choices, default="user", max_length=5, verbose_name="role")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
