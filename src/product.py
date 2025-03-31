from src.base_product import BaseProduct
from src.log_mixin import LogCreationMixin
from src.exceptions import ZeroQuantityError

class Product(LogCreationMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        try:
            if quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
            super().__init__(
                name=name, description=description, price=price, quantity=quantity
            )
            self.name = name
            self.description = description
            self._price = price
            self.quantity = quantity
            print("Товар успешно добавлен")
        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
            raise
        finally:
            print("Обработка добавления товара завершена")

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = new_price

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """
        Создает продукт из словаря. Для дочерних классов автоматически передает все дополнительные поля.
        """
        required_fields = ["name", "description", "price", "quantity"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")

        if data["price"] <= 0:
            raise ValueError("Цена должна быть положительной")

        return cls(**data)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(other) is not type(self):  # Строгая проверка на идентичность классов
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity


