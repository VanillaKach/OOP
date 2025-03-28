from typing import Any


class LogCreationMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(f"Создан объект {self.__class__.__name__} с параметрами:")
        for k, v in kwargs.items():
            print(f"  {k}: {v}")
        super().__init__(*args, **kwargs)
