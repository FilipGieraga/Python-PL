# Program Lotto symuluje kumulację lotto pozwalając użytkownikowi wybrać swoje numery, wygerować je automatycznie, sprawdzić ile liczb zostało trafione oraz losować automatycznie tak długo aż zostanie trafiona wybrana ilość liczb.

Wymagania: Python 3, random module

# Program:
- pozwala na wprowadzenie własnego losu, czyli 6 liczb całkowitych z
  przedziału od 1 do 49, bez powtórzeń
- pozwala wygenerować własny los autmatycznie
- losuje wyniki kumulacji
- sprawdza czy w naszym losie są jakieś trafienia i zlicza je
- pyta użytkownika jaką liczbę trafień chciałby uzyskać od 1 do 6
- losuje tak długo aż tafi określoną przez nas liczbę trafień, przy
  czym wynik kumulacji pozostaje niezmieniony
- wyniki kumulacji oraz naszych losów są posortowane rosnąco,
  aby łatwiej je odczytać

# Szczegółowy opis:
Program zaczyna od wywołania funkcji lotto(), pytając użytkownika czy chce wybrać swoje numery.
Jeśli tak, tworzy pusty zbiór (set()), który będzie przechowywał nasze wybrane liczby. Program
pozwala wprowadzać poszczególne elementy, sprawdzając przy tym czy liczby znajdują się w odpowiednim zakresie,
czy nie powtarzają się i czy są w ogóle liczbami całkowitymi.
Jeśli użytkownik nie zdecyduje się ich wprowadzić, zostaną wybrane automatycznie.
Następnie zostają wylosowane i wydrukowane wyniki kumulacji wraz z naszymi dla porównania i ilościa wspólnych trafień.
Program pyta użytkownika jaką ilość trafień chciałby uzyskać. Liczba jaką można tu wprowadzić zawiera się w
przedziale od 1 do 6, w innym wypadku program prosi o ponowny input.
Zostaje wykonana pętla while która działa tak długo, aż ilość automatycznie wygenerowanych trafień pokryje się
z wynikami kumulacji w stopniu jaki wcześniej został określony.
Program drukuje nam ile razy się zapętlił aby trafić podaną liczbę oraz pokazuje jakie liczby się pokryły
w przypadku losu oraz wyników kumulacji.
Na końcu wywołana jest funkcja choice która pozwala zacząć wszystko od nowa, bądź zakończyć program.
