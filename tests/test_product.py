import pytest
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

    with patch('builtins.input', return_value='y'):
        product.price = 80.0  # Понижение цены
    assert product.price == 80.0


def test_product_price_update_lower_cancel() -> None:
    product = Product("Test Product", "This is a test product.", 100.0, 10)

    with patch('builtins.input', return_value='n'):
        product.price = 80.0  # Понижение цены
    assert product.price == 80.0  # Цена не должна измениться
