from io import StringIO
import sys
from src.product import Product

def test_log_mixin_output():
    captured_output = StringIO()
    sys.stdout = captured_output
    Product("Test", "Desc", 100, 10)
    sys.stdout = sys.__stdout__
    assert "Создан объект: Product" in captured_output.getvalue()
