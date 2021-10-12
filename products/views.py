from django.shortcuts import render

from datetime import datetime
from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):

    goods = Product.objects.all()
    categories = ProductCategory.objects.all()

    context = {
        'title': 'GeekShop - Каталог',
        'products': goods,
        'categories': categories,
        'copyright': datetime.now(),
    }
    return render(request, 'products/products.html', context)
