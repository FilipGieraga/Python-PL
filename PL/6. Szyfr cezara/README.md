# Program funkcja kwadratowa to program którego celem jest policzenie delty oraz określenie miejsc zerowych jeśli takie istnieją.

Wymagania Python 3, math module

# Program:
- sprawdza czy funckja jest kwadratowa
- w przypadku funkcji liniowej podaje punkt przecięcia
- wylicza deltę funcji kwadratowej
- liczy wierzchołek
- bierze input ktory jest wlasciwy czyli liczbowy, w innym wypadku prosi o podanie właściwych parametrów
- liczy i podaje ilosc miejsc zerowych(jesli są) na podstawie delty
- wyznacza miejsca zerowe

# Szczegółowy opis:
Na początku zostaje wywołana funcja parameters(), która pobiera od użytkownika wartości 3 parametrów a,b,c.
Jeśli którykolwiek parametr zostanie źle wprowadzony, trzeba zacząć wprowadzanie od nowa.
Prawidłowymi parametrami są liczby całkowite oraz dziesiętne.
Następnie program sprawdza czy wartość parametru a jest zerowa, jeśli tak to liczy miejsce zerowe dla
funkcji liniowej i drukuje rezultat, wywołując przy tym funkcję choice().
Jeśli nie to liczy delte oraz wywołuje funkcje m_zerowe(), której przekazuje listę parametrów a,b,c oraz wynik delty.
W funkcji m_zerowe() ostatni parametr z przekazanej listy zostaje przypisany zmiennej delta, sprawdzamy czy delta
jest większa od zera, jeśli nie jest, nie da się wyciągnąć z niej pierwiastka. Da się natomiast zawsze policzyć wierzchołek
paraboli i jest to robione w następnym kroku.
Następnie jeśli delta mniejsza od zera, drukujemy brak miejsc zerowych, jesli równa zero mamy jedno miejsce zerowe, które
jest policzone ze wzoru, zaokrąglone do 2 miejsc po przecinku i wydrukowane.
Jeśli większa od zera liczone są dwa miejsca zerowe, są również zaokrąglone i wydrukowane.
Na końcu po wydrukowaniu wyników jest wywoałana funkcja choice(), która pozwala ponownie wywołać funkcję paramaters()
i zacząć liczenie od nowa, bądź zakończyć program.
