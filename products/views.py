from django.shortcuts import render
from datetime import datetime
import json


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):

    with open('products/fixtures/products.json', 'r', encoding='utf-8') as f:
        json_products = json.load(f)

    context = {
        'title': 'GeekShop - Каталог',
        'products': json_products,
        'copyright': datetime.now(),
    }
    return render(request, 'products/products.html', context)
