from django.db import models


# For Customer Model for test DataBase Scaling 
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


class Bank(models.Model):
  customer = models.ForeignKey(CustomerInformation,on_delete=models.CASCADE)
  account_number = models.IntegerField(null=True)
  branch_name = models.CharField(max_length=20)

  def __str__(self) -> str:
      return self.branch_name     

      