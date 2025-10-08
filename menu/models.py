from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
   
class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    price = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='upload/product/', null=True, blank=True)
    is_available = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(default='', blank=False, max_length=400)
    phone = models.CharField(max_length=15, blank=False)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

