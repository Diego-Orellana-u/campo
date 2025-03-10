from django.db import models

# Create your models here.
class Menu(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField()
  description = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)