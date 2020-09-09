import random

cyfry = "0123456789"
duze_litery = "ABCDEFGHIJKLMNOPRSTQUWXYZ"
male_litery = "abcdefghijklmnoprqstuwxyz"
znaki_specjalne = "!@#$%^&*(){}[]\|:\"'<>?,./"


def sprecyzowane_haslo():
    p = ""
    while True:
        try:
            d1 = input("Czy mają być cyfry?(t/n)\n")
            if d1 not in "tn":
                raise ValueError("Niezrozumiała decyzja")
        except Exception as error:
            print(f"Wystąpił błąd: {error}\nWpisz decyzję t/n.")
        else:
            break
    if d1 == "t":
        while True:
            try:
                i1 = int(input("Ile?\n"))
            except Exception as error:
                print(f"Wystąpił błąd: {error}\nPodaj liczbę całkowitą.")
            else:
                break
        for i in range(i1):
            p += random.choice(cyfry)
    else:
        pass

    while True:
        try:
            d2 = input("Czy mają być duze litery?(t/n)\n")
            if d2 not in "tn":
                raise ValueError("Niezrozumiała decyzja")
        except Exception as error:
            print(f"Wystąpił błąd: {error}\nWpisz decyzję t/n.")
        else:
            break
    if d2 == "t":
        while True:
            try:
                i2 = int(input("Ile?\n"))
            except Exception as error:
                print(f"Wystąpił błąd: {error}\nPodaj liczbę całkowitą.")
            else:
                break
        for i in range(i2):
            p += random.choice(duze_litery)
    else:
        pass

    while True:
        try:
            d3 = input("Czy mają być małe litery?(t/n)\n")
            if d3 not in "tn":
                raise ValueError("Niezrozumiała decyzja")
        except Exception as error:
            print(f"Wystąpił błąd: {error}\nWpisz decyzję t/n.")
        else:
            break
    if d3 == "t":
        while True:
            try:
                i3 = int(input("Ile?\n"))
            except Exception as error:
                print(f"Wystąpił błąd: {error}\nPodaj liczbę całkowitą.")
            else:
                break
        for i in range(i3):
            p += random.choice(male_litery)
    else:
        pass

    while True:
        try:
            d4 = input("Czy mają być znaki specjalne?(t/n)\n")
            if d4 not in "tn":
                raise ValueError("Niezrozumiała decyzja")
        except Exception as error:
            print(f"Wystąpił błąd: {error}\nWpisz decyzję t/n.")
        else:
            break
    if d4 == "t":
        while True:
            try:
                i4 = int(input("Ile?\n"))
            except Exception as error:
                print(f"Wystąpił błąd: {error}\nPodaj liczbę całkowitą.")
            else:
                break
        for i in range(i4):
            p += random.choice(znaki_specjalne)
    else:
        pass
    return p


def losowo_wygenerowane_haslo(cyfry, duze_litery, male_litery, znaki_specjalne):
    x = cyfry + duze_litery + male_litery + znaki_specjalne
    while True:
        try:
            y = int(input("Ile znaków ma mieć hasło?\n"))
        except Exception as error:
            print(f"Wystąpił błąd: {error}\nPodaj liczbę całkowitą.")
        else:
            break
    x = ''.join(random.sample(x, len(x)))
    x = x[:y]
    return f"Twoje hasło to : {x}"


def decyzja():
    while True:
        try:
            choice = input("Czy chcesz określić ilość poszczególnych znaków w haśle tj. małe i duże litery?(t/n)\n")
            if choice == "t":
                p = sprecyzowane_haslo()
                p = ''.join(random.sample(p, len(p)))
                print(f"Twoje hasło to : {p}")
                ponownie()
            elif choice == "n":
                print(losowo_wygenerowane_haslo(cyfry, duze_litery, male_litery, znaki_specjalne))
                ponownie()
            else:
                raise ValueError("Niezrozumiała decyzja")
        except Exception as error:
            print(f"Wystąpił błąd: {error}\nWpisz decyzję t/n.")
        else:
            break


def ponownie():
    choi = input("Czy chcesz spróbować jeszcze raz?(t/n)\n")
    if choi == "t":
        decyzja()
    else:
        print("Dziękuje za skorzystanie z programu.")


if __name__ == '__main__':
    decyzja()
