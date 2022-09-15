from django.urls import path
from .views import ShopView, ProductDetailView, wishlist_view, WishListView, update_cart_view, ShoppingCart

app_name = 'shop'

urlpatterns = [
    path('', ShopView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/<int:pk>/wishlist/', wishlist_view, name='wishlist'),
    path('wishlists/', WishListView.as_view(), name='all_wishlists'),
    path('add_cart/<int:id>/', update_cart_view, name='cart'),
    path('shopping_cart/', ShoppingCart.as_view(), name='shopping-cart')
]
