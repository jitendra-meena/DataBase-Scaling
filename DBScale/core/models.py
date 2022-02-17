from django.db import models



class Customer(models.Model):
  name = models.CharField(max_length=20)
  address = models.CharField(max_length=50)
  city = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name


class CustomerSupport(models.Model):
  name = models.CharField(max_length=20)
  address = models.CharField(max_length=50)
  city = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name  
  
  
class CustomerInformation(models.Model):
  name = models.CharField(max_length=20)
  detail = models.CharField(max_length=50)
  city = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name  