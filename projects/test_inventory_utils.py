import pytest
from inventory_utils_mutated import calculate_sales_tax, check_stock_level, calculate_discount

def test_calculate_sales_tax():
    assert calculate_sales_tax(100, 10) == 10
    assert calculate_sales_tax(200, 5) == 10


def test_check_stock_level():
    assert check_stock_level(0) == "Low"
    assert check_stock_level(10) == "OK"
    with pytest.raises(ValueError):
        check_stock_level(-1)


def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(200, 50) == 100
    with pytest.raises(ValueError):
        calculate_discount(100, -5)
