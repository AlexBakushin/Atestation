from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Organization

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель пользователя
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.SET_NULL, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
