import math

def choice():
    choi=input("Czy chcesz spróbować jeszcze raz?(t/n)\n")
    if choi=="t":
        parameters()
    else:
        print("Dziękuje za skorzystanie z programu.")


def parameters(a=0, b=0, c=0):
    print("Funkcja kwadratowa o postaci ax**2+bx+c=0")
    while True:
        try:
            a = float(input("Wprowadź parametr a: \n"))
            b = float(input("Wprowadź parametr b: \n"))
            c = float(input("Wprowadź parametr c : \n"))
        except:
            print("Zła watość parametrów, proszę spróbować jeszcze raz")
        else:
            break

    if a==0.0:
        print(f"Funcja jest liniowa, nie kwadratowa.\nJej wykres to y={int(b)}x+{int(c)}")
        if c==0.0:
            print("Miejscem zerowym tej funkcji liniowej jest środek wykresu (0,0) ")
        elif b==0.0:
            print("Funckja jest stała.")
        else:
            p1=c/(-b)
            print(f"Miejscem zerowym tej funkcji liniowej jest {round(p1,2)}")
        choice()
    else:
        delta = b**2-4*a*c
        d=[a, b, c, delta]
        print(f"Delta jest równa {delta}")
        return (m_zerowe(d))



def m_zerowe(d):
    delta = d[3]
    if delta > 0:
        sqrt_delta = math.sqrt(delta)
    else:
        print("Brak pierwiastka z delty.")
    p = -d[1] / (2 * d[0])
    q = -d[3] / (4 * d[0])
    p = round(p, 2)
    q = round(q, 2)
    print(f"Wierzchołek funkcji ma współrzędne x = {p} y = {q}")


    if d[3]<0:
        print("Funkcja nie posiada miejsc zerowych.")
    elif d[3]==0:
        m1 = -d[1]/(2*d[0])
        m1 =  round(m1, 2)
        print(f"Funckja posiada jedno miejsce zerowe, gdzie x = {m1} ")
    else:
        m2 = (-d[1]-math.sqrt(d[3]))/(2*d[0])
        m3 = (-d[1]+math.sqrt(d[3]))/(2*d[0])
        m2 = round(m2, 2)
        m3 = round(m3, 2)
        print(f"Funkcja posiada dwa miejsca zerowe, gdzie x1 = {m2}, a x2 = {m3} ")
    choice()

parameters()

