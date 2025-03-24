from src.base_entity import BaseEntity
from src.product import Product

class Order(BaseEntity):
    def __init__(self, product: Product, quantity: int):
        super().__init__(f"Заказ на {product.name}")
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} шт., Итого: {self.total_price} руб."
