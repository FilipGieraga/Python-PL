'''
Program liczy liczbę dni od urodzenia
'''
import time
import datetime

# print(time.time())
# liczba sekund jaka minela od poczatku czasu dla komputerow, czyli 1 stycznia 1970

# print(time.asctime())
# prezentuje date godzine i rok na chwile obecna

# print(time.gmtime())
# godzina w Greenwich

# help(time)
#Pozwala przejrzeć dokumentację modułu w tym wypadku time

# print(dir(datetime))
# drukuje liste atrybutow oraz metod danego objektu

# help(datetime.date)

#przypisanie wartosci do zmiennej d1
# d1= datetime.date(1966,11,19)
# print(d1.day)
#
# # mozemy miec access do konkretnej wartosci tej daty jak np rok
# print(d1.year)
#
# cr=datetime.date(2000,1 , 1)
# dt=datetime.timedelta(5400)
# #liczba dodatnia zwiekszy liczbe, a ujemna zmniejszy
# print(cr+dt)
#
# # mozemy drukowac format daty w sposob jaki chcemy
#
# message="I was born on {:%A, %B %d, %Y}."
# print(message.format(d1))
#
# # datetime pozwala nam na wykorzystanie czasu daty i datetime
# launch_date=datetime.date(2017,3,30)
# launch_time=datetime.time(22,27,0)
# launch_datetime=datetime.datetime(2017,3,30,22,27,0)
#
#
# now=datetime.date.today()
# print(now)
#
# delt=(now-d1)
# print(f"Żyjesz dokladnie : {delt.days} dni.")
#
# print(f"Czyli {delt.days*24*60} sekund.")
#
# d2=datetime.date(2020,8,31)
#
# print(d2-now)

# d1= datetime.date(1966,71,19)
# print(d1)

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