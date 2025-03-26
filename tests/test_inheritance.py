from src.smartphone import Smartphone

class TestSmartphone:
    @classmethod
    def new_product(cls, data: dict) -> "Smartphone":
        required = {'name', 'description', 'price', 'quantity'}
        base = {k: v for k, v in data.items() if k in required}
        extra = {k: v for k, v in data.items() if k not in required}
        return cls(**base, **extra)  # Передаём все параметры

    def test_new_smartphone(self):
        data = {
            'name': 'iPhone',
            'description': '...',
            'price': 100000,
            'quantity': 2,
            'efficiency': 95.5,
            'model': '15 Pro',
            'memory': 256,
            'color': 'black'
        }
        phone = Smartphone.new_product(data)
        assert phone.memory == 256
        assert phone.model == '15 Pro'
