import random
import argparse


def calculate(**kwargs):
    nr_podejscia = 1
    wylosowany_nr = 0
    lucky_number = kwargs.get("lucky_number")
    dolna_granica = kwargs.get("range")[0]
    gorna_granica = kwargs.get("range")[1]

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


parser = argparse.ArgumentParser(
    description="Program zgadujący losową, bądź podaną liczbę z losowego, bądź podanego przedziału")

parser.add_argument('-z', type=str, metavar='dolny i górny zakres', help="zakres, domyślnie <1,1000>",
                    default="1,1000")

parser.add_argument('-s', type=int, metavar='szczęśliwa liczba',
                    help="szczęśliwa liczba, domyślnie w zakresie<1,1000>",
                    default=random.randint(1, 1000))
args = parser.parse_args()

my_list = [int(item) for item in args.z.split(',')]


if __name__=='__main__':
    if my_list[0] >= my_list[1]:
        print("Podany przedział jest nieprawidłowy.")
    elif args.s not in range(my_list[0], my_list[1] + 1):
        print("Szczęśliwa liczba nie jest w przedziale.")
    else:
        calculate(lucky_number=args.s, range=my_list)

