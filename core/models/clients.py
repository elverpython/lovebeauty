from django.db import models
from worker.models import Worker
from core.models import Brands

class Clients(models.Model):
    name = models.CharField(max_length=255, verbose_name='Клиент')
    description = models.TextField(default='Нет описания', verbose_name='Примечание')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    workers = models.ManyToManyField(
        to=Worker,
        blank=True,
        related_name='client',
    )
    brand = models.ForeignKey(
        to=Brands,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name