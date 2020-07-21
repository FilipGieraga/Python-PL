# Program do rozwiązywania prostych sudoku

Wymagania: Python 3, numpy module

# Funkcja sudoku_examples()
Wyświetla nam przykładowe sudoku, których jest pięć i pozwala wybrać które z nich ma być rozwiązane za pomocą kolejnej funkcji solve().
Program niestety nie jest idealny i rozwiązuje je jedynie takim sposobem jaki jest mi znany. Jedno z tych przykładowych sudoku jest
częsciowo wypełnione aby mogło się rozwiązać, a jedno pokazuje problem całego algorytmu, który stworzyłem, bez szukania gotowych odpowiedzi.
Pozostałe 3 to czyste szablony ze stron internetowych wypełniające się bez dodatkowych warunków

# Funkcja solve()
Po wybraniu konkretnego sudoku program przechodzi do poszukiwania rozwiązania i wykonuje się albo dopóki w sudoku znikną wszystkie zera, albo zostanie wykonane
15 iteracji. Na początku stworzona jest lista możliwych liczb do wpisania w nasze sudoku, czyli liczby od 1 do 9. Zostaje również zadeklarowany pusty słownik.
Funkcja iteruje przez każdy niezerowy element w sudoku i jest podzielona na odpowiednie kwadraty takie jak te występujące w sudoku. Wypełnione już pola
zostają nienaruszone. Dla każdego niezerowego pola w sudoku stworzona jest pusta lista solutions, która przechowuje rozwiązania dla konkretnych współrzędnych.
Aby rozwiązanie znalazło się w liście solutions musi spełniać trzy warunki:<br>
brak danej liczby w pionie, poziomie i danym kwadracie<br>
Warunek ten jest sprawdzany dla wszystkich liczb możliwych do wpisania od 1 do 9.
Dla każdego niezerowego elementu wspólrzędne oraz rozwiązania są zapisane w zadeklarowanym słowniku w przykładowej postaci ...,(3, 2): [7, 8], (3, 6): [8],...
Widzimy tutaj, że element o wsp. 3,2 posiada dwa rozwiązania i w tej iteracji pętli nie zostanie wpisany do sudoku, natomiast wsp 3,6 mają tylko jedno rozwiązanie
czyli 8 i znajdzie się ono w tej iteracji pętli w sudoku.
Jeżeli dany element ma tylko jedno rozwiązanie zostaje ono wpisane do sudoku, ponieważ nie ma wtedy wątpliowści, że musi się ono tam znaleźć.
Program przy każdej swojej iteracji tylko częściowo wypełnia sudoku, jedynie tam gdzie jest tego pewien. Pod koniec każdej iteracji, pokazuje nam:<br>
słownik współrzędnych i rozwiązań dla danej iteracji<br>wyświetla które to podejście <br>liczbę wstawień do sudoku.
Niestety sudoku nie jest takie proste, że wystarczy jedynie sprawdzić pion, poziom i kwadrat. Są sudoku które dla każdego niezerowego elementu,
posiadają wiele rozwiązań i tak jest np. z sudoku nr 3 gdzie program już przy pierwszej iteracji nie może nic wstawić dlatego zapętla się 15 razy i kończy.



