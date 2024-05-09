from django.contrib import admin
from users.models import User

admin.site.register(User)  # Регистрация модели пользователя в админ панели
