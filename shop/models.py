from django.db import models
from datetime import datetime

# Create your models here.

class Company(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    created_at=models.DateField(auto_now_add=True)
    logo=models.ImageField(upload_to='shop/images/company')

    def __str__(self):
        return self.name


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    cat_image = models.ImageField(upload_to='shop/images/category', blank= True, default = '')
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    company = models.ForeignKey(Company, on_delete = models.CASCADE, blank = True)
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_image = models.ImageField(upload_to='shop/images/product')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name