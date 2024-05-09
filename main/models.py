import json
from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    """
    Модель Контакта (один на организацию)
    """
    email = models.CharField(max_length=255, verbose_name='Email')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house = models.CharField(max_length=255, verbose_name='Номер дома')

    def __str__(self):
        return f"{self.email}, {self.country}"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Organization(models.Model):
    """
    Модель Организации (несколько на пользователя)
    """
    TYPE_OF_ORGANIZATION = [
        ('factory', 'Завод'),
        ('retail', 'Розничная сеть'),
        ('entrepreneur', 'Индивидуальный предприниматель')
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    type_of_organization = models.CharField(max_length=15, choices=TYPE_OF_ORGANIZATION, verbose_name='Тип организации')
    rang = models.PositiveIntegerField(verbose_name='Уровень в иерархии', default=0)
    parent = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.SET_NULL, **NULLABLE)
    contact = models.ForeignKey(Contact, verbose_name='Контакты', on_delete=models.SET_NULL, **NULLABLE)
    arrears = models.FloatField(verbose_name='Задолженность')
    created = models.DateTimeField(verbose_name='Время создания', auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Product(models.Model):
    """
    Модель Продукта (несколько на организацию)
    """
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.SET_NULL, blank=False,
                                     null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
