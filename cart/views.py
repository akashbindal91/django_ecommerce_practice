from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from shop.models import Product
# Create your views here.

""" Create Cart details from the session of the request """
""" Cart_id acn also be reference as bill no or order no """
def _cart_id(request):
    """ get session key from the request so as to determine which user create the order """
    cart = request.session.session_key
    
    if not cart:
        cart = request.session.create()
    return cart


""" Add item to the cart table by product """
def add_cart(request, product_id):
    # product = Product.objects.get(pk=product_id)
    """ get product details """
    product = Product.objects.get(id=product_id)
    
    """ get cart details """
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    """ create cart list of the goods to keep track on and generate billing system
        Add item to the cart product wise """
    try:
        """ product already exist increase its quantity """
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        """ product doesnot exist so create it with quantity 1 """
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
        cart_item.save()

    return redirect('cart:cart_detail')


""" Get Cart Details """
def cart_detail(request, total=0, counter=0, cartItems=None):
    try:
        """ get Cart / bill no """
        cart = Cart.objects.get(cart_id = _cart_id(request))

        """ get items with refrence to cart_id or bill no where status is active """
        cart_items = CartItem.objects.filter(cart = cart, active=True)

        """ calculate total amount and total no. of items """
        for cart_item in cart_items:
            total   += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    # either use step 1 or step 2, It wont matter
    
    # step 1
    # return render(request, 'cart.html', { cart_item : cart_items, total : total, counter : counter })

    # step 2
    return render(request, 'cart/cart.html', dict(cart_items = cart_items, total = total, counter = counter) ) 