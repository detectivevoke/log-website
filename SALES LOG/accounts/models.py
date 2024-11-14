from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
class Product(models.Model):

    CATEGORY = (
        ("Tree", "Tree"),
        ("Decoration", "Decoration")
    )
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):

    STATUS= (
    ("Not Ordered", "Not Ordered"),
    ("Waiting for delivery", "Waiting for delivery"),
    ("Got Delivery, going to deliver", "Got Delivery, going to deliver"),
    ("Delivered","Delivered")
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
