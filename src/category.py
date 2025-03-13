import json
from typing import List, Optional
from .product import Product  # Правильный относительный импорт

class Category:
    category_count: int = 0  # Счетчик категорий
    product_count: int = 0    # Счетчик продуктов

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию и увеличивает счетчик продуктов."""
        print(f"Проверка типа продукта: {type(product)}")  # Отладочное сообщение
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только экземпляры класса Product или его наследников.")

    @property
    def products(self) -> List[Product]:  # Изменено на возвращение списка
        """Возвращает список продуктов."""
        return self.__products

    def get_product_count(self) -> int:
        """Возвращает количество продуктов в категории."""
        return len(self.__products)

    def get_products(self) -> List[Product]:
        """Возвращает список продуктов (опционально, если нужно)."""
        return self.__products


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
