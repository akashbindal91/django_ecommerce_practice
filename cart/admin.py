from django.contrib import admin
# from shop.models import Product, Category
from cart.models import Cart, CartItem
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    # """ list_display """
    # add fields you want to see in admin under above list
    list_display = ['cart_id', 'date_added']
    # """ prepopulated_fields """
    # helps to auto update / overwrite as soon as its parent fields is updated
    # prepopulated_fields = { 'slug' : ('name', )}
    """ list_per_page """
    # gives you pagination
    list_per_page = 20
admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    # """ list_display """
    # add fields you want to see in admin under above list
    list_display = ['product', 'cart']
    # """ prepopulated_fields """
    # helps to auto update / overwrite as soon as its parent fields is updated
    # prepopulated_fields = { 'slug' : ('name', )}
    """ list_per_page """
    # gives you pagination
    list_per_page = 20
admin.site.register(CartItem, CartItemAdmin)
