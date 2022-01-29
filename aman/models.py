from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=150 ,verbose_name='الاسم')