from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.


class Item(models.Model):       # Item = Good

    item_name = models.CharField(max_length=140)        # name = item_name
    section = models.ForeignKey('Section', related_name='goods')       # Category = Section

    def __str__(self):
        return self.item_name


class Section(models.Model):

    section_name = models.CharField(max_length=140, unique=True)    # name = section_name

    def __str__(self):
        return self.section_name


class Items_options(models.Model):        # Goods_Variation = Items_options

    option_name = models.CharField(max_length=140)       # variation_name = option_name
    price = models.DecimalField(max_digits=8, decimal_places=2)      # cost = price
    item_description = models.TextField(blank=True)  # description = item_description
    parent = models.ForeignKey('Item', related_name="item")

    def __str__(self):
        return self.parent.option_name + " " + self.option_name


class Shop_Client(AbstractBaseUser):       # Customer = Shop_client
    user = models.CharField(max_length=100)     # Username = user
    email = models.EmailField(max_length=100, unique=True)  # unique=True


class Basket(models.Model):           # Cart = Basket

    client = models.ForeignKey(Shop_Client, related_name="basket", blank=True, default=None, null=True)

    items = models.ManyToManyField('Items_Options', related_name="in_basket")   # goods = items

    def client_name(self):        # customer_name = client_name
        return self.client.username

    def client_email(self):   # customer_email = client_email
        return self.client.email


