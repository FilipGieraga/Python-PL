# Program Struktura korporacji:

Wymagania: Python 3, pandas module, xlsxwriter module

## Dokumentacja:
Program ten jest kontunuacją programu Struktura korporacji, w której wygenerowany został plik json przechowujący dane na temat wszystkich pracowników.
Dane te nie są w żaden sposób posortowane, dlatego w drugiej części dane są na początku zhierarchizowane. Dzięki temu CEO jest na samej górze, a zwykli
pracownicy na samym dole. Głównym trzonem tej części projektu jest funkcja **excel_firma**, która tworzy nam excel z naszymi danymi. Pierwszy rząd jest
zablokowany aby łatwiej można było odczytać dane. Wszystkie dane pracowników są w pierwszej zakładce. Żeby plik był przyjemniejszy dla oka, dodane są również
formatowania komórek tj. Płeć, Staż pracy(w dniach), Zarobki roczne i Zarobki miesięczne.
W zależności od płci komórki mają czerwone bądź niebieskie czcionki.<br>
Staż pracy(w dniach), Zarobki roczne i Zarobki miesięczne posiadają paski danych.<br>
<br>

W drugim arkuszu zawarte są statyski, które liczone są wewnątrz funkcji excel_firma za pomocą mniejszych wcześniej zdefiniowanych funkcji korzystających z
modułu pandas.
W arkuszu statystyka znajdziemy informacje tj.:
- Średnie zarobki na wszystkich stanowiskach
- Mediana zarobków na wszystkich stanowiskach
- Średni wiek pracowników na danym stanowisku
- Ilośc osób na danym stanowisku
- Ilośc osób w danym dziale
- Ilośc kobiet i mężczyzn w firmie
- Średnie zarobki kobiet i mężczyzn na najniższych stanowiskach

<br>
Stworzony zostaje również wykres kolunowy pokazujący średnią i medianę zarobków miesięcznych na każdym stanowisku.

## Program tak naprawdę wyświetla nam jedynie komunikat, że plik excel został zapisany w ścieżce w której się znajduje.
