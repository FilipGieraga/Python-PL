import random
import datetime
import json
####
from collections import OrderedDict
from operator import getitem


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

imiona_męskie = imiona_męskie.replace('\n',' ')
imiona_męskie=imiona_męskie.split(", ")

imiona_żeńskie="""Ada, Adela, Adelajda, Adrianna, Agata, Agnieszka, Aldona, Aleksandra, Alicja, Alina, Amanda, Amelia, Anastazja,
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

imiona_żeńskie = imiona_żeńskie.replace('\n',' ')
imiona_żeńskie=imiona_żeńskie.split(", ")

nazwiska="""
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


nazwiska=nazwiska.split()

dzialy=["Badania i rozwój","Finansowo-księgowy","Compliance","IT","Logistyka","Marketing","HR"]
stanowiska_hr=["Kierownik","Rekrutacja","Zarządzanie świadczeniami i odszkodowaniami",
               "Bezpieczeństwo i zdrowie","Trening i rozwój","Relacje z pracownikiem"]


def losowa_data():
    """Losowa data z przedziału od początku 2010 do dzisiaj"""
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date.today()
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%d-%m-%Y")


def losowy_wiek():
    """Losowa data z przedziału od początku 2010 do dzisiaj"""
    start_date = datetime.date(1975, 1, 1)
    end_date = datetime.date(1992, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def licz_wiek(data_urodzenia):
    """Liczenie wieku poszczególnych pracowników firmy"""
    dzisiaj = datetime.date.today()
    wiek = dzisiaj.year - data_urodzenia.year -((dzisiaj.month, dzisiaj.day)<(data_urodzenia.month, data_urodzenia.day))
    return wiek


def pracownicy(liczba_pracowników, nazwa_firmy):
    """Generowanie danych podstawowych"""
    firma = {}
    x=set(random.sample(range(10000,100000),k=1000))


    for i in range(liczba_pracowników):
        id_pracownika = x.pop()
        plec = random.choice(["M", "K"])
        if plec =="M":
            imie= random.choice(imiona_męskie)
            plec="Mężczyzna"
        else:
            imie = random.choice(imiona_żeńskie)
            plec = "Kobieta"
        nazwisko= random.choice(nazwiska)
        if plec == "Kobieta":
            list_nazwisko = list(nazwisko)
            if list_nazwisko[-1]=="i":
                list_nazwisko[-1] = "a"
                nazwisko = ''.join(list_nazwisko)
        email= imie.lower()+"."+nazwisko.lower()+"@"+nazwa_firmy.lower()+".com"
        data_rozpoczęcia = losowa_data()
        data_rozpoczęcia1= datetime.datetime.strptime(data_rozpoczęcia, "%d-%m-%Y")
        staz_pracy=datetime.datetime.today()-data_rozpoczęcia1
        staz_pracy= staz_pracy.days
        data_urodzenia = losowy_wiek()
        wiek= licz_wiek(data_urodzenia)
        data_urodzenia=data_urodzenia.strftime("%d-%m-%Y")

        firma.update({id_pracownika :
                          {"Imię":imie,
                           "Nazwisko":nazwisko,
                           "Płeć":plec,
                           "E-mail":email,
                           "Data urodzenia": data_urodzenia,
                           "Wiek": wiek,
                           "Data rozpoczęcia": data_rozpoczęcia,
                           "Staż pracy": staz_pracy,#str(staz_pracy)+" dni",
                           }
                      })
    return firma

def firma_struktura(firma, nazwa_firmy):
    """Generowanie struktury stanowisk działów, stanowisk oraz zarobków"""
    list_staz=[]
    list_klucze=[]
    for k,v in firma.items():
        list_staz+=([v["Staż pracy"]])
        list_klucze+=[k]

    #======= wazne
    wspolczynnik= len(firma)/100
    wspolczynnik=int(wspolczynnik)

    l_menadzerow=10
    l_supervisorow=20
    l_hr=(len(firma)*0.03)
    l_hr= round(l_hr,0)
    l_hr=int(l_hr)
    wykorzystane_dzialy = random.sample(dzialy[0:-1], wspolczynnik)
    wykorzystane_dzialy1=wykorzystane_dzialy.copy()
    stanowiska_hr1=stanowiska_hr.copy()

    for i in range(len(firma)):
        if i==0:
            klucz_1=list_staz.index(max(list_staz)) # index najwyzszej wartosci w liscie staz
            klucz_2=list_klucze[klucz_1] # wartosc
            firma[klucz_2]["Stanowisko"] = 'CEO'
            firma[klucz_2]["E-mail"] = firma[klucz_2]["Imię"].lower()+"."+firma[klucz_2]["Nazwisko"].lower()+"-CEO@"+nazwa_firmy.lower()+".com"
            if wspolczynnik==1:
                zarobki = random.randint(200000,250000)
                zarobki=round(zarobki,-1)
            elif wspolczynnik==2:
                zarobki = random.randint(230000, 280000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==3:
                zarobki = random.randint(265000, 300000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==4:
                zarobki = random.randint(290000, 330000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==5:
                zarobki = random.randint(320000, 400000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==6:
                zarobki = random.randint(380000, 500000)
                zarobki = round(zarobki, -1)
            firma[klucz_2]["Zarobki roczne"] = str(zarobki)+" zł"
            firma[klucz_2]["Zarobki miesięczne"] = str(int(zarobki/12))+" zł"
            # print(list_klucze)
            # print(list_staz)
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            # print(list_klucze)
            # print(list_staz)
            # print(klucz_1,klucz_2)
            increment1=i


        elif i in range(i,increment1+wspolczynnik+1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            firma[klucz_2]["Stanowisko"] = 'President'
            ### Oddział
            firma[klucz_2]["Dział"] = wykorzystane_dzialy1.pop()
            if wspolczynnik==1:
                zarobki = random.randint(150000,175000)
                zarobki=round(zarobki,-1)
            elif wspolczynnik==2:
                zarobki = random.randint(160000, 180000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==3:
                zarobki = random.randint(175000, 190000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==4:
                zarobki = random.randint(190000, 210000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==5:
                zarobki = random.randint(200000, 240000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==6:
                zarobki = random.randint(230000, 260000)
                zarobki = round(zarobki, -1)
            firma[klucz_2]["Zarobki roczne"] = str(zarobki) + " zł"
            firma[klucz_2]["Zarobki miesięczne"] = str(int(zarobki / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            increment2 = i


        elif i in range(i,increment2+wspolczynnik+1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            firma[klucz_2]["Stanowisko"] = 'Vice-President'
            ### Oddział
            if len(wykorzystane_dzialy1)==0:
                wykorzystane_dzialy1 = wykorzystane_dzialy.copy()
            firma[klucz_2]["Dział"] = wykorzystane_dzialy1.pop()
            if wspolczynnik==1:
                zarobki = random.randint(100000,115000)
                zarobki=round(zarobki,-1)
            elif wspolczynnik==2:
                zarobki = random.randint(120000, 140000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==3:
                zarobki = random.randint(130000, 160000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==4:
                zarobki = random.randint(150000, 175000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==5:
                zarobki = random.randint(160000, 180000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==6:
                zarobki = random.randint(175000, 199000)
                zarobki = round(zarobki, -1)
            firma[klucz_2]["Zarobki roczne"] = str(zarobki) + " zł"
            firma[klucz_2]["Zarobki miesięczne"] = str(int(zarobki / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            increment3 = i


        elif i in range(i,increment3+(l_menadzerow*wspolczynnik)+1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            firma[klucz_2]["Stanowisko"] = 'Menadżer'
            ### Oddział
            if len(wykorzystane_dzialy1)==0:
                wykorzystane_dzialy1 = wykorzystane_dzialy.copy()
            firma[klucz_2]["Dział"] = wykorzystane_dzialy1.pop()
            if wspolczynnik==1:
                zarobki = random.randint(70000,95000)
                zarobki=round(zarobki,-1)
            elif wspolczynnik==2:
                zarobki = random.randint(78000, 95000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==3:
                zarobki = random.randint(85000, 100000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==4:
                zarobki = random.randint(95000, 105000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==5:
                zarobki = random.randint(100000, 110000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==6:
                zarobki = random.randint(105000, 115000)
                zarobki = round(zarobki, -1)
            firma[klucz_2]["Zarobki roczne"] = str(zarobki) + " zł"
            firma[klucz_2]["Zarobki miesięczne"] = str(int(zarobki / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            increment4 = i


        elif i in range(i,increment4+(l_supervisorow*wspolczynnik)+1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            firma[klucz_2]["Stanowisko"] = 'Supervisor'
            ### Oddział
            if len(wykorzystane_dzialy1)==0:
                wykorzystane_dzialy1 = wykorzystane_dzialy.copy()
            firma[klucz_2]["Dział"] = wykorzystane_dzialy1.pop()
            if wspolczynnik==1:
                zarobki = random.randint(50000,65000)
                zarobki=round(zarobki,-1)
            elif wspolczynnik==2:
                zarobki = random.randint(60000, 70000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==3:
                zarobki = random.randint(70000, 80000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==4:
                zarobki = random.randint(85000, 98000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==5:
                zarobki = random.randint(95000, 103000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==6:
                zarobki = random.randint(100000, 107000)
                zarobki = round(zarobki, -1)
            firma[klucz_2]["Zarobki roczne"] = str(zarobki) + " zł"
            firma[klucz_2]["Zarobki miesięczne"] = str(int(zarobki / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
            increment5 = i
            kierownik = 1

        elif i in range(i,increment5+l_hr+1):
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            if len(stanowiska_hr1)==0:
                stanowiska_hr1 = stanowiska_hr.copy()
                stanowiska_hr1=stanowiska_hr1[1:]
            if wspolczynnik > 3 and kierownik < 2:
                firma[klucz_2]["Stanowisko"] = stanowiska_hr1[0]
                kierownik+=1
            else:
                firma[klucz_2]["Stanowisko"] = stanowiska_hr1.pop(0)
            ### Oddział
            firma[klucz_2]["Dział"] = dzialy[-1]
            if wspolczynnik==1 and firma[klucz_2]["Stanowisko"] == 'Kierownik':
                zarobki = random.randint(70000, 95000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==2 and firma[klucz_2]["Stanowisko"] == 'Kierownik':
                zarobki = random.randint(78000, 95000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==3 and firma[klucz_2]["Stanowisko"] == 'Kierownik':
                zarobki = random.randint(85000, 100000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==4 and firma[klucz_2]["Stanowisko"] == 'Kierownik':
                zarobki = random.randint(95000, 105000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==5 and firma[klucz_2]["Stanowisko"] == 'Kierownik':
                zarobki = random.randint(100000, 110000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==6 and firma[klucz_2]["Stanowisko"] == 'Kierownik':
                zarobki = random.randint(105000, 115000)
                zarobki = round(zarobki, -1)

            if wspolczynnik==1 and firma[klucz_2]["Stanowisko"] != 'Kierownik':
                zarobki = random.randint(50000,65000)
                zarobki=round(zarobki,-1)
            elif wspolczynnik==2 and firma[klucz_2]["Stanowisko"] != 'Kierownik':
                zarobki = random.randint(60000, 70000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==3 and firma[klucz_2]["Stanowisko"] != 'Kierownik':
                zarobki = random.randint(70000, 80000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==4 and firma[klucz_2]["Stanowisko"] != 'Kierownik':
                zarobki = random.randint(85000, 98000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==5 and firma[klucz_2]["Stanowisko"] != 'Kierownik':
                zarobki = random.randint(95000, 103000)
                zarobki = round(zarobki, -1)
            elif wspolczynnik==6 and firma[klucz_2]["Stanowisko"] != 'Kierownik':
                zarobki = random.randint(100000, 107000)
                zarobki = round(zarobki, -1)
            firma[klucz_2]["Zarobki roczne"] = str(zarobki) + " zł"
            firma[klucz_2]["Zarobki miesięczne"] = str(int(zarobki / 12)) + " zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)


        else:
            klucz_1 = list_staz.index(max(list_staz))
            klucz_2 = list_klucze[klucz_1]
            firma[klucz_2]["Stanowisko"] = 'Zwykły pracownik'
            if len(wykorzystane_dzialy1)==0:
                wykorzystane_dzialy1 = wykorzystane_dzialy.copy()
            firma[klucz_2]["Dział"] = wykorzystane_dzialy1.pop()
            if wspolczynnik<=3:
                zarobki = random.randint(40000,60000)
                zarobki=round(zarobki,-1)
            elif wspolczynnik>3:
                zarobki = random.randint(55000, 85000)
                zarobki = round(zarobki, -1)
            firma[klucz_2]["Zarobki roczne"] = str(zarobki)+" zł"
            firma[klucz_2]["Zarobki miesięczne"] = str(int(zarobki/12))+" zł"
            list_klucze.pop(klucz_1)
            list_staz.pop(klucz_1)
    return firma

def drukuj_pracowników(firma):
    for k,v in firma.items():
        print(k,v)


def to_json(firma):
    with open("Pracownicy.json", "w", encoding='utf-8') as outfile:
        json.dump(firma, outfile, indent=2, ensure_ascii=False)
    print("Dane załadowano do pliku .json .")


liczba_pracowników=500
nazwa_firmy="Google"
firma = pracownicy(liczba_pracowników, nazwa_firmy)
firma = firma_struktura(firma, nazwa_firmy)
drukuj_pracowników(firma)
to_json(firma)


