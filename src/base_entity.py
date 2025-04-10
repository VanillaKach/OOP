from abc import ABC, abstractmethod


class BaseEntity(ABC):
    @abstractmethod
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def __str__(self) -> str:
        pass
