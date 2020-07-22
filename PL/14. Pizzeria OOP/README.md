# Program Pizzeria opiera się na programowaniu obiektowym i symyluje pizzerię

Wymagania: Python 3

# Klasa Pizza():
Każda instancja klasy Pizza, która zostanie zadeklarowana wymaga 4 parametrów do wprowadzenia tj. nazwa, składniki, rozmiar i cena.<br>
Przykładowa pizza dodana w tej klasie:<br>
Wege=Pizza("Wege",("pieczarki","papryka","kukurydza","groszek"),Pizza.rozmiar[0],20)<br>
Pizze deklarujemy z rozmiarem najmniejszym, czyli 28 cm oraz odpowiadającą mu ceną. Nazwa zmiennej powinna odzwierciedlać nazwę pizzy.
Składniki możemy deklarować słownie bądź jako indeksy listy zadeklarowanej w klasie jako Pizza.składniki.
Podczas deklarowania pizzy w tle zostaje zainkrementowana ilosc_pozycji, żeby można było stwierdzić ile mamy instancji klas(czyli naszych pizz).
Nazwa zmiennej zostaje przechowana w liście menu, która może zostać później wykorzystana w metodzie klasy wyswietl_menu().
Podczas deklarowania każdej instancji klasy są również sprawdzane składniki w pizzy. Nie możemy stworzyć instancji klasy, w której
składnik nie istnieje na naszej liście zadekladowanej wewnątrz klasy.

Kiedy nasze instancje są już zadeklarowane, możemy każdą z nich wyświetlić w sposób czytelny dzięki metodzie __repr__
Za pomocą funkcji klasy Pizza.wyswietl_menu() możemy wyświetlić menu, które składa się ze wszystkich stworzonych pizz.
Za pomocą statycznej metody Pizza.godziny_otwarcia() możemy zobaczyć, kiedy pizzeria jest otwarta.
Metoda cena rozmiaru podaje nam ceny rozmiarów poszczególnych pizz licząc ją poprzez pomnnożenie rozmiaru przez wskaźnik
W przypadku rozmiaru 1, czyli najmniejszego mnożenie nie zostaje wykonane.
W przypadku rozmiaru 2, wskaźnik to 1.4, a przy trójce, wskaźnik to 2.
Aby wyświetlić cenę największego rozmiaru Capricciosy, wystarczy wpisać: print(Capricciosa.cena_rozmiaru(3))
Pizza.ilosc_pozycji wyświetli nam ile jest instancji w klasie
Dwie najważniejsze metody w tej klasie to: self.zamow() i Pizza.zrob_to_sam()




# Metoda Pizza.zrob_to_sam():
Ta metoda nie odnosi się do instancji klasy i pozwala nam stworzyć własną pizze ze składników zadeklarowanych w klasie.
Na początku musimy określić ile chcemy składników w naszej pizzy, od 1 do 4.
Składniki z naszej listy Pizza.składniki zostają nam wyświetlone oraz ponumerowane od jedynki. My jedynie wybieramy sobie numery składników, jakie
chcemy. Na koniec zostajemy tylko zapytani o rozmiar. Po wprowadzeniu tych danych program wyświetla nam cenę ,składniki i rozmiar.


# Metoda self.zamow():
Ta metoda zakłada, że chcemy konkrętną pizzę z menu.   Self to odniesienie do jej instancji np. Margerita.zamow() pozwoli na zamówienie tej konkretnej
instancji klasy.Na początku program pyta o rozmiar od 1 do 3. Następnie pyta czy chcemy dokonać zmian w pizzy.
Jeśli tak, mamy możliwość dodania, odjęcia, zamienienia składnika oraz zakończenia dokonywania zmian.
Przy wszystkich tych operacjach cena zostaje dostosowana do zmian, uwzgledniając przy tym czy dany składnik jest mięsem.<br>
Jeśli odejmiemy zwykły składnik -2 zł, mięso -3 zł<br>
Jeśli dodamy zwykły składnik +2 zł, mięso +3 zł<br>
Przy zamianie uwzględniane jest co zamieniamy na co i ceny są takie same, tzn. odjecie miesa dodanie zw. skladnika -3 +2 czyli cena będzie o złotówkę mniejsza.<br>
Potem program prosi nas o podanie adresu i nr telefonu. Na koniec metoda wyświetla że zamówienie zostało złożone na konkretny adres i nr. telefonu, cenę,
rozmiar oraz jaką pizze otrzymamy.
