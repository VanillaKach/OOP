from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other):
        pass
