from django.contrib import admin
from shop.models import Product, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    """ list_display """
    # add fields you want to see in admin under above list
    list_display = ['name', 'slug']
    """ prepopulated_fields """
    # helps to auto update / overwrite as soon as its parent fields is updated
    prepopulated_fields = { 'slug' : ('name', )}
    """ list_per_page """
    # gives you pagination
    list_per_page = 20
admin.site.register( Category, CategoryAdmin )

class ProductAdmin(admin.ModelAdmin):
    """ list_display """
    # add fields you want to see in admin under above list
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated' ]
    """ list_editable """
    # show editable fields on the admin itself without entering into the object itself
    list_editable = ['price', 'stock', 'available']
    """ prepopulated_fields """
    # helps to auto update / overwrite as soon as its parent fields is updated
    prepopulated_fields = { 'slug' : ('name', )}
    """ list_per_page """
    # gives you pagination
    list_per_page = 20
admin.site.register(Product, ProductAdmin )