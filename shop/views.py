from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from shop.models import Product, Category
# Create your views here.

def index(request):
    text = 'This is the first page.'
    return HttpResponse(text)

def allProdCat(request, c_slug=None):
    c_page= None
    products = None

    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category_id=c_page)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'shop/category.html', {'products' : products, 'category' : c_page})