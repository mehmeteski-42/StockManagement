# urunler/utils.py

def convert_to_base_unit(product, quantity, unit_input):
    if product.unit_type == "adet-koli":
        if unit_input == "koli":
            return quantity * product.unit_per_package
        elif unit_input == "adet":
            return quantity
    return quantity
