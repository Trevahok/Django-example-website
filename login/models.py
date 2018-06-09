from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=64,primary_key=True)
    password=models.CharField(max_length=64)
    def __str__(self):
        return self.username
