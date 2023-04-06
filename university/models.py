from django.db import models

# Create your models here.
class College(models.Model):
    name=models.TextField()
    clgid=models.BigIntegerField()
    address=models.TextField()
    