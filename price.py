# models/price.py

from datetime import datetime

print("Ładowanie modułu Price")  # Ta linia powinna się wyświetlić, gdy moduł zostanie załadowany

class Price:
    def __init__(self, user_id, price, timestamp=None):
        self.user_id = user_id
        self.price = price
        self.timestamp = timestamp or datetime.now()
