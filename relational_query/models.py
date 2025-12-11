from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField()
    password = models.CharField(max_length=500)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='categories')  #remove user data (models.CASCADE) use
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places= 2)  #most important (decimal_places) part
    unit = models.CharField(max_length=100)
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField()
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='customers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invoice(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_due = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='invoices')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='invoices')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InvoiceProduct(models.Model):
    qty = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.ForeignKey(User, on_delete=models.CASCADE,related_name='invoice_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='invoice_products')
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,related_name='invoice_products')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='invoice_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)