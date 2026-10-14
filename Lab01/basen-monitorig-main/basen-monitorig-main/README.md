# Testowanie automatyczne – Lab 1: monitor basenów

W kompleksie basenowym czujniki mierzą temperaturę wody. Skrypt `monitor.py`
pobiera odczyt z serwera i decyduje, co zrobić: `OK`, `PODGRZEJ`, `SCHLODZ`
albo `ALARM`. Twoje zadanie: **napisać testy automatyczne** do tego skryptu.

## Uruchomienie (ok. 2 minut)

Potrzebujesz Pythona 3.9 lub nowszego.

```bash
pip install -r requirements.txt
pytest
```

Jeśli komenda `pip` lub `pytest` nie działa (albo system zgłasza `externally-managed-environment`),
użyj wirtualnego środowiska:

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest
```

Powinieneś zobaczyć pięć zielonych testów.

Jeśli prowadzący poda inny adres serwera (np. awaryjny), zmień stałą `BASE_URL` na początku `monitor.py`.

Możesz też otworzyć repozytorium w GitHub Codespaces (przycisk **Code → Codespaces**),
wtedy nie musisz nic instalować.

Możesz też zobaczyć odpowiedź skryptu dla wszystkich basenów:

```bash
python monitor.py
```

## Zadanie

1. Przeczytaj `monitor.py` i zrozum, jak działa decyzja o akcji.
2. Otwórz `tests/test_basen.py`. Są tam gotowe testy: dla basenu dużego i dziecięcego oraz trzy testy funkcji `decyzja()`
   (norma 26–28 °C).
3. **Dopisz analogiczne testy** dla pozostałych basenów: `jacuzzi` i `zimny`.
   Jacuzzi ma w normalnych warunkach akcję `OK`.
   Zimny basen jest za ciepły (norma 10–15 °C), więc ma być schłodzony: akcja `SCHLODZ`.
4. Uruchom `pytest`. Wszystkie testy mają być zielone. Zgłoś się do prowadzącego.

## Zadanie dodatkowe

Dopisz testy funkcji `decyzja()` dla wartości brzegowych: dokładnie na granicy normy
(26 i 28) i na granicy tolerancji (23 i 31) oraz tuż za nią. Co zwraca funkcja?
Czy to zgadza się z tym, co byś oczekiwał?

## Wskazówki

- Użyj nazwy testu opisującej, co sprawdza (`test_jacuzzi_jest_w_normie`).
- Możesz poprosić AI o pomoc, ale **przeczytaj i zrozum** każdy wygenerowany test.
  Zastanów się, co on naprawdę sprawdza.
