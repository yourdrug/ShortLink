from django.core.validators import URLValidator
from django.db import models


class Links(models.Model):
    class Meta:
        verbose_name = 'Короткие ссылки'
        verbose_name_plural = 'Короткие ссылки'
        ordering = ['time_create']

    shortLink = models.TextField(max_length=100, validators=[URLValidator()])
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    user_name = models.CharField(max_length=50, verbose_name="Имя пользователя")
