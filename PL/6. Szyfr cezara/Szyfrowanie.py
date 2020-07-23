

string="aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźżaąbc"
string1="abcdefghijklmnopqrstuvwxyzabc"
string2=" -.,"

def choice():
    choi = input("Czy chcesz spróbować jeszcze raz?(t/n)\n")
    if choi == "t":
        choi1=input("Czy chcesz zaszyfrować wiadomość?(t/n)\n")
        if choi1=="t":
            cipher(string, string1, string2)
        else:
            decipher(string, string1, string2)
    else:
        print("Dziękuje za skorzystanie z programu.")


def cipher(string, string1, string2):
    zdanie=input("Wprowadź zdanie do zaszyfrowania:\n")
    p = input("Czy uwzględnić polskie znaki?(t/n)\n")
    if p == "t":
        p = string
    else:
        p = string1
    zdanie=zdanie.lower()
    nowe_zdanie=""
    cipher=[]
    for element in zdanie:
        if element in p:
            x=p.find(element)
            l=x+3
            cipher.append(l)
            nowe_zdanie += p[l]
        elif element in string2:
            cipher.append(element)
            nowe_zdanie+=element
    nowe_zdanie=nowe_zdanie.upper()
    print(nowe_zdanie)
    choice()



def decipher(string,string1,string2):
    zdanie=input("Wprowadź zdanie do rozszyfrowania:\n")
    p=input("Czy uwzględnić polskie znaki?(t/n)\n")
    if p=="t":
        p=string
    else:
        p=string1
    zdanie=zdanie.lower()
    p=p[::-1]
    print(p)
    nowe_zdanie=""
    cipher=[]
    for element in zdanie:
        if element in p:
            x=p.find(element)
            l=x+3
            cipher.append(l)
            nowe_zdanie += p[l]
        elif element in string2:
            cipher.append(element)
            nowe_zdanie+=element
    nowe_zdanie=nowe_zdanie.upper()
    print(nowe_zdanie)
    choice()
cipher(string,string1,string2)
# print(decipher(string,string1,string2))