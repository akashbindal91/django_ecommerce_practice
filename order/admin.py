from django.contrib import admin
from order.models import Order, OrderItem
# Register your models here.


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = (
        ('Product', {
            "fields": (
                'product',
            ),
        }),
        ('Quantity', {
            "fields": (
                'quantity',
            ),
        }),
        ('Price', {
            "fields": (
                'price',
            ),
        }),
    )
    readonly_fields = ['product', 'quantity', 'price']

    """ removes the delete option """
    can_delete = False

    """ removes the option to add new """
    max_num = 0

    """ set path here specifically for this file as we have to modify in a different way then the default django | start looking from 24:08 """
    template = 'admin/order/tabular.html'


# admin.site.register(Order, OrderItemAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    docstring
    """
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ['id', 'billingName']
    search_fields = ['id', 'billingName', 'emailAddress']
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created', 'billingName', 'billingAddress1', 'billingCity',
                       'billingPostCode', 'billingCountry', 'shippingName', 'shippingAddress1', 'shippingCity', 'shippingPostCode', 'shippingCountry']

    fieldsets = (
        ('ORDER INFORMATION', {
            'fields': (
                'id', 'token', 'total', 'created'
            ),
        }),
        ('BILLING INFORMATION', {
            'fields': (
                'emailAddress', 'billingName', 'billingAddress1', 'billingCity', 'billingPostCode', 'billingCountry'
            ),
        }),
        ('SHIPPING INFORMATION', {
            'fields': (
                'shippingName', 'shippingAddress1', 'shippingCity', 'shippingPostCode', 'shippingCountry'
            ),
        }),
    )

    inlines = [OrderItemAdmin]

    """ Disable Delete Permission | Removes the delete button """

    def has_delete_permission(self, request, obj=None):
        return False

    """ Disable Add Permission | Removes the Save and add another button """

    def has_add_permission(self, request):
        return False
