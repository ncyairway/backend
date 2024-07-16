from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telephone = models.CharField(max_length=15, unique=True)
    IDENTITY_CHOICES = (
        (1, 'Supplier'),
        (2, 'Purchaser'),
        (3, 'Administrator'),
    )
    identity = models.IntegerField(choices=IDENTITY_CHOICES)

class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    address = models.TextField()

class Order(models.Model):
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    buyer = models.ForeignKey(User, related_name='buyer_orders', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='seller_orders', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    order_time = models.DateTimeField()
    delivery_time = models.DateTimeField()
    ORDER_STATUS_CHOICES = (
        (0, 'Unpaid'),
        (1, 'Paid'),
        (2, 'Delivered'),
        (3, 'Confirmed by Seller'),
        (4, 'Cancelled'),
    )
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES)
    

class SingleGood(models.Model):
    order = models.ForeignKey(Order,related_name='order_goods', on_delete=models.CASCADE)
    commodity = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    amount = models.IntegerField()
    

class Commodity(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to='images/commodity_images/')
    sales_volume = models.IntegerField()
    suppliers = models.ForeignKey(User, related_name='supplied_commodities', on_delete=models.CASCADE)
    Commodity_STATUS_CHOICES = (
        (0, 'On_Shelves'),
        (1, 'off_shelves'),
        (2, 'disuse'),
    )
    commodity_status = models.IntegerField(choices=Commodity_STATUS_CHOICES)