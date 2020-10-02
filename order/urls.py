

from order import views
from django.urls import path
app_name= 'order'
urlpatterns = [
    path('thanks/<int:order_id>/', views.thanks, name='thanks')
]
