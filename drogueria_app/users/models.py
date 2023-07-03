from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    identify_card = models.IntegerField
    phone_number = models.IntegerField
    role = models.CharField(max_length=50)
    user = models.CharField(max_length=80)
    password = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    laboratory = models.CharField(max_length=100)
    INVIMA = models.CharField(max_length=150)
    batch = models.CharField(max_length=150)
    expiration_date = models.DateField("expiration date")
    price = models.IntegerField
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Regiter(models.Model):
    stock = models.IntegerField
    date_entry = models.DateField("date entry")
    total_value = models.IntegerField
    user = models.ForeignKey(User,on_delete=models.CASCADE)
