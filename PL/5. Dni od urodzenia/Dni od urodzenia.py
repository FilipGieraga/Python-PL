import time
import datetime

def choice():
    choi=input("Czy chcesz spróbować jeszcze raz?(t/n)\n")
    if choi=="t":
        count_days()
    else:
        print("Dziękuje za skorzystanie z programu.")

def count_days():
    while True:
        try:
            a = int(input("W jakim dniu się urodziłeś?(1,31)\n"))
            b = int(input("W jakim miesiącu?(1,12)\n"))
            c = int(input("W którym roku?\n"))
            birth = datetime.date(c, b, a)
        except:
            print("Zły format daty, proszę spróbuj jeszcze raz. \nProszę nie dodawać 0 z przodu w przypadku liczb od 1 do 9")
        else:
            break
    birth=datetime.date(c,b,a)
    print(birth)
    now = datetime.date.today()
    delt=(now-birth)
    if delt.days>0:
        print(f"Żyjesz dokladnie : {delt.days} dni, czyli {delt.days*24} godzin.")
        print(f"Czyli {delt.days*24*60} minut.")
    elif delt.days<0:
        print(f"Jeśli urodziłbyś się dzisiaj, w podanym roku miałbyć dokładnie : {-delt.days} dni, czyli {-delt.days*24} godzin.")
        print(f"Czyli {-delt.days*24*60} minut.")
    else:
        print("Wpisałeś dzisiejszą datę.")
    choice()

count_days()
