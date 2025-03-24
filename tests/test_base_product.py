import pytest
from src.base_product import BaseProduct
from src.product import Product

def test_base_product_abstract_methods():
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100, 10)

def test_product_inheritance():
    product = Product("Test", "Desc", 100, 10)
    assert issubclass(Product, BaseProduct)  # Проверяем наследование
    assert isinstance(product, BaseProduct)  # Теперь должно работать
