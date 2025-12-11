from django.http import JsonResponse

from relational_query.models import Product


def products(request):
    #products
    products = Product.objects.all().values()
    return JsonResponse({'products': list(products)})

def inner_join(request):
    #Product > Catagory (inner join)
    products = Product.objects.select_related('category').values(
        'id', 'name', 'price', 'category__id', 'category__name')

    return JsonResponse({'products': list(products)})
