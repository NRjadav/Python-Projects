from django.db import models

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone=models.IntegerField()

    def __str__(self):
        return self.name







