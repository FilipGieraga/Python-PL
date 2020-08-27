import random
import turtle


def losowy_spacer(n):
    x = 0
    y = 0
    for i in range(n):
        krok = random.choice(["N", "S", "E", "W"])
        if krok == "N":
            y = y + 1
        elif krok == "S":
            y = y - 1
        elif krok == "E":
            x = x + 1
        else:
            x = x - 1
    return x, y


def max_min_kroki(liczba_spacerow, postawione_kroki):
    """Wykonuje określoną liczbę spacerów z określonymą ilością kroków i zwraca najdłuższy i najkrótszy spacer"""
    przebyty_dystans = set()
    for i in range(liczba_spacerow):
        spacer = losowy_spacer(postawione_kroki)
        print(f"Obserwacja: {i + 1}, Współrzędne: {spacer}, Odległość od domu: {abs(spacer[0]) + abs(spacer[1])}")
        distance_walked = abs(spacer[0]) + abs(spacer[1])
        przebyty_dystans.add(distance_walked)
    print(f"Minimalny bezwględny przebyty dystans:{min(przebyty_dystans)}")
    print(f"Maksymalny bezwględny przebyty dystans:{max(przebyty_dystans)}")


def petla_spacerow(liczba_spacerow, zakres_dlugosci_spacerow, limit_dystansu):
    """Determinuje jak często potrzebny będzie transport ze spaceru,
    będzie potrzebny zawsze gdy absolutna długość spaceru jest większa od limit_dystansu"""
    for walk_length in range(1, zakres_dlugosci_spacerow + 1):
        brak_transportu = 0
        for i in range(liczba_spacerow):
            (x, y) = losowy_spacer(walk_length)
            dystans = abs(x) + abs(y)
            if dystans <= limit_dystansu:
                brak_transportu += 1
        procentowy_brak_transportu = float(brak_transportu) / liczba_spacerow
        print(f"Ilość kroków = {walk_length}, % wartość braku transportu = {100 * procentowy_brak_transportu}")


def rysuj_losowy_spacer(n, forward, pointer, speed):
    """Rysuje losowy spacer"""
    make = turtle.Turtle()
    x = 0
    y = 0
    make.dot(pointer, 'red')
    make.speed(speed)
    for i in range(n):
        step = random.choice(["N", "S", "E", "W"])
        if step == "N":
            y = y + 1
            make.setheading(90)  # UP
            make.forward(forward)
        elif step == "S":
            y = y - 1
            make.setheading(270)  # DOWN
            make.forward(forward)
        elif step == "E":
            x = x + 1
            make.setheading(0)  # RIGHT
            make.forward(forward)
        else:
            x = x - 1
            make.setheading(180)  # LEFT
            make.forward(forward)
    make.dot(pointer, 'blue')
    make.end_fill()
    turtle.done()
    print(f"({x},{y}), Odległość od domu: {abs(x) + abs(y)}")
    return x, y


#####--------- rysuj_losowy_spacer(kroki,dlugosc linii, wielkosc kropki na poczatku i koncu ,szybkosc rysowania)
# Funkcja do rysowania losowego spaceru ponizej:
# rysuj_losowy_spacer(100,50,5,6)


# liczba_spacerow = 1000
# dla kazdego spaceru w zakresie dlugosci spacerow, liczba spacerow zostanie wykonana
# zakres_dlugosci_spacerow = 100
# zaczyna sie od jednego i konczy na okreslonej dlugosci
# limit_dystansu = 10
# jesli dystans na koniec spaceru jest dluzszy niz limit_dystansu, porzebny jest transport spowrotem
#####--------- petla_spacerow(liczba_spacerow, zakres_dlugosci_spacerow, limit_dystansu):
# petla_spacerow(1000,100,10)


#####--------- x,y=losowy_spacer(kroki)
# x,y =losowy_spacer(1000)
# print(f"({x},{y}), Bezwzględny dystans od domu: {abs(x) + abs(y)}")


#####--------- max_min_kroki(liczba_spacerow,postawione_kroki)
# max_min_kroki(100,100000)
