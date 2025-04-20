# urunler/urls.py

from django.urls import path
from .views import product_entry

urlpatterns = [
    path('', product_entry, name='product-entry'),
]
