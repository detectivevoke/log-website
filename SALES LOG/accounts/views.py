from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="Pending").count()

    context = {"orders": orders, "customers": customers,"total_orders": total_orders, "orders_pending":orders_pending,"delivered":delivered}
    
    return render(request, 'accounts/dashboard.html',context)
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {"products": products})

def purchase(request):
    f = redirect("https://www.google.com")
    return f

def customer(request):
    return render(request, 'accounts/customer.html', )

