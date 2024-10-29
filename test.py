# Pusta lista słów
slowa = []

# Startowy indeks dla najwyższego okna
start_index = 0  # Początkowy indeks, z którego zaczynamy wyświetlanie

def wyswietl_okna():
    """Wyświetla słowa w trzech oknach, jeśli są dostępne przynajmniej trzy słowa."""
    if len(slowa) < 3:
        print("\nDodaj przynajmniej trzy słowa, aby wyświetlić okna.")
        return
    
    print("\nAktualny widok okien:")
    print("Okno 1:", slowa[start_index] if start_index < len(slowa) else "...")
    print("Okno 2:", slowa[start_index + 1] if start_index + 1 < len(slowa) else "...")
    print("Okno 3:", slowa[start_index + 2] if start_index + 2 < len(slowa) else "...")

def dodaj_slowo(nowe_slowo):
    """Dodaje nowe słowo w środkowym oknie, przesuwając pozostałe."""
    global slowa, start_index

    # Wstawiamy nowe słowo w miejsce środkowe
    slowa.insert(start_index + 1, nowe_slowo)

    # Upewniamy się, że lista nie przekracza 5 elementów
    if len(slowa) > 5:
        slowa.pop()
    
    wyswietl_okna()

def przesun_w_gore():
    """Przesuwa widok w górę, jeśli możliwe."""
    global start_index
    if start_index > 0:
        start_index -= 1
    wyswietl_okna()

def przesun_w_dol():
    """Przesuwa widok w dół, jeśli możliwe."""
    global start_index
    if start_index < len(slowa) - 3:  # Zmienione na len(slowa) - 3, by nie przekraczać listy
        start_index += 1
    wyswietl_okna()

# Początkowy widok (lista pusta)
wyswietl_okna()

# Interfejs użytkownika
while True:
    print("\nOpcje:")
    print("1 - Dodaj nowe słowo")
    print("2 - Przesuń widok w górę")
    print("3 - Przesuń widok w dół")
    print("4 - Zakończ program")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        nowe_slowo = input("Podaj nowe słowo do dodania: ")
        dodaj_slowo(nowe_slowo)
    elif wybor == "2":
        przesun_w_gore()
    elif wybor == "3":
        przesun_w_dol()
    elif wybor == "4":
        print("Zakończono program.")
        break
    else:
        print("Niepoprawny wybór, spróbuj ponownie.")
