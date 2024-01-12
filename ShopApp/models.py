from django.db import models

# Create your models here.
class ShopDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.CharField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to="Images",null=True,blank=True)
    Location = models.CharField(max_length=50,null=True,blank=True)
    Address = models.CharField(max_length=50,null=True,blank=True)

class CategoryDB(models.Model):
    CategoryName = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=50,null=True,blank=True)
    CategoryImage = models.ImageField(upload_to="CateogoryImages",null=True,blank=True)

class ProductDB(models.Model):
    CategoryName = models.CharField(max_length=50,null=True,blank=True)
    ProductName = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=50,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    ProductImage = models.ImageField(upload_to="ProductImages",null=True,blank=True)

# class ContactDB(models.Model):
#     Name = models.CharField(max_length=50,null=True,blank=True)
#     Email = models.CharField(max_length=50,null=True,blank=True)
#     Message = models.CharField(max_length=50,null=True,blank=True)
