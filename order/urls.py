

from order import views
from django.urls import path
app_name= 'order'
urlpatterns = [
    path('thanks/<int:order_id>/', views.thanks, name='thanks'),
    path('history/', views.orderHistory, name='order_history'),
    path('view_order/<int:order_id>/', views.viewOrder, name='view_order'),
]
