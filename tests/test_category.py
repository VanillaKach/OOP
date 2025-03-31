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

    assert category.product_count == 2
    assert category.get_products()[0].name == "Product 1"
    assert category.get_products()[1].name == "Product 2"


def test_category_count() -> None:
    category1 = Category("Category 1", "First category.")
    category2 = Category("Category 2", "Second category.")
    assert Category.category_count == 5  # Проверка общего количества категорий

def test_category_str() -> None:
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 5)
    category = Category("Test Category", "This is a test category.", [product1, product2])
    assert str(category) == "Test Category, количество продуктов: 15 шт."


@pytest.fixture(autouse=True)
def reset_counts():
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0

def test_category_count():
    Category("Cat1", "Desc1", [])
    Category("Cat2", "Desc2", [])
    assert Category.category_count == 2

def test_product_count():
    p1 = Product("P1", "Desc", 100, 5)
    p2 = Product("P2", "Desc", 200, 3)
    Category("Cat", "Desc", [p1, p2])
    assert Category.product_count == 2

def test_middle_price_with_products():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 5)
    category = Category("Test Category", "Description", [product1, product2])
    assert category.middle_price() == 150.0

def test_middle_price_empty_category():
    category = Category("Empty Category", "Description", [])
    assert category.middle_price() == 0.0

def test_middle_price():
    # Тест с товарами
    p1 = Product("P1", "Desc", 100, 5)
    p2 = Product("P2", "Desc", 200, 3)
    category = Category("Test", "Desc", [p1, p2])
    assert category.middle_price() == 150.0

    # Тест с одним товаром
    category = Category("Test", "Desc", [p1])
    assert category.middle_price() == 100.0

    # Тест пустой категории
    category = Category("Empty", "Desc", [])
    assert category.middle_price() == 0.0
