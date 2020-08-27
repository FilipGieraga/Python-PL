import random
import csv
import json
import pandas as pd
from matplotlib import pyplot as plt
import pdfkit

w = "dolnośląskie kujawsko-pomorskie lubelskie lubuskie łódzkie małopolskie mazowieckie opolskie podkarpackie podlaskie pomorskie śląskie\
    świętokrzyskie warmińsko-mazurskie wielkopolskie zachodniopomorskie"

w = w.split()
# print(w)


imiona_męskie = """Adam, Adolf, Adrian, Albert, Aleksander, Aleksy, Alfred, Amadeusz, Andrzej, Antoni, Arkadiusz, Arnold, Artur,
Bartłomiej, Bartosz, Benedykt, Beniamin, Bernard, Błażej, Bogdan, Bogumił, Bogusław, Bolesław, Borys, Bronisław,
Cezary, Cyprian, Cyryl, Czesław,
Damian, Daniel, Dariusz, Dawid, Dionizy, Dominik, Donald,
Edward, Emanuel, Emil, Eryk, Eugeniusz,
Fabian, Feliks, Ferdynand, Filip, Franciszek, Fryderyk,
Gabriel, Gerard, Grzegorz, Gustaw,
Henryk, Herbert, Hilary, Hubert,
Ignacy, Igor, Ireneusz,
Jacek, Jakub, Jan, Janusz, Jarosław, Jerzy, Joachim, Józef, Julian, Juliusz,
Kacper, Kajetan, Kamil, Karol, Kazimierz, Klaudiusz, Konrad, Krystian, Krzysztof,
Lech, Leon, Leszek, Lucjan, Ludwik,
Łukasz,
Maciej, Maksymilian, Marceli, Marcin, Marek, Marian, Mariusz, Mateusz, Michał, Mieczysław, Mikołaj, Miłosz, Mirosław,
Nikodem, Norbert,
Olaf, Olgierd, Oskar,
Patryk, Paweł, Piotr, Przemysław,
Radosław, Rafał, Remigiusz, Robert, Roman, Rudolf, Ryszard,
Sebastian, Seweryn, Sławomir, Stanisław, Stefan, Sylwester, Szymon,
Tadeusz, Teodor, Tomasz,
Wacław, Waldemar, Wiesław, Wiktor, Witold, Władysław, Włodzimierz, Wojciech,
Zbigniew, Zdzisław, Zenon, Zygmunt"""

imiona_męskie = imiona_męskie.replace('\n', ' ')
imiona_męskie = imiona_męskie.split(", ")

# print(imiona_męskie)
# print(len(imiona_męskie))

imiona_żeńskie = """Ada, Adela, Adelajda, Adrianna, Agata, Agnieszka, Aldona, Aleksandra, Alicja, Alina, Amanda, Amelia, Anastazja,
Andżelika, Aneta, Anita, Anna, Antonina,
Barbara, Beata, Berenika, Bernadeta, Blanka, Bogusława, Bożena,
Cecylia, Celina, Czesława,
Dagmara, Danuta, Daria, Diana, Dominika, Dorota,
Edyta, Eliza, Elwira, Elżbieta, Emilia, Eugenia, Ewa, Ewelina,
Felicja, Franciszka,
Gabriela, Grażyna,
Halina, Hanna, Helena,
Iga, Ilona, Irena, Irmina, Iwona, Izabela,
Jadwiga, Janina, Joanna, Jolanta, Jowita, Judyta, Julia, Julita, Justyna,
Kamila, Karina, Karolina, Katarzyna, Kazimiera, Kinga, Klaudia, Kleopatra, Kornelia, Krystyna,
Laura, Lena, Leokadia, Lidia, Liliana, Lucyna, Ludmiła, Luiza,
Łucja,
Magdalena, Maja, Malwina, Małgorzata, Marcelina, Maria, Marianna, Mariola, Marlena, Marta, Martyna, Marzanna, Marzena, Matylda,
Melania, Michalina, Milena, Mirosława, Monika,
Nadia, Natalia, Natasza, Nikola, Nina,
Olga, Oliwia, Otylia,
Pamela, Patrycja, Paula, Paulina,
Regina, Renata, Roksana, Róża, Rozalia,
Sabina, Sandra, Sara, Sonia, Stanisława, Stefania, Stella, Sylwia,
Tamara, Tatiana, Teresa,
Urszula,
Weronika, Wiesława, Wiktoria, Wioletta,
Żaneta,
Zofia, Zuzanna, Zyta"""

