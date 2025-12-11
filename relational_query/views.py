from django.http import JsonResponse

from relational_query.models import Product


def products(request):
    #products
    products = Product.objects.all().values()
    return JsonResponse({'products': list(products)})
