from django.shortcuts import get_object_or_404, render
from order.models import Order

# Create your views here.


def thanks(request, order_id):
    """
    docstring
    """

    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
    return render( request, 'thanks.html', {'customer_order' : customer_order})

