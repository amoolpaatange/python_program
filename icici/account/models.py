from django.db import models

# Create your models here.
class emp(models.Model):
        dept_name=models.CharField(max_length=26)
        dept_city = models.CharField(max_length=24)
        dept_id = models.IntegerField()
class saving(models.Model):
        dept_name=models.CharField(max_length=26)
        dept_city = models.CharField(max_length=24)
