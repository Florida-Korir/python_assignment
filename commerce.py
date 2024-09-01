def add_product(product_name, price, quantity):
    return {
        'product_name': product_name,
        'price': price,
        'quantity': quantity
    }

def update_price(product, new_price):
    product['price'] = new_price
    return product

def update_quantity(product, quantity_change):
    product['quantity'] += quantity_change
    return product

# Example usage:
product = add_product('Laptop', 999.99, 10)
print("Product added:", product)

product = update_price(product, 899.99)
print("Updated price:", product)

product = update_quantity(product, -2)
print("Updated quantity:", product)
