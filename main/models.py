import json
from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    email = models.CharField(max_length=255, verbose_name='Email')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house = models.CharField(max_length=255, verbose_name='Номер дома')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    rang = models.PositiveIntegerField(verbose_name='Уровень в иерархии', default=0)
    parent = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.SET_NULL, **NULLABLE)
    contact = models.ForeignKey(Contact, verbose_name='Контакты', on_delete=models.SET_NULL, **NULLABLE)
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    arrears = models.FloatField(verbose_name='Задолженность')
    created = models.DateTimeField(verbose_name='Время создания', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'




