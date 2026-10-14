"""Monitor basenów.

Skrypt pobiera temperaturę wody z czujnika basenu i decyduje,
co zrobić: OK, PODGRZEJ, SCHLODZ albo ALARM.
"""
import requests

# Adres serwera z czujnikami (podany przez prowadzącego)
BASE_URL = "https://baseny-1031605285283.europe-central2.run.app"

# Normy temperatury wody w °C: nazwa basenu -> (minimum, maksimum)
NORMY = {
    "duzy": (26, 28),
    "jacuzzi": (36, 39),
    "zimny": (10, 15),
    "dzieciecy": (29, 31),
}

# O ile stopni można wyjść poza normę, zanim to jest już ALARM
TOLERANCJA = 3


def pobierz_temperature(nazwa):
    """Pobiera temperaturę basenu z serwera."""
    url = BASE_URL + "/basen?nazwa=" + nazwa
    odpowiedz = requests.get(url, timeout=5)
    dane = odpowiedz.json()
    return dane["temperatura"]


def decyzja(temperatura, norma_min, norma_max):
    """Zwraca akcję dla danej temperatury i normy."""
    if temperatura < norma_min - TOLERANCJA:
        return "ALARM"
    if temperatura > norma_max + TOLERANCJA:
        return "ALARM"
    if temperatura < norma_min:
        return "PODGRZEJ"
    if temperatura > norma_max:
        return "SCHLODZ"
    return "OK"


def sprawdz_basen(nazwa):
    """Sprawdza jeden basen i zwraca wynik jako słownik."""
    temperatura = pobierz_temperature(nazwa)
    norma_min, norma_max = NORMY[nazwa]
    akcja = decyzja(temperatura, norma_min, norma_max)
    return {"basen": nazwa, "temperatura_c": temperatura, "akcja": akcja}


if __name__ == "__main__":
    for nazwa in NORMY:
        print(sprawdz_basen(nazwa))
