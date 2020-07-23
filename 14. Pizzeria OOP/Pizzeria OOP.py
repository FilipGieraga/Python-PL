
class Pizza:

    menu=[]

    ilosc_pozycji=0

    składniki=["ser","szynka","pieczarki","jalapeno","boczek","cebula","kukurydza","groszek","kabanos","pomidor",
    "ogórek kiszony","tabasco","suszone pomidory","papryka","parmezan","mozzarella","bazylia","rukola","oregano"]

    rozmiar=["28cm","40cm","52cm"]

    def __init__(self,pizza, składniki, rozmiar, cena):
        for s in składniki:
            if s.lower() not in Pizza.składniki:
                raise ValueError("Nie mamy takiego składnika :(")
        self.__class__.menu.append(pizza)
        self.pizza=pizza
        self.skladniki=składniki
        self.rozmiar=rozmiar
        self.cena=cena
        self.numer=Pizza.ilosc_pozycji+1
        Pizza.ilosc_pozycji += 1


    def cena_rozmiaru(self, rozmiar):
        if rozmiar==1:
            cena=self.cena
        elif rozmiar==2:
            cena=1.4*self.cena
        elif rozmiar==3:
            cena = 2*self.cena
        return f"{round(cena)}zł"


    @classmethod
    def zrob_to_sam(cls):
        lista=[]
        while True:
            try:
                x=int(input("Ile składników?\n"))
                if x not in range(1,5):
                    raise ValueError
            except:
                print("Dzwolonona liczba składników to od 1 do 4")
            else:
                break
        q=x
        for i, skladnik in enumerate(Pizza.składniki, start=1):
            print(i, skladnik)
        for x in range(0,x):
            s=int(input("Który składnik chcesz dodać?\n"))
            t= Pizza.składniki[s-1]
            lista.append(t)
        for i, rozmiar in enumerate(Pizza.rozmiar, start=1):
            print(i, f"Rozmiar: {rozmiar}")
        r= int(input("Jaki rozmiar?\n"))
        if q ==2 and r==1:
            print(f"Sładniki to: {lista}, rozmiar: {Pizza.rozmiar[r-1]}, cena 20 zł")
        elif q ==3 and r==1:
            print(f"Sładniki to: {lista}, rozmiar: {Pizza.rozmiar[r-1]}, cena 22 zł")
        elif q==4 and r==1:
            print(f"Sładniki to: {lista}, rozmiar: {Pizza.rozmiar[r-1]}, cena 24 zł")
        elif q ==2 and r==2:
            print(f"Sładniki to: {lista}, rozmiar: {Pizza.rozmiar[r-1]}, cena 24 zł")
        elif q ==3 and r==2:
            print(f"Sładniki to: {lista}, rozmiar: {Pizza.rozmiar[r-1]}, cena 26 zł")
        elif q ==4 and r==2:
            print(f"Sładniki to: {lista}, rozmiar: {Pizza.rozmiar[r-1]}, cena 28 zł")
        elif q== 2 and r == 3:
            print(f"Sładniki to: {lista}, rozmiar: {Pizza.rozmiar[r-1]}, cena 32 zł")
        elif q == 3 and r == 3:
            print(f"Sładniki to: {lista}, rozmiar: {Pizza.rozmiar[r-1]}, cena 34 zł")
        elif q == 4 and r == 3:
            print(f"Sładniki to: {lista}, rozmiar: {Pizza.rozmiar[r-1]}, cena 36 zł")
        else:
            print("Bład zamówienia")

    def zamow(self):
        for i, rozmiar in enumerate(Pizza.rozmiar, start=1):
            print(i, f"Rozmiar: {rozmiar}, Cena: {self.cena_rozmiaru(i)} zł.")
        rozmiar = int(input("Jaki rozmiar do pizzy?\n"))
        cena= self.cena_rozmiaru(rozmiar)
        rozmiar=Pizza.rozmiar[rozmiar-1]
        zmiana=input("Czy chcesz coś zmienić?(t/n)\n")


        if zmiana =="n":
            adres=input("Podaj ulicę i nr mieszkania:\n")
            telefon=int(input("Podaj nr telefonu(bez myślników):\n"))
            print(f"Zamówienie zostało przyjęte na adres: {adres}. W razie czego będziemy dzwonić na: {telefon}")
            print("Twoje zamówienie to:")
            print(f"Nazwa pizzy: {self.pizza}\nSkładniki: {self.skladniki}\nRozmiar: {rozmiar}\nCena: {cena}")


        elif zmiana =="t":
            skladniki = self.skladniki.copy()
            mieso=["szynka","boczek","kabanos"]
            cena=cena[:2]
            cena= int(cena)
            print(cena)
            decyzja = int(input(
                "Co chcesz zrobić?\n1-Dodać składnik\n2-Usunąć składnik\n3-Zamienić składnik\n4-Zakończyć zmiany\n"))


            while decyzja !=4:
                if decyzja==1:
                    for i, skladnik in enumerate(Pizza.składniki, start=1):
                        print(i, skladnik)
                    s = int(input("Który składnik chcesz dodać?\n"))
                    if Pizza.składniki[s-1] in mieso:
                        cena+=3
                    else:
                        cena+=2
                    print(f"Cena: {cena}")
                    skladniki.append(Pizza.składniki[s-1])
                    print(skladniki)


                elif decyzja==2:
                    for i, skladnik in enumerate(skladniki, start=1):
                        print(i, skladnik)
                    u = int(input("Który składnik chcesz usunąć?\n"))
                    if Pizza.składniki[u-1] in mieso:
                        cena-=3
                    else:
                        cena-=2
                    print(f"Cena: {cena}")
                    skladniki.pop(u-1)
                    print(skladniki)


                elif decyzja==3:
                    for i, skladnik in enumerate(skladniki, start=1):
                        print(i, skladnik)
                    z = int(input("Który składnik chcesz zamienić?\n"))
                    for i, skladnik in enumerate(Pizza.składniki, start=1):
                        print(i, skladnik)
                    z1 = int(input(f"Jaki składnik zamiast {skladniki[z-1]}?\n"))
                    skladniki.pop(z-1)
                    skladniki.append(Pizza.składniki[z1-1])
                    print(skladniki)

                decyzja = int(input(
                    "Co chcesz zrobić?\n1-Dodać składnik\n2-Usunąć składnik\n3-Zamienić składnik\n4-Zakończyć zmiany\n"))


            if isinstance(cena,int):
                cena = str(cena) + "zł"
            print("Zmiany zostały dokonane.")
            adres = input("Podaj ulicę i nr mieszkania:\n")
            telefon = int(input("Podaj nr telefonu(bez myślników):\n"))
            print(f"Zamówienie zostało przyjęte na adres: {adres}. W razie czego będziemy dzwonić na: {telefon}")
            print("Twoje zamówienie to:")
            print(f"Nazwa pizzy: {self.pizza}\nSkładniki: {skladniki}\nRozmiar: {rozmiar}\nCena:{cena}")





    def __repr__(self):
        return (f"Nazwa pizzy: {self.pizza},\nSkładniki: {self.skladniki},"
                f"\nCena za {Pizza.rozmiar[0]}:{self.cena_rozmiaru(1)}\n        {Pizza.rozmiar[1]}:{self.cena_rozmiaru(2)} \n"
                f"        {Pizza.rozmiar[2]}:{self.cena_rozmiaru(3)}"
                f"\nNr pizzy: {self.numer}")


    @classmethod
    def wyswietl_menu(cls):
        print("Nasze Menu:")
        for i, instance in enumerate(cls.menu,start=1):
            print(i, instance)

    @staticmethod
    def godziny_otwarcia():
        print("Godziny otwarcia to:\nPn-Pt 9:00-22:00\nSb: 10:00-24:00")




