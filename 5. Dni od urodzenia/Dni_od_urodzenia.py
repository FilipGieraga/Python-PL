import datetime


def wybor():
    decyzja = input("Czy chcesz spróbować jeszcze raz?(t/n)\n")
    if decyzja == "t":
        licz()
    else:
        print("Dziękuje za skorzystanie z programu.")


def licz():
    while True:
        try:
            dzien = int(input("W jakim dniu się urodziłeś?(1,31)\n"))
            miesiac = int(input("W jakim miesiącu?(1,12)\n"))
            rok = int(input("W którym roku?\n"))
            urodziny = datetime.date(rok, miesiac, dzien)
        except Exception as error:
            print(f"Wystąpił błąd: {error}\n"
                  "Zły format daty, proszę spróbuj jeszcze raz. "
                  "\nProszę nie dodawać 0 z przodu w przypadku liczb od 1 do 9")
        else:
            break
    urodziny = datetime.date(rok, miesiac, dzien)
    dzisiaj = datetime.date.today()
    delta = (dzisiaj - urodziny)
    if delta.days > 0:
        print(f"Żyjesz dokladnie : {delta.days} dni, czyli {delta.days * 24} godzin.")
        print(f"Czyli {delta.days * 24 * 60} minut.")
    elif delta.days < 0:
        print(
            f"Jeśli urodziłbyś się dzisiaj, w podanym roku miałbyć dokładnie : {-delta.days} dni, czyli {-delta.days * 24} godzin.")
        print(f"Czyli {-delta.days * 24 * 60} minut.")
    else:
        print("Wpisałeś dzisiejszą datę.")
    wybor()


if __name__ == '__main__':
    licz()
