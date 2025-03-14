from product import Product

def test_product():
    product = Product("Test Product", "Test Description", 100, 10)
    print(f"Тип продукта: {type(product)}")  # Должно вывести: <class 'product.Product'>
    print(product)

if __name__ == "__main__":
    test_product()