Margerita=Pizza("Margerita",[Pizza.składniki[0],Pizza.składniki[-1]],Pizza.rozmiar[0],18)
Capricciosa=Pizza("Capricciosa",(Pizza.składniki[0],Pizza.składniki[1],Pizza.składniki[2]),Pizza.rozmiar[0],20)
Rimini=Pizza("Rimini",("boczek","cebula"),Pizza.rozmiar[0],20)
Wege=Pizza("Wege",("pieczarki","papryka","kukurydza","groszek"),Pizza.rozmiar[0],20)

#-------------
# Wyswietla menu:
Pizza.wyswietl_menu()
print("\n\n")

#-------------
# Wyswietla godziny otwarcia:
Pizza.godziny_otwarcia()
print("\n\n")

#--------------
# Cena rozmiaru, gdzie rozmiar podawany jest w nawiasie 1- mała, 2 - średnia 3 - duża:
print(Margerita.cena_rozmiaru(3))
print("\n\n")

#--------------
# Pizza losowa po wywolaniu wyswietla się w następujący sposób:
print(Capricciosa)
print("\n\n")

#--------------
# Możemy sami stworzyć pizze ze składników zadeklarowanych w klasie:
Pizza.zrob_to_sam()
print("\n\n")

#--------------
# Możemy zamówić pizze z menu:
Margerita.zamow()
print("\n\n")

#--------------
# Ilość pozycji pizz w klasie:
print(Pizza.ilosc_pozycji)
print("\n\n")


# print(Margerita.__dict__)

