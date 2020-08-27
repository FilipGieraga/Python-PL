string = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźżaąbc"
string1 = "abcdefghijklmnopqrstuvwxyzabc"
string2 = " -.,"


def wybor():
    while True:
        try:
            decyzja = input("Czy chcesz spróbować jeszcze raz?(t/n)\n")
            decyzja=decyzja.lower()
            if decyzja not in "tn":
                raise ValueError("Zła wartość decyzji.")
        except Exception as error:
            print(error)
        else:
            break


    if decyzja == "t":
        while True:
            try:
                decyzja_2 = input("Czy chcesz zaszyfrować wiadomość?(t/n)\n")
                decyzja_2 = decyzja_2.lower()
                if decyzja_2 not in "tn":
                    raise ValueError("Zła wartość decyzji.")
            except Exception as error:
                print(error)
            else:
                break


        if decyzja_2 == "t":
            szyfruj(string, string1, string2)
        else:
            rozszyfruj(string, string1, string2)
    else:
        print("Dziękuje za skorzystanie z programu.")


def szyfruj(string, string1, string2):
    zdanie = input("Wprowadź zdanie do zaszyfrowania:\n")


    while True:
        try:
            znaki = input("Czy uwzględnić polskie znaki?(t/n)\n")
            znaki = znaki.lower()
            if znaki not in "tn":
                raise ValueError("Zła wartość decyzji.")
        except Exception as error:
            print(error)
        else:
            break


    if znaki == "t":
        znaki = string
    else:
        znaki = string1
    zdanie = zdanie.lower()
    nowe_zdanie = ""
    for element in zdanie:
        if element in znaki:
            x = znaki.find(element)
            l = x + 3
            nowe_zdanie += znaki[l]
        elif element in string2:
            nowe_zdanie += element
    nowe_zdanie = nowe_zdanie.upper()
    print(nowe_zdanie)
    wybor()


def rozszyfruj(string, string1, string2):
    zdanie = input("Wprowadź zdanie do rozszyfrowania:\n")


    while True:
        try:
            znaki = input("Czy uwzględnić polskie znaki?(t/n)\n")
            znaki = znaki.lower()
            if znaki not in "tn":
                raise ValueError("Zła wartość decyzji.")
        except Exception as error:
            print(error)
        else:
            break


    if znaki == "t":
        znaki = string
    else:
        znaki = string1
    zdanie = zdanie.lower()
    znaki = znaki[::-1]
    nowe_zdanie = ""
    for element in zdanie:
        if element in znaki:
            x = znaki.find(element)
            l = x + 3
            nowe_zdanie += znaki[l]
        elif element in string2:
            nowe_zdanie += element
    nowe_zdanie = nowe_zdanie.upper()
    print(nowe_zdanie)
    wybor()


if __name__=='__main__':
    szyfruj(string, string1, string2)

