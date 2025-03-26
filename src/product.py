from src.base_product import BaseProduct
from src.log_mixin import LogCreationMixin


class Product(LogCreationMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(
            name=name, description=description, price=price, quantity=quantity
        )
        self.name = name  # Добавляем публичный атрибут
        self.description = description  # Добавляем публичный атрибут
        self._price = price
        self.quantity = quantity  # Добавляем публичный атрибут

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
        # Базовые поля, обязательные для всех продуктов
        required_fields = ["name", "description", "price", "quantity"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")

        # Для базового класса Product
        if cls == Product:
            return cls(
                name=data["name"],
                description=data["description"],
                price=data["price"],
                quantity=data["quantity"],
            )

        # Для дочерних классов передаем ВСЕ поля из data
        return cls(**data)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "BaseProduct") -> "Product":
        if not isinstance(other, Product):
            raise TypeError("Нельзя складывать товары разных классов")
        total_value = self.price * self.quantity + other.price * other.quantity
        return Product(
            name=f"Сумма {self.name} и {other.name}",
            description="",
            price=total_value / (self.quantity + other.quantity),
            quantity=self.quantity + other.quantity,
        )