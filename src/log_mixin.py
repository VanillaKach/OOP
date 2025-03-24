class LogCreationMixin:
    def __init__(self, **kwargs):
        print(f"Создан объект: {self.__class__.__name__}({kwargs})")
        super().__init__(**kwargs)  # Важно вызывать super() после вывода
