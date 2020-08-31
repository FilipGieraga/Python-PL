import random
import argparse
from argparse import RawTextHelpFormatter

cyfry = "0123456789"
duze_litery = "ABCDEFGHIJKLMNOPRSTQUWXYZ"
male_litery = "abcdefghijklmnoprqstuwxyz"
znaki_specjalne = "!@#$%^&*(){}[]\|:\"'<>?,./"


def sprecyzowane_haslo(**kwargs):
    p = ''
    for k, v in kwargs.items():
        if k == 'c' and v != 0:
            for i in range(v):
                p += random.choice(cyfry)
        if k == 'd' and v != 0:
            for i in range(v):
                p += random.choice(duze_litery)
        if k == 'm' and v != 0:
            for i in range(v):
                p += random.choice(male_litery)
        if k == 'z' and v != 0:
            for i in range(v):
                p += random.choice(znaki_specjalne)
    p = ''.join(random.sample(p, len(p)))
    return print(f"Twoje sprecyzowane hasło: {p}")


def losowo_wygenerowane_haslo(y):
    x = cyfry + duze_litery + male_litery + znaki_specjalne
    x = ''.join(random.sample(x, len(x)))
    x = x[:y]
    return f"Twoje losowe hasło to: {x}"


parser = argparse.ArgumentParser(description="Wygeneruj losowe haslo", formatter_class=RawTextHelpFormatter)

parser.add_argument("o", metavar="Opcje", type=str, help="l - losowe hasło\n"
                                                         "[-n liczba] opcjonalna ilość znaków w całkowicie losowym haśle, domyślnie 8\n"
                                                         "s - sprecyzowane hasło\n"
                                                         "[-c liczba] opcjonalna ilość cyfr w sprecyzowanym haśle, domyślnie 0\n"
                                                         "[-m liczba] opcjonalna ilość małych liter w sprecyzowanym haśle, domyślnie 0\n"
                                                         "[-d liczba] opcjonalna ilość duzych liter w sprecyzowanym haśle, domyślnie 0\n"
                                                         "[-s liczba] opcjonalna ilość znaków specjalnych w sprecyzowanym haśle, domyślnie 0\n",
                    choices=["l", "s"], nargs="?")

args, sub_args = parser.parse_known_args()

if args.o == 'l':
    parser.add_argument('-n', type=int, help="ilość znaków w całkowicie losowym haśle, domyślnie 8", default=8)
    args = parser.parse_args(sub_args)
    print(losowo_wygenerowane_haslo(args.n))
elif args.o == 's':
    parser.add_argument('-c', type=int, help="ilość cyfr w sprecyzowanym haśle, domyślnie 0", default=0)
    parser.add_argument('-m', type=int, help="ilość małych liter w sprecyzowanym haśle, domyślnie 0", default=0)
    parser.add_argument('-d', type=int, help="ilość duzych liter w sprecyzowanym haśle, domyślnie 0", default=0)
    parser.add_argument('-z', type=int, help="ilość znakow specjalnych w sprecyzowanym haśle, domyślnie 0", default=0)
    args = parser.parse_args(sub_args)
    sprecyzowane_haslo(c=args.c, d=args.d, m=args.m, z=args.z)
else:
    pass
