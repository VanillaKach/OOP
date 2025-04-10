from typing import List, Optional

from src.base_entity import BaseEntity

from .product import Product  # Правильный относительный импорт


class Category(BaseEntity):
    category_count: int = 0  # Счетчик категорий
    product_count: int = 0  # Счетчик продуктов

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию и увеличивает счетчик продуктов."""
        print(f"Проверка типа продукта: {type(product)}")  # Отладочное сообщение
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты")
        self.__products.append(product)
        Category.product_count = len(self.__products)

    @property
    def products(self) -> List[Product]:
        """Возвращает список продуктов."""
        return self.__products

    def get_product_count(self) -> int:
        """Возвращает количество продуктов в категории."""
        return len(self.__products)

    def get_products(self) -> List[Product]:
        """Возвращает список продуктов (опционально, если нужно)."""
        return self.__products

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self) -> float:
        """Рассчитывает среднюю цену товаров в категории."""
        if not self.__products:
            return 0.0
        total = sum(product.price for product in self.__products)
        return total / len(self.__products)
