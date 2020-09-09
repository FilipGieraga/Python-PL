import random


def wybor():
    decyzja = input("Czy chcesz spróbować jeszcze raz?(t/n)\n")
    if decyzja == "t":
        wprowadzanie()
    else:
        print("Dziękuje za skorzystanie z programu.")


def wprowadzanie():
    while True:
        try:
            decyzja_1 = input("Czy chcesz podać liczbę? (t/n)\n")
            if decyzja_1 not in "tTnN":
                raise ValueError("Niezrozumiała decyzja")
        except Exception as error1:
            print(f"Wystąpił błąd : {error1}\nWpisz decyzję t/n.")
        else:
            break
    decyzja_1 = decyzja_1.lower()
    if decyzja_1 == "t":
        while True:
            try:
                lucky_number = int(input("Podaj liczbę: \n"))
            except Exception as error:
                print(f"Wystąpił błąd : {error}\nZły input, spróbuj jeszcze raz.")
            else:
                break
        print(f"Twoja liczba to: {lucky_number}")
    elif decyzja_1 == "n":
        lucky_number = random.randint(1, 1000)
        print(f"Twoja losowo wygenerowana liczba to: {lucky_number}")

    while True:
        try:
            decyzja_2 = input("Czy chcesz podać przedział? (t/n)\n")
            if decyzja_2 not in "tTnN":
                raise TypeError
        except:
            print("Wpisz decyzję t/n.")
        else:
            break

    decyzja_2 = decyzja_2.lower()
    if decyzja_2 == "t":
        while True:
            try:
                dolna_granica = int(input("Dolna granica: "))
                gorna_granica = int(input("Górna granica: "))
                if dolna_granica >= gorna_granica:
                    raise ValueError("Dolna granica powinna być mniejsza niż górna granica")
            except Exception as error3:
                print(f"Wystąpił błąd : {error3}\nZły input, spróbuj ponownie.")
            else:
                break
        print(f"Wybrany przez Ciebie zakres to : [{dolna_granica} , {gorna_granica}]")
    elif decyzja_2 == "n":
        dolna_granica = 1
        gorna_granica = 1000
        print(f"Twój domyślny zakres to : [{dolna_granica} , {gorna_granica}]")

    if lucky_number not in range(dolna_granica, (gorna_granica + 1)):
        print("Podana, bądź wygenerowana liczba nie jest w przedziale.")
        wybor()
    else:
        calculate(lucky_number, dolna_granica, gorna_granica)


# lucky_number- szczesliwy nr wygenerowany bądź wprowadzony
# dolna_granica- dolna granica wygenerowana bądź wprowadzona
# gorna_granica- gorna granica wygenerowana bądź wprowadzon
# wylosowany_nr- liczba wylosowana przez komputer
# nr_podejscia- ilosc podejsc komputera do zgadniecia liczby
# lucky_number- musi sie miescic w [dolna_granica,gorna_granica]

def calculate(lucky_number, dolna_granica, gorna_granica):
    nr_podejscia = 1
    wylosowany_nr = 0
    while wylosowany_nr != lucky_number:
        wylosowany_nr = random.randint(dolna_granica, gorna_granica)
        print(f"Podejście nr {nr_podejscia}, wylosowany nr: {wylosowany_nr}, szczęśliwy nr to: {lucky_number}, "
              f"zakres [{dolna_granica} , {gorna_granica}]")
        nr_podejscia += 1
        if wylosowany_nr > lucky_number:
            gorna_granica = wylosowany_nr - 1
            print(f"Za wysoko, szczęśliwy nr jest mniejszy, zmniejszamy górny zakres do {gorna_granica}.\n")
        elif wylosowany_nr < lucky_number:
            dolna_granica = wylosowany_nr + 1
            print(f"Za nisko, szczęśliwy nr jest większy, zwiększamy dolny zakres do {dolna_granica}.\n")
        else:
            print("Trafiony :)")
    else:
        print(f"Program znalazł liczbę przy podejściu nr. {nr_podejscia - 1}")
    wybor()

if __name__=='__main__':
    wprowadzanie()
