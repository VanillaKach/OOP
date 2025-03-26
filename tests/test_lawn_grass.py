from src.lawn_grass import LawnGrass

def test_lawn_grass_creation():
    grass = LawnGrass(
        "Elite Grass", "Premium quality", 500.0, 10, "USA", "14 days", "Green"
    )
    assert grass.country == "USA"
    assert grass.germination_period == "14 days"

def test_lawn_grass_addition():
    grass1 = LawnGrass("Grass1", "Desc", 300.0, 5, "Russia", "7 days", "Green")
    grass2 = LawnGrass("Grass2", "Desc", 400.0, 3, "USA", "10 days", "Dark Green")
    assert grass1 + grass2 == (300.0 * 5) + (400.0 * 3)  # 1500 + 1200 = 2700

def test_lawn_grass_addition_same_type():
    grass1 = LawnGrass("G1", "Desc", 300, 5, "RU", "7d", "Green")
    grass2 = LawnGrass("G2", "Desc", 400, 3, "US", "10d", "Blue")
    assert grass1 + grass2 == 300*5 + 400*3
