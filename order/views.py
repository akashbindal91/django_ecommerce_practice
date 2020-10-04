from django.shortcuts import get_object_or_404, render
from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.


def thanks(request, order_id):
    """
    docstring
    """

    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
    return render(request, 'thanks.html', {'customer_order': customer_order})


@login_required()
def orderHistory(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(emailAddress=email)
    return render(request, 'order/order_list.html', {'order_details': order_details})


@login_required()
def viewOrder(request, order_id):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.get(
            emailAddress=email, id=order_id)
        order_items = OrderItem.objects.filter(order=order_details)


    return render(request, 'order/order_details.html', {'order_details': order_details, 'order_items': order_items})
