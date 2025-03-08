from typing import Generator

import pytest

from src.class_for_prod import Category, Product


@pytest.fixture(autouse=True)
def reset_category_count() -> Generator[None, None, None]:
    """Сбрасывает количество категорий перед каждым тестом."""
    Category.category_count = 0
    yield
    Category.category_count = 0  # Сбрасываем после теста


@pytest.fixture
def sample_product() -> Product:
    """Создает тестовый продукт."""
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def sample_category(sample_product: Product) -> Category:
    """Создает тестовую категорию с продуктом."""
    return Category(
        "Смартфоны", "Смартфоны, как средство не только коммуникации", [sample_product]
    )


def test_product_initialization(sample_product: Product) -> None:
    """Тестирует инициализацию объекта Product."""
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_category_initialization(sample_category: Category) -> None:
    """Тестирует инициализацию объекта Category."""
    assert sample_category.name == "Смартфоны"
    assert (
        sample_category.description == "Смартфоны, как средство не только коммуникации"
    )
    assert len(sample_category.products) == 1
    assert sample_category.products[0].name == "Samsung Galaxy S23 Ultra"


def test_product_count() -> None:
    """Тестирует подсчет количества продуктов в категории."""
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны", "Описание категории", [product1, product2, product3]
    )

    assert category.product_count == 3


def test_category_count() -> None:
    """Тестирует общее количество категорий."""
    Category("Смартфоны", "Описание категории 1", [])
    Category("Телевизоры", "Описание категории 2", [])

    assert Category.category_count == 2


if __name__ == "__main__":
    pytest.main()
