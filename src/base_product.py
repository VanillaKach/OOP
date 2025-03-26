from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> "BaseProduct":
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
