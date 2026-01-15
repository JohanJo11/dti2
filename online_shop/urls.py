from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove'),
    path('confirm/', views.confirm_order, name='confirm'),
    path('clear/', views.clear_cart, name='clear'),
]
