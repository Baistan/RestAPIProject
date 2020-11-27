import required as required
from django.db import models

# Create your models here.
from register.models import Account


class Product(models.Model):
    types = (
        ('black','black'),
        ('green','green')
    )
    name = models.CharField(max_length=50)
    tea_types = models.CharField(max_length=50,choices=types)
    size = models.IntegerField(default=0)
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=30)
    tastes = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.tea_types

class Adress(models.Model):
    endpoint = models.CharField(max_length=60)
    order = models.ForeignKey('Order',on_delete=models.SET_NULL,null=True,related_name='endpoint')
    def __str__(self):
        return self.endpoint


class Order(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True)
    status = models.BooleanField()
    account = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)

class ProductToOrder(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,related_name='to_order')
    products = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
