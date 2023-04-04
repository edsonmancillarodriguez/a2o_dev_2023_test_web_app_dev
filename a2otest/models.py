from django.db import models


# Create your models here.
class A2Otest(models.Model):
    name = models.CharField('Nombre', max_length=50)
