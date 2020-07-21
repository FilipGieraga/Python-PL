'''
Wytyczne
Program realizujący grę LOTTO  na tzw. chybi-trafił.
Kupon składa się z 1 zakładu (tablica dwuwymiarowa liczb całkowitych lub wartości logicznych o rozmiarze 7x7),
w którym program wybiera (zakreśla) losowo 6 różnych liczb z przedziału [1,49].
Otrzymujemy w ten sposób określony zakład.
Następnie maszyna losująca (dalsza część programu) wyznacza 6 niepowtarzających się liczb (tablica jednowymiarowa)
również z przedziału [1,49].
Program sprawdza rezultat losowania i generuje raport na ekran który zawiera:
automatycznie wypełniony zakład z widocznymi skreśleniami (znak ‘X’ przy skreślonej liczbie),
aktualny wynik losowania (z maszyny losującej),
rezultat trafień – pokrycie się aktualnego losowanie z wcześniej zakreślonymi liczbami.
'''
import random


def lotto():
    d=input("Czy chcesz wprowadzić swój los?(t/n)\n")
    if d=="t":
        twoj_los=set()
        for i in range(1,7):
            while True:
                try:
                    liczba=int(input(f"Podaj liczbę nr {i}:\n"))
                    if liczba not in range(1,50) or liczba in twoj_los:
                        raise ValueError
                    twoj_los.add(liczba)
                    if i<6:
                        print(f"Podane dotychczas liczby to: {sorted(twoj_los)}")
                    else:
                        pass
                except:
                    print("Możliwe błedy:\nPodałeś liczbę poza zakresem <1,49>\nNie jest to liczba całkowita"
                          "\nPodałeś już tą liczbę wcześniej")
                    print(f"Podane dotychczas liczby to: {sorted(twoj_los)}")
                else:
                    break
    else:
        print("Twój pierwszy los zostanie wygenerowany automatycznie.")

    if d=="t":
        los=twoj_los
    else:
        los = set(random.sample(range(1,50), 6))
    wyniki = set(random.sample(range(1,50), 6))
    wspólne=(los.intersection(wyniki))

    print(f"Wyniki losowania to: {sorted(wyniki)}")
    print(f"Nasze liczby to: {sorted(los)}")

    if len(wspólne)==0:
        print("Niestety zero trafień :( ")
    else:
        print(f"Ilość trafień to {len(wspólne)},\na wspólne liczby to {list(wspólne)}")

    while True:
        try:
            x=int(input("Wpisz ilość trafień jaką chcesz uzyskać.\n"))
            if x not in range(1, 7):
                raise ValueError
            else:
                pass
        except:
            print("Podałeś liczbę poza zakresem <1,6>, bądź to nie jest liczba całkowita")
        else:
            break

    q=2
    while len(wspólne)<x:
        los = set(random.sample(range(1, 50), 6))
        print(f"Wyniki : {sorted(wyniki)}")
        wspólne = (los.intersection(wyniki))
        print(f"Los nr. {q}: {sorted(los)}, ilośc trafień to {len(wspólne)}")
        q+=1
    else:
        print(f"Trafiłeś za {q-1}-tym razem, a wspólne liczby to {sorted(wspólne)}.")
    choice()



def choice():
    choi=input("Czy chcesz spróbować jeszcze raz?(t/n)\n")
    if choi=="t":
        lotto()
    else:
        print("Dziękuje za skorzystanie z programu.")


lotto()
