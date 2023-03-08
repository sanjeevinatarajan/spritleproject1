from django.db import models

# Create your models here.
class master (models.Model):
    input=models.CharField(max_length=250)
    output=models.CharField(max_length=150)
class student (models.Model):
    None


