from app.app import get_status
import time

def test_order_placed():
    order_time = time.time()
    assert get_status(order_time) == "Order Placed"

def test_shipped():
    order_time = time.time() - 80
    assert get_status(order_time) == "Shipped"

def test_delivered():
    order_time = time.time() - 500
    assert get_status(order_time) == "Delivered"