imiona_żeńskie = imiona_żeńskie.replace('\n', ' ')
imiona_żeńskie = imiona_żeńskie.split(", ")

# print(imiona_żeńskie)
# print(len(imiona_żeńskie))

# r=random.choice(imiona_męskie)
# l=random.choice(imiona_żeńskie)
# print(r,l)

# l1=random.randint(1,10)
# print(l1)

nazwiska = """
 Nowak Kowalski Wiśniewski Wójcik Kowalczyk Kamiński Lewandowski Zieliński Szymański Woźniak Dąbrowski\
 Kozłowski  Jankowski  Mazur  Wojciechowski  Kwiatkowski  Krawczyk  Kaczmarek  Piotrowski  Grabowski\
 Zając Pawłowski Michalski Król Wieczorek Jabłoński Wróbel Nowakowski Majewski Olszewski Stępień\
 Malinowski Jaworski Adamczyk Dudek Nowicki Pawlak Górski Witkowski Walczak Sikora Baran Rutkowski\
 Michalak Szewczyk Ostrowski Tomaszewski Pietrzak Zalewski Wróblewski Marciniak Jasiński Zawadzki\
 Bąk Jakubowski Sadowski Duda Włodarczyk Wilk Chmielewski Borkowski Sokołowski Szczepański Sawicki\
 Kucharski Lis Maciejewski Kubiak Kalinowski Mazurek Wysocki Kołodziej Kaźmierczak Czarnecki Sobczak\
 Konieczny Urbański Głowacki Wasilewski Sikorski Zakrzewski Krajewski Krupa Laskowski Ziółkowski Gajewski\
 Mróz Brzeziński Szulc Szymczak Makowski Baranowski Przybylski Kaczmarczyk Borowski Błaszyk Adamski Górecki\
 Chojnacki Kania Leszczyński Janik Szczepaniak Czerwiński Kozioł Mucha Lipiński Wesołowski Kozak Cieślak\
 Kowalewski Andrzejewski Mikołajczyk Jarosz Musiał Zięba Kowalik Kołodziejczyk Markowski Brzozowski Kopeć\
 Nowacki Orłowski Domański Żak Tomczyk Kurek Piątek Pawlik Tomczak Markiewicz Ciesielski Wawrzyniak Kot\
 Wójtowicz Polak Wolski Kruk Stasiak Stankiewicz Sowa Łuczak Wierzbicki Jastrzębski Urbaniak Karpiński\
 Czajkowski Piasecki Gajda Nawrocki Bednarek Stefański Klimek Janicki Jóźwiak Dziedzic Sosnowski Bielecki\
 Majchrzak Madej Leśniak Milewski Maj Kowal Małecki Śliwiński Socha Skiba Marek Dobrowolski Domagała\
 Bednarczyk Wrona Urban Olejniczak Pająk Matuszewski Romanowski Kasprzak Świątek Wilczyński Ratajczak\
 Kurowski Michalik Owczarek Orzechowski Grzelak Łukasik Olejnik Sobolewski Rogowski Mazurkiewicz Barański\
 Bukowski Matusiak Sroka Kosiński Kędzierski Skowroński Marcinkowski"""

nazwiska = nazwiska.split()
# print(nazwiska)

# waga mezczyzn i wzrost
waga_m = random.randint(58, 140)
wzrost_m = random.randint(168, 192)

# waga kobiet i wzrost
waga_k = random.randint(42, 110)
wzrost_k = random.randint(156, 178)


def choice():
    d1 = input("Czy chcesz stworzyć plik uczestnicy.csv?(t/n)\n")
    if d1 == "t":
        csv_file()
    else:
        pass
    d2 = input("Czy chcesz stworzyć plik uczestnicy.json?(t/n)\n")
    if d2 == "t":
        json_file()
    else:
        pass


