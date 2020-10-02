from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from shop.models import Product, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from shop.forms import SignUpForm
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
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
    paginator = Paginator(product_list, 10)  # Show 25 products per page

    """ Both The Steps Can  be used for pagination"""
    """ this is step 1 """
    """ start """
    try:
        # get has second parameter here. ?
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    """ end """

    """ this is step 2 """
    """ start """
    # page = request.GET.get('page')
    # products = paginator.get_page(page)
    """ end """

    return render(request, 'shop/category.html', {'products': products, 'category': c_page})


def ProdCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
        # print(product.query)
        print(Product.objects.filter(
            category__slug=c_slug, slug=product_slug).query)

        """ This above Query will perform as """
        # SELECT * FROM `shop_product` INNER JOIN `shop_category` ON (`shop_product`.`category_id` = `shop_category`.`id`) WHERE (`shop_category`.`slug` = category-4 AND `shop_product`.`slug` = product-4) ORDER BY `shop_product`.`name` ASC

        """ Explain category__slug=c_slug """
        # from category table where slug = c_slug

    except Exception as e:
        raise e

    return render(request, 'shop/product.html', {'product': product})


def signupView(request):
    """
    docstring
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
        else:
            pass
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signinView(request):
    """
    docstring
    """

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('shop:allProdCat')
            else:
                return redirect('signup')
        else:
            pass
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})


def signoutView(request):
    logout(request)
    return redirect('signin')