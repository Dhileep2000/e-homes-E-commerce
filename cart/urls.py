from django.urls import path
from .views import *


urlpatterns = [
    
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('success/', success, name='success'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('hx_menu_cart/',hx_menu_cart,name='hx_menu_cart'),
    path('hx_cart_total/',hx_cart_total,name='hx_cart_total'),
    path('update_cart/<int:product_id>/<str:action>',update_cart,name="update_cart"),
    
]