def csv_file():
    id1 = 100000
    with open("uczestnicy.csv", "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(['Imie', 'Nazwisko', 'Wiek', 'Płeć', 'Województwo', 'Identyfikator'])
        for i in range(200):
            plec = random.choice(["M", "K"])
            if plec == "M":
                imie = random.choice(imiona_męskie)
            else:
                imie = random.choice(imiona_żeńskie)
            nazwisko = random.choice(nazwiska)
            if plec == "K":
                list_nazwisko = list(nazwisko)
                if list_nazwisko[-1] == "i":
                    list_nazwisko[-1] = "a"
                    nazwisko = ''.join(list_nazwisko)
            wiek = random.randint(18, 80)
            wojewodztwo = random.choice(w)
            identyfikator = id1
            csv_writer.writerow([imie, nazwisko, wiek, plec, wojewodztwo, identyfikator])
            i += 1
            id1 += random.randint(1, 4)


def json_file():
    with open("uczestnicy.csv", "r") as new_file:
        csv_reader = csv.reader(new_file, delimiter=",", quotechar='"')
        next(csv_reader)
        d = dict()
        x1 = 0  # id2
        x2 = 0  # wzrost
        x3 = 0  # waga
        for line in csv_reader:
            if line:
                id2 = line[5]
                plec1 = line[3]
                x1 = id2
                if plec1 == "M":
                    waga = random.randint(58, 140)
                    wzrost = random.randint(168, 192)
                    x2 = wzrost
                    x3 = waga
                elif plec1 == "K":
                    waga = random.randint(42, 110)
                    wzrost = random.randint(156, 178)
                    x2 = wzrost
                    x3 = waga
                d.update({x1: {"wzrost": x2, "waga": x3}})

    def set_default(d):
        if isinstance(d, set):
            return list(d)
        raise TypeError

    with open("uczestnicy.json", "w") as outfile:
        json.dump(d, outfile, default=set_default, indent=2)


def BMI():
    df2 = pd.read_json("uczestnicy.json")
    df2 = df2.T
    df2["BMI"] = df2.waga / ((df2.wzrost / 100) ** 2)
    df2["Komentarz"] = ''
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)
    df2.loc[df2.BMI.between(0, 18.49), ["Komentarz"]] = ["Niedowaga"]
    df2.loc[df2.BMI.between(18.5, 24.99), ["Komentarz"]] = ["Waga prawidłowa"]
    df2.loc[df2.BMI.between(25, 29.99), ["Komentarz"]] = ["Nadwaga"]
    df2.loc[df2.BMI.between(30, 60), ["Komentarz"]] = ["Otyłość kliniczna"]
    df1 = pd.read_csv("uczestnicy.csv", engine='python')
    df2["Płeć"] = df1["Płeć"].values
    df2["Województwo"] = df1["Województwo"].values
    df2["Wiek"] = df1["Wiek"].values
    print("\n")
    print(df2)
    df2_m = df2.loc[df2["Płeć"].str.contains("M")]
    df2_k = df2.loc[df2["Płeć"].str.contains("K")]
    plt.style.use('fivethirtyeight')
    return df2, df2_m, df2_k


