# Ten projekt został wykonany na zlecienie

Wymagania Python 3, random module, json module, csv module, pandas module, matplotlib, pdfkit

# Treść projektu:
Załóży, że chcemy zrobić badanie wagi pacjentów w całej Polsce. W celach badawczych pobieramy od uczestników projektu następujące dane: imię, nazwisko,
wiek, województwo zamieszkania, płeć, wzrost, waga. Dodatkowo każdy uczestnik projektu, w momencie przystąpienia do niego otrzymuje identyfikator -
6-cio cyfrowy unikatowy numer. Zbieranie danych sklada się z dwóch etapów. Etap pierwszy to dane osobowe i nadanie numeru identyfikacyjnego.
Dane te są dostęne w pliku CSV (uczestnicy.csv) o następującej strukturze:

imie, nazwisko, wiek, plec, wojewodztwo, identyfikator
"Jan", "Kowalski", 37, "m", "lubuskie", 134567
"Anna", "Nowak", 56, "k", "mazowieckie", 786543
(..)

Druga część to badanie pacjentów wykonywane na specjalnym oprogramowaniu (np. waga z zapisem danych na komputer). W wyniku tych badań mamy plik w formacie
json (pomiary.json) w postaci:
   [
     {'134567': {'wzrost': 182,
             'waga': 76
        }},
     {'786543': {'wzrost': 167,
                 'waga': 52
         }},
     {...}
   ]

Polem łączącym dane z obu plików jest identyfikator.

W projekcie należy wykonać następujące kroki:

1. Wygenerować co najmniej dla 200 osób plik uczestnicy.csv. Identyfikatory umuszą być unikatowe. Imiona, Nazwska i inne potrzebne dane wygenerować
losowo (np, z listy imion, nazwiski i województw). Zakładamy, że wiek uczestników jest w przedziale 18-80.
2. Wygenerować plik z losowymi pomiarami dla każdego uczestnika z pliku uczestnicy.csv. Przy generowaniu danych założyć, że dla mężczyzn wzrosty jest z
przedziału 168-192, a waga 58-140. W przypadku kobiet wzrost to liczba losowa z przedziału 156-178, a waga 42-110.
4. Dla każdego pacjenta obliczyć indeks BMI, oraz określić kategorię w której osoba się znajduje (niedowaga, waga prawidłowa, nadwaga, otyłość
kliniczna). Zrobić statystykę w poszczególnych grupach z podziałem na kobiety i mężczyzn.
5. Zrobić histogram BMI w podziale na kobiety i mężczyźni
6. Zrobić histogramu BMI w podziale na kobiety i mężczyźni w przedziałach wiekowych 18-35, 46-65, powyżej 65.
7. Znaleźć średni, maksymalny i mnimalny indeks BMI w grupie kobiet i mężczyzn.
8. Zrobić wykres średniego BMI (kobiety i mężczyźni) w poszczegóonych województwach.
9. Wyniki uzyskane w analizie umieścić w pliku pdf.<br><br>

### Aby funkcja html_to_pdf działa poprawnie należy pobrać ten program:<br>
https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf<br>
oraz podać do niego ścieżke w funkcji w zmiennej path_wkhtmltopdf
Jeśli coś pójdzie nie tak w tej funkcji, program nie wyrzuci błedu, jedynie komunikat.
