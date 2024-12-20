from django.urls import path
from .views import ProductListView, CartView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/<int:pk>/', CartView.as_view(), name='cart-detail'),
]