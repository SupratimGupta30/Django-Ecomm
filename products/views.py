from products.models import SizeVariant
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from products.models import Product
from accounts.models import Cart, CartItem

# Create your views here.


def get_products(request, slug):
    try:
        product = Product.objects.get(slug= slug)

        context={'product': product}

        if request.GET.get("size"):
            size = request.GET.get("size")
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            print(price)
        return render(request, 'product/product.html', context)
    except Exception as e:
        print(e)


@login_required
def add_to_cart(request, uid):
    variant= request.GET.get("variant")
    product = Product.objects.get(uid= uid)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user = user, is_paid=False)

    cart_item = CartItem.objects.create(cart = cart, product = product)
        
    if variant:
        variant = request.GET.get("variant")
        size_variant = SizeVariant.objects.get(size_name=variant)
        cart_item.size_variant = size_variant
        cart_item.save()
        
    return HttpResponseRedirect(request.path_info)