def histograms(df2, df2_m, df2_k):
    # #Histogram dla mężczyzn
    BMI_m = plt.hist(df2_m.BMI, edgecolor="black")
    plt.legend()
    plt.title('Histogram BMI Mężczyźni')
    plt.xlabel("BMI")
    plt.ylabel("liczba osób")
    plt.tight_layout()
    plt.savefig("Histogram1.png")
    plt.show()

    # Histogram dla kobiet
    BMI_k = plt.hist(df2_k.BMI, edgecolor="black")
    plt.legend()
    plt.title('Histogram BMI Kobiety')
    plt.xlabel("BMI")
    plt.ylabel("liczba osób")
    plt.tight_layout()
    plt.savefig("Histogram2.png")
    plt.show()

    df2_m1 = df2.loc[(df2["Płeć"].str.contains("M")) & (df2["Wiek"].between(18, 35))]
    # print(df2_m1.BMI)
    df2_k1 = df2.loc[(df2["Płeć"].str.contains("K")) & (df2["Wiek"].between(18, 35))]
    # print(df2_k1)
    BMI_mk1 = plt.hist(df2_k1.BMI, edgecolor="blue", bins=5, color="red", alpha=0.5, label="Kobiety")
    BMI_mk1 = plt.hist(df2_m1.BMI, edgecolor="red", bins=5, color="blue", alpha=0.5, label="Mężczyźni")
    plt.legend(loc='upper right')
    plt.title('Histogram BMI dla k i m w wieku 18-35')
    plt.xlabel("BMI")
    plt.ylabel("liczba osób")
    plt.tight_layout()
    plt.savefig("Histogram3.png")
    plt.show()

    df2_m2 = df2.loc[(df2["Płeć"].str.contains("M")) & (df2["Wiek"].between(46, 65))]
    # print(df2_m1.BMI)
    df2_k2 = df2.loc[(df2["Płeć"].str.contains("K")) & (df2["Wiek"].between(46, 65))]
    # print(df2_k1)
    BMI_mk2 = plt.hist(df2_k2.BMI, edgecolor="blue", bins=5, color="red", alpha=0.5, label="Kobiety")
    BMI_mk2 = plt.hist(df2_m2.BMI, edgecolor="red", bins=5, color="blue", alpha=0.5, label="Mężczyźni")
    plt.legend(loc='upper right')
    plt.title('Histogram BMI dla k i m w wieku 46-65')
    plt.xlabel("BMI")
    plt.ylabel("liczba osób")
    plt.tight_layout()
    plt.savefig("Histogram4.png")
    plt.show()

    df2_m3 = df2.loc[(df2["Płeć"].str.contains("M")) & (df2["Wiek"].between(66, 80))]
    # print(df2_m1.BMI)
    df2_k3 = df2.loc[(df2["Płeć"].str.contains("K")) & (df2["Wiek"].between(46, 80))]
    # print(df2_k1)
    BMI_mk3 = plt.hist(df2_k3.BMI, edgecolor="blue", bins=5, color="red", alpha=0.5, label="Kobiety")
    BMI_mk3 = plt.hist(df2_m3.BMI, edgecolor="red", bins=5, color="blue", alpha=0.5, label="Mężczyźni")
    plt.legend(loc='upper right')
    plt.title('Histogram BMI dla k i m w wieku 66-80')
    plt.xlabel("BMI")
    plt.ylabel("liczba osób")
    plt.tight_layout()
    plt.savefig("Histogram5.png")
    plt.show()

    # Grupowanie średniej względem województw

    w_m = df2_m.groupby("Województwo")["BMI"].mean()
    # print(w_m)
    w_k = df2_k.groupby("Województwo")["BMI"].mean()
    # print(w_k)

    w_m.plot(kind='bar', title="Mężczyźni", x='BMI', y='Województwo')
    plt.subplots_adjust(bottom=0.44)
    plt.savefig("Histogram6.png")
    plt.show()

    w_k.plot(kind='bar', title="Kobiety", x='BMI', y='Województwo')
    plt.subplots_adjust(bottom=0.44)
    plt.savefig("Histogram7.png")
    plt.show()

    print("\n\n")
    s1 = (f"Najwyższe BMI w grupie mężczyzn to: {df2_m.BMI.max()}")
    s2 = (f"Najwyższe BMI w grupie kobiet to: {df2_k.BMI.max()}")
    s3 = (f"Średnie BMI w grupie mężczyzn to: {df2_m.BMI.mean()}")
    s4 = (f"Średnie BMI w grupie kobiet to: {df2_k.BMI.mean()}")
    s5 = (f"Najniższe BMI w grupie mężczyzn to: {df2_m.BMI.min()}")
    s6 = (f"Najniższe BMI w grupie kobiet to: {df2_k.BMI.min()}")
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)
    print("\n\n")


def html_to_pdf(df2):
    try:
        print("Tworzenie podsumowania w pdf")
        html = df2.to_html("Podsumowanie.html")
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }
        pdfkit.from_file("Podsumowanie.html", "Podsumowanie.pdf", configuration=config, options=options)
    except:
        print(
            "Coś poszło nie tak. Zainstaluj program wkhtmltopdf i sprawdź czy zmienna path_wkhtmltopdf do niego prowadzi")


choice()
df2, df2_m, df2_k = BMI()
histograms(df2, df2_m, df2_k)
html_to_pdf(df2)
