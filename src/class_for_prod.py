import json
from typing import List


class Product:
    """Класс для представления продукта."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории продуктов."""

    category_count = 0
    total_product_count = 0  # Переименовываем для избежания конфликта с методом

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.total_product_count += len(products)  # Используем новый атрибут

    @property
    def product_count(self) -> int:
        """Возвращает количество продуктов в категории."""
        return len(self.products)


def load_data_from_json(file_path: str) -> List[Category]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = [
            Product(
                name=product["name"],
                description=product["description"],
                price=product["price"],
                quantity=product["quantity"],
            )
            for product in category_data["products"]
        ]
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories
