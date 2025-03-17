from unittest.mock import patch

from src.product import Product


# Тесты для класса Product
def test_product_creation() -> None:
    product = Product("Test Product", "This is a test product.", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "This is a test product."
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_update() -> None:
    product = Product("Test Product", "This is a test product.", 100.0, 10)
    product.price = 120.0
    assert product.price == 120.0


def test_product_price_update_lower() -> None:
    product = Product("Test Product", "This is a test product.", 100.0, 10)

    with patch("builtins.input", return_value="y"):
        product.price = 80.0  # Понижение цены
    assert product.price == 80.0


def test_product_price_update_lower_cancel() -> None:
    product = Product("Test Product", "This is a test product.", 100.0, 10)

    with patch("builtins.input", return_value="n"):
        product.price = 80.0  # Понижение цены
    assert product.price == 80.0  # Цена не должна измениться

def test_product_str() -> None:
    product = Product("Test Product", "This is a test product.", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_product_addition() -> None:
    product1 = Product("Test Product 1", "Description 1", 100.0, 10)
    product2 = Product("Test Product 2", "Description 2", 200.0, 5)
    assert product1 + product2 == (100.0 * 10) + (200.0 * 5)  # 1000 + 1000 = 2000
