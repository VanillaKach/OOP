import pytest

from unittest.mock import patch

from src.product import Product

from src.lawn_grass import LawnGrass
from src.exceptions import ZeroQuantityError


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

@classmethod
def new_product(cls, data: dict) -> "LawnGrass":
    required = {'name', 'description', 'price', 'quantity'}
    base = {k: v for k, v in data.items() if k in required}
    extra = {k: v for k, v in data.items() if k not in required}
    return cls(**base, **extra)

def test_new_product_with_extra_fields():
    data = {
        'name': 'Газон',
        'description': 'Мягкий',
        'price': 500,
        'quantity': 10,
        'country': 'Россия',
        'germination_period': '7 дней',
        'color': 'зелёный'
    }
    grass = LawnGrass.new_product(data)
    assert grass.color == 'зелёный'
    assert grass.country == 'Россия'

def test_product_addition_different_classes():
    product = Product("Товар", "Описание", 100, 1)
    grass = LawnGrass("Газон", "Зеленый", 500, 10, "Россия", "7 дней", "зеленый")
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        product + grass

def test_zero_quantity_product():
    with pytest.raises(ZeroQuantityError):
        Product("Invalid", "Desc", 100, 0)

def test_zero_quantity_error_message():
    try:
        Product("Invalid", "Desc", 100, 0)
    except ZeroQuantityError as e:
        assert str(e) == "Товар с нулевым количеством не может быть добавлен"
    else:
        pytest.fail("ZeroQuantityError not raised")
