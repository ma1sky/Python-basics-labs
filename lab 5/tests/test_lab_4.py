import pytest
from classProduct import product
from classVehicle import vehicle
from classPhone import phone

# Тесты для класса Product
def test_product_init():
    prod = product("Product", 10)
    assert prod.name == "Product"
    assert prod.price == 10

def test_product_invalid_price():
    with pytest.raises(TypeError):
        product("Invalid", -5)

def test_vehicle_init():
    veh = vehicle("Car", 5000, 1500)
    assert veh.name == "Car"
    assert veh.price == 5000
    assert veh.weight == 1500

def test_vehicle_invalid_weight():
    with pytest.raises(TypeError):
        vehicle("Invalid", 2000, "InvalidWeight")

def test_phone_init():
    ph = phone("Smartphone", 800, "ModelX")
    assert ph.name == "Smartphone"
    assert ph.price == 800
    assert ph.model == "ModelX"

def test_phone_invalid_model():
    with pytest.raises(TypeError):
        phone("InvalidPhone", 1000, 12345)