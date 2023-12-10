from django.db import models
from worker.models import Worker

class Brands(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название брэнда')
    description = models.TextField(default='Нет описания')
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    workers = models.ManyToManyField(
        to=Worker,
        blank=True,
        related_name='brand',
    )

    def __str__(self):
        return self.name