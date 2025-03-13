import pytest
from src.category import Category
from src.product import Product

# Тесты для класса Category
def test_category_creation() -> None:
    category = Category("Test Category", "This is a test category.")
    assert category.name == "Test Category"
    assert category.description == "This is a test category."
    assert category.product_count == 0


def test_add_product_to_category() -> None:
    category = Category("Test Category", "This is a test category.")
    product = Product("Test Product", "This is a test product.", 100.0, 10)
    category.add_product(product)

    assert category.product_count == 1
    assert category.get_products()[0].name == "Test Product"


def test_add_multiple_products() -> None:
    category = Category("Test Category", "This is a test category.")
    product1 = Product("Product 1", "First product.", 100.0, 10)
    product2 = Product("Product 2", "Second product.", 150.0, 5)

    category.add_product(product1)
    category.add_product(product2)

    assert category.product_count == 3
    assert category.get_products()[0].name == "Product 1"
    assert category.get_products()[1].name == "Product 2"


def test_category_count() -> None:
    category1 = Category("Category 1", "First category.")
    category2 = Category("Category 2", "Second category.")
    assert Category.category_count == 5  # Проверка общего количества категорий
