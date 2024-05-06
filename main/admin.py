from django.contrib import admin
from main.models import Organization, Product, Contact


@admin.register(Organization)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rang', 'parent', 'contact', 'arrears', 'created')


@admin.register(Product)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date',)


@admin.register(Contact)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house')
    list_filter = ('city',)
