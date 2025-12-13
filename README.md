# Django Relational Queries API

This Django project demonstrates **relational database queries** using Django ORM, including **inner joins, outer joins, filtering, and foreign key lookups**. It provides a simple API to interact with `Product`, `Category`, and `InvoiceProduct` models.

---

## Features

- List all products.  
- Perform **inner joins** between `Product` and `Category`.  
- Perform **outer joins** between `Category` and `Product`.  
- Filter data using **select queries**.  
- Lookup data using **foreign keys**.  
- JSON-based API endpoints for easy consumption.  

---

## Requirements

- Python 3.12.3  
- Django 6

Install required packages using:

```bash
pip install -r requirements.txt
```
API Endpoints
1. List Products

Endpoint:
```
def products(request):
    #products
    products = Product.objects.all().values()
    return JsonResponse({'products': list(products)})
```
Description: Retrieve all products.

Response Example:
```
{
  "products": [
    {"id": 1, "name": "Product A", "price": 100, "category_id": 1},
    {"id": 2, "name": "Product B", "price": 200, "category_id": 2}
  ]
}
```
2. Inner Join: Product > Category

Endpoint:
```
def inner_join(request):
    #Product > Category (inner join)
    products = Product.objects.select_related('category').values(
        'id', 'name', 'price', 'category__id', 'category__name')
    return JsonResponse({'products': list(products)})
```
Description: Get products along with their category using an inner join.

Response Example:
```
{
  "products": [
    {"id": 1, "name": "Product A", "price": 100, "category__id": 1, "category__name": "Category X"},
    {"id": 2, "name": "Product B", "price": 200, "category__id": 2, "category__name": "Category Y"}
  ]
}
```
3. Outer Join: Category > Product

Endpoint:
```
def outer_join(request):
    #Category > Product (outer join)
    categories = Category.objects.prefetch_related('products').values(
        'id', 'name','products__id', 'products__name', 'products__price')
    return JsonResponse({'Categorys': list(categories)})
```
Description: Get categories along with their products using outer join (prefetch_related).

Response Example:
```
{
  "Categorys": [
    {"id": 1, "name": "Category X", "products__id": 1, "products__name": "Product A", "products__price": 100},
    {"id": 2, "name": "Category Y", "products__id": 2, "products__name": "Product B", "products__price": 200}
  ]
}
```
4. Select Data with Filtering

Endpoint:
```
def select_data(request):
    categories = Category.objects.filter(username_id=11).values()
    return JsonResponse({'categories': list(categories)})
```
Description: Filter categories by username_id = 11.

Response Example:
```
{
  "categories": [
    {"id": 3, "name": "Category Z", "username_id": 11}
  ]
}
```
5. Foreign Key Lookup

Endpoint:
```
def forenkey_lookup(request):
    invoiceProducts = InvoiceProduct.objects.filter(customer_id=12).values(
        'qty', 'sale_price',
    )
    return JsonResponse({'Invoice Products': list(invoiceProducts)})
```
Description: Lookup InvoiceProduct entries for a specific customer_id = 12.

Response Example:
```
{
  "Invoice Products": [
    {"qty": 2, "sale_price": 100},
    {"qty": 1, "sale_price": 200}
  ]
}
```
<br>
Configuration

Make sure your models.py defines the following relationships:
```
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
```
