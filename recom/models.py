from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.IntegerField(null=False)
    name = models.CharField(max_length=32, null=False)
    url = models.CharField(max_length=225, null=False)
