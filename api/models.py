from django.db import models
from datetime import date

# Create your models here.

class FormTest(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, default=date.today())
