from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
 
# MENU 
def menu_view(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})

    items = []
    total = 0

    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * qty
        total += subtotal

        items.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal
        })

    return render(request, 'menu.html', {
        'products': products,
        'items': items,
        'total': total
    })


# ADD TO CART
def add_to_cart(request):
    if request.method == 'POST':
        product_id = str(request.POST.get('product_id'))
        cart = request.session.get('cart', {})

        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('menu')


# VIEW CART
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * qty
        total += subtotal

        items.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })


def remove_from_cart(request, product_id):
    product_id = str(product_id)
    cart = request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    return redirect('menu')                


def confirm_order(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * qty
        total += subtotal

        items.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal
        })

    return render(request, 'print.html', {
        'items': items,
        'total': total
    })


def clear_cart(request):
    request.session['cart'] = {}
    return redirect('menu')








