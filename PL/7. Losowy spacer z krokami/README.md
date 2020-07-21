# Program random walk with steps składa się z kilku funkcji które są powiązane z koncepcją losowego spaceru. Zainspirowany kanałem Socratica na YT

Wymagania: Python 3, random module, turtle module

# Random_walk(n):
Funkcja random_walk(n) jest trzonem programu i pobiera od użytkownika jedynie liczbę kroków jakie ma wykonać program.
Po wykonaniu tych kroków zwraca nam współrzędne x i y oraz wartość bezwzględną przebytej ścieżki.

# max_min_steps(number_of_walks,steps_taken):
Funkcja max_min_steps(number_of_walks,steps_taken) wykonuje symulację spaceru ze stałą liczbą kroków
podaną ilość razy. Dystanse poszczególnych spacerów przechowane są w zmiennej distances_walked, która jest setem.
Program zwraca nam minimalną i maksymalną wartość bezwględną przebytego dystansu dla podanej ilości spacerów.



# walk_loop(number_of_walks,walk_lengths_range,distance_limit):
Funckja walk_loop(number_of_walks,walk_lengths_range,distance_limit) determinuje jak często potrzebny byłby
transport do domu taksówką ze spaceru. Będzię on potrzebny zawsze kiedy przebyty dystans bezwględny jest
dłuższy niż zmienna distance_limit.
W tej funkcji mamy również zmienną number_of_walks, która determinuje ile razy zostaną wykonane spacery
dla pojedyńczej długości spaceru.
Zmienna walk_lengths_range to zakres długości naszych spacerów od jednego do długości podanej.<br>
Przykład:<br>
number_of_walks=1000<br>
walk_lengths_range=100<br>
distance_limit=10<br>
Dla każdej długości spacerów od 1 do 100 kroków symulacja spacerów zostanie wykonana 1000 razy. Jeżeli bezwględny
dystans od domu będzie krótszy lub równy 10, zainkrementowana zostanie zmienna no_transport, której początkowa
wartość dla każdej długości spaceru jest równa zero. Po ostatnim wykonanym spacerze dla konkretnej ilości
kroków, podana nam zostanie procentowo ilość spacerów z których nie potrzebujemy taksówki dla konkretnej liczby kroków.


# draw_random_walk(n,forward,pointer,speed):
Funkcja draw_random_walk(n,forward,pointer,speed) jest moją ulubioną w tym programie i rysuje nam losowy spacer w
oparciu o przyjęte parametry.
n- to ilość kroków jaka ma zostać narysowana
forward- to długość pojedyńczego kroku w pixelach
pointer- to wielkość kropki jaka jest stawiana na początku(czerwona) i końcu(niebieska) w pixelach
speed- szybkość rysowania spaceru

## Disclaimer:
Wszystkie funkcje są zahaszowane, żeby je uruchomić należy usunąć # w odpowiednim miejscu
