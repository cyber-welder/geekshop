from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from datetime import datetime
from products.models import ProductCategory, Product
from baskets.models import Basket

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):

    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
        'copyright': datetime.now(),
    }
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, 3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator

    if request.user.is_authenticated:
        context['baskets'] = {basket.id: basket.product for basket in Basket.objects.filter(user=request.user)}

    return render(request, 'products/products.html', context)
