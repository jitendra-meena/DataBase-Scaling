from django.db import models

# Create your models here.


class User(models.Model):
  username = models.CharField(max_length=20)
  fullname = models.CharField(max_length=20)

  # def __str__(self):
  #   self.username