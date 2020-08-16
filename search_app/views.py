from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.

def searchResult(request):
    product = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        product = Product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
        # product = Product.objects.all().filter(Q(name__iexact=query) | Q(description__iexact=query))
        
    return render(request, 'search_app/search.html', {'query' : query, 'products' : product})