# models/player.py

print("Ładowanie modułu Player")  # Ta linia powinna się wyświetlić, gdy moduł zostanie załadowany

class Player:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
