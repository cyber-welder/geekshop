from django.shortcuts import render

from datetime import datetime
from products.models import ProductCategory, Product
from baskets.models import Basket

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):

    goods = Product.objects.all()
    categories = ProductCategory.objects.all()
    baskets = {}
    if request.user.is_authenticated:
        baskets = {basket.product: basket.id for basket in Basket.objects.filter(user=request.user)}

    context = {
        'title': 'GeekShop - Каталог',
        'products': goods,
        'categories': categories,
        'baskets': baskets,
        'copyright': datetime.now(),
    }
    return render(request, 'products/products.html', context)
