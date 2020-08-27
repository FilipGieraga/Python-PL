def wisielec():
    print("Hasło powinno być jednym wyrazem.")
    string = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźżaąbc"

    while True:
        try:
            haslo = input("Podaj haslo do zgadniecia:\n")
            haslo = haslo.upper()
            x = haslo.split()
            y = [l for l in haslo]
            if len(x) > 1:
                raise TypeError("Hasło jest dłuższe niż jeden wyraz.")
            if len(haslo) == 0:
                raise ValueError("Nie podałeś hasła.")
            for i in y:
                if i not in string.upper():
                    raise ValueError(f"Hasło posiada niedozwolone znaki.\nLista dozwolonych znaków: {string}")
        except Exception as error:
            print(f"Wystąpił bład: {error}\nSpróbuj ponownie.")
        else:
            break

    print(f"Twoje hasło to : {haslo}")
    zaszyfrowane_lista = ["_" for l in haslo]
    zaszyfrowane_string = ' '.join([str(elem) for elem in zaszyfrowane_lista])
    for i in range(20):
        print("\n")
    print(f"Hasło składa się z {len(haslo)} liter")
    print("Wielkość liter nie ma znaczenia")
    print(zaszyfrowane_string)
    uzyte_litery = set()

    l_podejsc = 10

    while "_" in zaszyfrowane_string:
        litera = input("Podaj litere lub całe hasło:\n")
        pozycja = []
        if len(litera) > 1:
            if litera.upper() == haslo.upper():
                print("Brawo, hasło znalezione :)")
                break
            else:
                print(f"To nie było hasło, próbuj dalej {zaszyfrowane_string}")
                l_podejsc -= 1
                print(f"Pozostało podejść: {l_podejsc}")
        elif litera.upper() in uzyte_litery or len(litera) == 0 or litera.upper() not in string.upper():
            print("Użyłeś spacji, niedozwolonego znaku, bądź litery, której już próbowałeś.")
        elif litera.upper() in haslo:
            print(f"Litera {litera.upper()} jest w haśle!")
            pozycja = [index for index, x in enumerate(haslo) if x == litera.upper()]
            for i in pozycja:
                zaszyfrowane_lista[i] = litera.upper()
                zaszyfrowane_string = ' '.join([str(elem) for elem in zaszyfrowane_lista])
            print(zaszyfrowane_string)
        else:
            print("Brak litery w haśle!!")
            uzyte_litery.add(litera.upper())
            l_podejsc -= 1
            print(f"Próbuj dalej : {zaszyfrowane_string}")
            print(f"Pozostało podejść: {l_podejsc}. Uzyte nietrafione litery sa nastepujące:{uzyte_litery}")

        if l_podejsc == 0 and "_" in zaszyfrowane_string:
            print(f"Niestety przegrałeś. Hasłem było : {haslo}")
            break
    else:
        print("Brawo, hasło znalezione :)")
    wybor()


def wybor():
    decyzja = input("Czy chcesz spróbować jeszcze raz?(t/n)\n")
    if decyzja == "t":
        wisielec()
    elif decyzja == "n":
        print("Dziękuje za skorzystanie z programu.")
    else:
        print(f"Jestem tylko komputerem i nie rozumiem polecenia {decyzja}")
        wybor()


if __name__ == '__main__':
    wisielec()
