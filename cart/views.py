from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart, CartItem
from shop.models import Product
import stripe
from django.conf import settings
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
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
        # cart_item.quantity += 1
        # cart_item.save()
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
        cart = Cart.objects.get(cart_id=_cart_id(request))

        """ get items with refrence to cart_id or bill no where status is active """
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        """ calculate total amount and total no. of items """
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    """ integration of stripe payment gateway integration """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_total = int(total)
    description = 'perfect cusion stipe interation test : new order'

    # either use step 1 or step 2, It wont matter

    # step 1
    # return render(request, 'cart.html', { cart_item : cart_items, total : total, counter : counter })

    # step 2

    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            customer = stripe.Customer.create(email=email, source=token)
            charge = stripe.Charge.create(amount=stripe_total, currency='inr', description=description,
                                          customer=customer.id)
        except stripe.error.CardError as e:
            return False,e
        # print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': ['j3k5pviaMgQGB32O7QLZmuik8yq4juMY4zTVejR8cuanPjmQXdy4pKHBwM3s7DNx'], 'stripeToken': ['tok_1HS5KPEcB39RSPvROkNWv5oj'], 'stripeTokenType': ['card'], 'stripeEmail': ['akashbindal91@gmail.com'], 'stripeBillingName': ['Akash'], 'stripeBillingAddressCountry': ['India'], 'stripeBillingAddressCountryCode': ['IN'], 'stripeBillingAddressZip': ['458470'], 'stripeBillingAddressLine1': ['D 1/2, vikram cement staff colony, nimach, madhya pradesh'], 'stripeBillingAddressCity': ['nimach'], 'stripeBillingAddressState': ['35'], 'stripeShippingName': ['Akash'], 'stripeShippingAddressCountry': ['India'], 'stripeShippingAddressCountryCode': ['IN'], 'stripeShippingAddressZip': ['458470'], 'stripeShippingAddressLine1': ['D 1/2, vikram cement staff colony, nimach, madhya pradesh'], 'stripeShippingAddressCity': ['nimach'], 'stripeShippingAddressState': ['35']}>
    return render(request, 'cart/cart.html', dict(cart_items=cart_items, total=total, counter=counter, data_key=data_key, description=description, stripe_total=stripe_total))


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def full_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
