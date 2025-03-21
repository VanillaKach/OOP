class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price  # Это вызовет сеттер price, который инициализирует __price
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

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """Создает новый продукт из переданного словаря данных."""
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
