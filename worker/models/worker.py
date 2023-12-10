from django.db import models
from django.contrib.auth.models import User

class Worker(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    is_working = models.BooleanField(default=True)

    def __str__(self):
        return self.name