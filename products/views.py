from django.shortcuts import render

from datetime import datetime
from products.models import ProductCategory, Product
from baskets.models import Basket

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):

    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
        'copyright': datetime.now(),
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    }
    if request.user.is_authenticated:
        context['baskets'] = {basket.id: basket.product for basket in Basket.objects.filter(user=request.user)}

    return render(request, 'products/products.html', context)
