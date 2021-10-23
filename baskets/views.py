from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

from products.models import Product
from baskets.models import Basket


@login_required()
def basket_add(request, product_id):
    if request.is_ajax():
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)
        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=1)
        context = {
            'product': product,
            'baskets': {basket.product: basket.id for basket in Basket.objects.filter(user=request.user)},
        }
        return JsonResponse({
            'result': render_to_string('products/button.html', context)
        })


@login_required()
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    if request.is_ajax():
        context = {
            'product': basket.product,
            'baskets': {basket.product: basket.id for basket in Basket.objects.filter(user=request.user)},
        }
        result = render_to_string('products/button.html', context)
        return JsonResponse({
            'result': result
        })
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required()
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        baskets = Basket.objects.filter(user=request.user)
        total_quantity = Product.objects.get(id=basket.product.id).quantity
        if quantity > 0:
            if quantity <= total_quantity:
                basket.quantity = quantity
                basket.save()
        else:
            basket.delete()
    context = {
        'baskets': baskets
    }
    return JsonResponse({
        'result': render_to_string('baskets/basket.html', context)
    })
