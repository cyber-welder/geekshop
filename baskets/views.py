from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from baskets.models import Basket


@login_required()
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        messages.success(request, 'Товар успешно добавлен в корзину')
    else:
        basket = baskets.first()
        if basket.quantity >= product.quantity:
            messages.warning(request, 'Не возможно добавить товар! Количество товара ограничено.')
        else:
            basket.quantity += 1
            basket.save()
            messages.success(request, 'Товар успешно добавлен в корзину')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required()
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
