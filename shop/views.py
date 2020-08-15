from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from shop.models import Product, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.


def index(request):
    text = 'This is the first page.'
    return HttpResponse(text)


def allProdCat(request, c_slug=None):
    c_page = None
    product_list = None

    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.filter(category_id=c_page)
    else:
        product_list = Product.objects.all().filter(available=True)

    """ Pagination Integrated """
    paginator = Paginator(product_list, 6) # Show 25 products per page

    try:
        # get has second parameter here. ?
        page = int(request.GET.get('page', '1')) 
    except:
        page = 1

    try:
        products = paginator.page(page)
    except ( EmptyPage, InvalidPage ):
        products = paginator.page( paginator.num_pages )
    
    return render(request, 'shop/category.html', {'products': products, 'category': c_page})


def ProdCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
        # print(product.query)
        print(Product.objects.filter(category__slug=c_slug, slug=product_slug).query)

        """ This above Query will perform as """
        # SELECT * FROM `shop_product` INNER JOIN `shop_category` ON (`shop_product`.`category_id` = `shop_category`.`id`) WHERE (`shop_category`.`slug` = category-4 AND `shop_product`.`slug` = product-4) ORDER BY `shop_product`.`name` ASC

        """ Explain category__slug=c_slug """
        # from category table where slug = c_slug

    except Exception as e:
        raise e

    return render(request, 'shop/product.html', {'product': product})
