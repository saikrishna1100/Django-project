from django.db import models

# Create your models here.
class Hostel(models.Model):
    room_id=models.BigIntegerField()
    count=models.BigIntegerField()
    