from django.db import models

# Create your models here.

class Emp(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()