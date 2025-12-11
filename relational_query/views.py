from django.http import JsonResponse

from relational_query.models import Product, Category, InvoiceProduct


def products(request):
    #products
    products = Product.objects.all().values()
    return JsonResponse({'products': list(products)})

def inner_join(request):
    #Product > Category (inner join)
    products = Product.objects.select_related('category').values(
        'id', 'name', 'price', 'category__id', 'category__name')

    return JsonResponse({'products': list(products)})

def outer_join(request):
    #Category > Product (outer join)
    categories = Category.objects.prefetch_related('products').values(
        'id', 'name','products__id', 'products__name', 'products__price')

    return JsonResponse({'Categorys': list(categories)})

def select_data(request):
    categories = Category.objects.filter(username_id=11).values()
    return JsonResponse({'categories': list(categories)})

def forenkey_lookup(request):
    invoiceProducts = InvoiceProduct.objects.filter(customer_id=12).values(
        'qty', 'sale_price',
    )
    return JsonResponse({'Invoice Products': list(invoiceProducts)})