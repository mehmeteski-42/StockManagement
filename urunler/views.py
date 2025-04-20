# urunler/views.py

from django.shortcuts import render, redirect
from .models import Product
from .utils import convert_to_base_unit
from django.contrib import messages

def product_entry(request):
    if request.method == 'POST':
        barcode = request.POST['barcode']
        name = request.POST.get('name')
        quantity = float(request.POST['quantity'])
        unit = request.POST['unit']

        try:
            product = Product.objects.get(barcode=barcode)
            converted_qty = convert_to_base_unit(product, quantity, unit)
            product.stock_quantity += converted_qty
            product.save()
            messages.success(request, f"{product.name} güncellendi. Yeni stok: {product.stock_quantity}")
        except Product.DoesNotExist:
            unit_type = request.POST.get('unit_type')
            unit_per_package = int(request.POST.get('unit_per_package', 1))
            if unit_type != 'adet-koli':
                unit_per_package = None
            new_product = Product.objects.create(
                barcode=barcode,
                name=name,
                unit_type=unit_type,
                unit_per_package=unit_per_package,
                stock_quantity=quantity if unit_type != 'adet-koli' else quantity * unit_per_package
            )
            messages.success(request, f"{new_product.name} sisteme eklendi.")
        return redirect('product-entry')

    return render(request, 'urunler/entry.html')
