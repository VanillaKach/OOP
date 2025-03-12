from typing import List, Optional

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для атрибута цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для атрибута цены с проверкой."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная.")

    @staticmethod
    def new_product(data: dict) -> 'Product':
        """Создает новый продукт из переданного словаря данных."""
        return Product(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"]
        )

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только экземпляры класса Product или его наследников.")

    @property
    def products(self) -> str:
        """Возвращает список продуктов в виде строки."""
        return "\n".join(str(product) for product in self.__products)

    def get_product_count(self) -> int:
        """Возвращает количество продуктов в категории."""
        return len(self.__products)

    def get_products(self) -> List[Product]:
        """Возвращает список продуктов (опционально, если нужно)."""
        return self.__products
