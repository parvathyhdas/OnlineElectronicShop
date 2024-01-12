from django.db import models

# Create your models here.
class ContactDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.CharField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=50,null=True,blank=True)

class RegisterDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField( null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    UserName = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)


class CartDB(models.Model):
    UserName = models.CharField(max_length=50, null=True,blank=True)
    ProductName = models.CharField(max_length=50, null=True,blank=True)
    Description = models.CharField(max_length=500, null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Totalprice = models.IntegerField(null=True,blank=True)
