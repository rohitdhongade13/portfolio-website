import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(default='', max_length=123)
    phone = models.CharField(default='',max_length=12)
    email = models.EmailField(default='')
    dese = models.TextField()