import json
import os
import pytest
from typing import List, Dict, Any
from src.utils import load_data_from_json
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_json_file(tmp_path: pytest.TempPathFactory) -> str:
    """Создает временный JSON файл для тестирования."""
    data: List[Dict[str, Any]] = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации.",
            "products": [
                {
                    "name": "Samsung Galaxy S23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                }
            ]
        },
        {
            "name": "Планшеты",
            "description": "Планшеты для работы и отдыха.",
            "products": [
                {
                    "name": "iPad Pro",
                    "description": "12.9 дюймов, 128GB",
                    "price": 100000.0,
                    "quantity": 10
                }
            ]
        }
    ]

    file_path = tmp_path / "test_data.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return str(file_path)


def test_load_data_from_json(sample_json_file: str) -> None:
    """Тестирует функцию загрузки данных из JSON файла."""
    categories: List[Category] = load_data_from_json(sample_json_file)

    assert len(categories) == 2  # Должно быть 2 категории

    # Проверяем первую категорию
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == "Смартфоны, как средство не только коммуникации."
    assert len(categories[0].products) == 2  # Должно быть 2 продукта в первой категории

    # Проверяем первый продукт в первой категории
    product1: Product = categories[0].products[0]
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    # Проверяем второй продукт в первой категории
    product2: Product = categories[0].products[1]
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8

    # Проверяем вторую категорию
    assert categories[1].name == "Планшеты"
    assert categories[1].description == "Планшеты для работы и отдыха."
    assert len(categories[1].products) == 1  # Должно быть 1 продукт в второй категории

    # Проверяем продукт во второй категории
    product3: Product = categories[1].products[0]
    assert product3.name == "iPad Pro"
    assert product3.description == "12.9 дюймов, 128GB"
    assert product3.price == 100000.0
    assert product3.quantity == 10
