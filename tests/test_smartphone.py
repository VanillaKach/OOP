from src.smartphone import Smartphone

def test_smartphone_creation():
    phone = Smartphone(
        "iPhone 15", "512GB, Gray", 210000.0, 8, 95.5, "15 Pro", 512, "Gray"
    )
    assert phone.name == "iPhone 15"
    assert phone.memory == 512
    assert phone.color == "Gray"

def test_smartphone_addition():
    phone1 = Smartphone("Phone1", "Desc", 1000.0, 2, 90.0, "X", 128, "Black")
    phone2 = Smartphone("Phone2", "Desc", 2000.0, 3, 95.0, "Y", 256, "White")
    assert phone1 + phone2 == (1000.0 * 2) + (2000.0 * 3)  # 2000 + 6000 = 8000
    