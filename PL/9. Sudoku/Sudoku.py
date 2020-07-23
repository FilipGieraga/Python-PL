import numpy as np


def grid():
    """Utworzenie macierzy 9 na 9 wypelnionej zerami typu int"""
    s_grid=np.zeros((9,9), dtype = int)
    return s_grid

# sudoku1 = grid()

def fill_the_grid(sudoku1):
    """Dodawanie elementow niezerowych do macierzy"""
    statement="t"
    while statement=="t":
        while True:
            try:
                x, y, z = input(
                    "Podaj pozycję do wypełnienia(rząd(1,9), kolumna(1,9), wartość(1,9) po spacji: \n").split(',')
                x = int(x)
                y = int(y)
                z = int(z)
                if x not in range(1,10) or y not in range(1,10) or z not in range(1,10):
                    raise ValueError
            except :
                print("Zła wartość jednego z parametrów. Spróbuj ponownie.")
            else:
                break
        x = x - 1
        y = y - 1
        sudoku1[x][y]=z
        print(f"Wartość {z} została wstawiona do elementu ({x+1},{y+1})")
        statement = str(input("Czy chcesz dodać kolejną liczbę?(t/n)"))
    print(sudoku1)
    return sudoku1

# sudoku= fill_the_grid(sudoku)


def sudoku_examples():
    """Przykładowe szablony sudoku do rozwiązania przez mój algorytm"""
    #srednie
    s_1=np.array([[2,0,0,0,0,7,5,0,0],
                  [0,6,5,0,1,0,0,0,4],
                  [7,0,0,0,5,0,0,0,0],
                  [0,0,0,0,0,6,9,0,3],
                  [6,0,0,0,0,0,0,7,8],
                  [0,7,4,0,0,1,0,0,0],
                  [0,0,0,4,0,0,0,0,1],
                  [4,3,7,0,0,0,0,9,5],
                  [9,0,2,5,3,8,0,0,0]])
    #srednie
    s_2=np.array([[0,3,0,0,0,0,0,0,9],
                  [0,0,0,8,0,0,0,0,2],
                  [0,2,7,0,0,4,0,0,0],
                  [9,0,0,4,5,0,8,0,0],
                  [1,0,0,0,0,6,9,0,0],
                  [3,7,4,0,0,2,0,6,0],
                  [4,9,6,0,7,0,2,0,0],
                  [0,0,0,3,6,0,0,0,0],
                  [0,5,0,2,0,0,0,9,1]])
    #trudne nie przejdzie
    s_3=np.array([[0,5,0,0,0,0,0,0,0],
                  [0,0,3,0,9,0,0,6,2],
                  [0,0,0,0,6,0,5,3,8],
                  [9,0,0,0,0,1,3,4,0],
                  [0,0,0,0,0,0,7,0,0],
                  [0,3,0,2,0,0,0,0,0],
                  [0,0,0,9,0,5,0,8,0],
                  [5,0,0,0,0,7,0,0,0],
                  [1,0,9,6,0,0,0,0,4]])
    #łatwe
    s_4=np.array([[3,0,1,7,0,2,5,4,0],
                  [0,9,2,0,0,0,0,0,0],
                  [0,7,0,6,0,0,2,0,3],
                  [5,0,0,1,6,0,0,2,0],
                  [1,6,0,0,2,9,4,0,0],
                  [0,0,0,0,7,8,0,0,5],
                  [0,1,9,8,3,4,6,0,2],
                  [8,3,0,0,0,0,0,1,4],
                  [2,0,0,0,0,0,3,7,8]])
    #trudne częściowo wypełnione
    s_5=np.array([[0,0,0,0,0,0,0,0,9],
                  [0,0,9,0,0,0,0,0,1],
                  [5,0,0,0,0,4,0,0,0],
                  [4,0,0,8,3,2,1,0,0],
                  [0,1,8,7,4,0,3,0,0],
                  [7,0,0,1,9,6,0,0,0],
                  [9,6,0,0,7,0,4,0,0],
                  [3,7,0,5,0,0,0,0,8],
                  [0,8,5,0,0,0,0,6,0]])


    print("Przykładowe sudoku:")
    print(f"Sudoku nr.1: \n{s_1}\n")
    print(f"Sudoku nr.2: \n{s_2}\n")
    print(f"Sudoku nr.3: \n{s_3}")
    print("Dodatkowy komentarz: To sudoku jest za trudne dla mojego algorytmu, dlatego zatrzyma się po 15 iteracji.\n")
    print(f"Sudoku nr.4: \n{s_4}\n")
    print(f"Sudoku nr.5: \n{s_5}")
    print("Dodatkowy komentarz: To sudoku zostało częściowo wypełnione, żeby móc się wykonać.\n")
    while True:
        try:
            x=int(input("Wybierz nr sudoku:\n"))
            if x not in range(1,6):
                print("Nieprawidłowy numer sudoku.")
                raise ValueError
        except:
            print("Spróbuj ponownie.")
        else:
            break

    if x==1:
        sudoku = s_1
    elif x==2:
        sudoku = s_2
    elif x==3:
        sudoku = s_3
    elif x==4:
        sudoku = s_4
    elif x==5:
        sudoku = s_5
    return sudoku

sudoku1 = sudoku_examples()


def solve(sudoku1):
    """Funkcja rozwiązująca sudoku prostym sposobem"""
    l=[1,2,3,4,5,6,7,8,9]
    l = [int(i) for i in l]

    d={}
    for r in range(0,9):
        for c in range(0,9):
            if sudoku1[r][c]==0:
                if r < 3 and c < 3:
                    solutions = []
                    for element in l:
                        if element in sudoku1[:, c] or element in sudoku1[r, :] or element in sudoku1[0:3, 0:3]:
                            print(f"Dla wsp. ({r},{c}) {element} nie spełnia warunku.")
                            element += 1
                        else:
                            print(f"Dla wsp. ({r},{c}) {element} spełnia warunek.")
                            solutions.append(element)
                            d[(r, c)] = solutions
                    for wsp, rozw in d.items():
                        x = wsp[0]
                        y = wsp[1]
                        if len(rozw)==1:
                            sudoku1[x][y] = rozw[0]
                elif r in range(3, 6) and c in range(0, 3):
                    solutions = []
                    for element in l:
                        if element in sudoku1[:, c] or element in sudoku1[r, :] or element in sudoku1[3:6, 0:3]:
                            print(f"Dla wsp. ({r},{c}) {element} nie spełnia warunku.")
                            element += 1
                        else:
                            print(f"Dla wsp. ({r},{c}) {element} spełnia warunek.")
                            solutions.append(element)
                            d[(r, c)] = solutions
                    for wsp, rozw in d.items():
                        x = wsp[0]
                        y = wsp[1]
                        if len(rozw)==1:
                            sudoku1[x][y] = rozw[0]
                elif r in range(6, 9) and c in range(0, 3):
                    solutions = []
                    for element in l:
                        if element in sudoku1[:, c] or element in sudoku1[r, :] or element in sudoku1[6:9, 0:3]:
                            print(f"Dla wsp. ({r},{c}) {element} nie spełnia warunku.")
                            element += 1
                        else:
                            print(f"Dla wsp. ({r},{c}) {element} spełnia warunek.")
                            solutions.append(element)
                            d[(r, c)] = solutions
                    for wsp, rozw in d.items():
                        x = wsp[0]
                        y = wsp[1]
                        if len(rozw) == 1:
                            sudoku1[x][y] = rozw[0]
                elif r in range(0, 3) and c in range(3, 6):
                    solutions = []
                    for element in l:
                        if element in sudoku1[:, c] or element in sudoku1[r, :] or element in sudoku1[0:3,3:6]:
                            print(f"Dla wsp. ({r},{c}) {element} nie spełnia warunku.")
                            element += 1
                        else:
                            print(f"Dla wsp. ({r},{c}) {element} spełnia warunek.")
                            solutions.append(element)
                            d[(r, c)] = solutions
                    for wsp, rozw in d.items():
                        x = wsp[0]
                        y = wsp[1]
                        if len(rozw) == 1:
                            sudoku1[x][y] = rozw[0]
                elif r in range(0, 3) and c in range(6, 9):
                    solutions = []
                    for element in l:
                        if element in sudoku1[:, c] or element in sudoku1[r, :] or element in sudoku1[0:3, 6:9]:
                            print(f"Dla wsp. ({r},{c}) {element} nie spełnia warunku.")
                            element += 1
                        else:
                            print(f"Dla wsp. ({r},{c}) {element} spełnia warunek.")
                            solutions.append(element)
                            d[(r, c)] = solutions
                    for wsp, rozw in d.items():
                        x = wsp[0]
                        y = wsp[1]
                        if len(rozw) == 1:
                            sudoku1[x][y] = rozw[0]
                elif r in range(3, 6) and c in range(3, 6):
                    solutions = []
                    for element in l:
                        if element in sudoku1[:, c] or element in sudoku1[r, :] or element in sudoku1[3:6, 3:6]:
                            print(f"Dla wsp. ({r},{c}) {element} nie spełnia warunku.")
                            element += 1
                        else:
                            print(f"Dla wsp. ({r},{c}) {element} spełnia warunek.")
                            solutions.append(element)
                            d[(r, c)] = solutions
                    for wsp, rozw in d.items():
                        x = wsp[0]
                        y = wsp[1]
                        if len(rozw) == 1:
                            sudoku1[x][y] = rozw[0]
                elif r in range(3, 6) and c in range(6, 9):
                    solutions = []
                    for element in l:
                        if element in sudoku1[:, c] or element in sudoku1[r, :] or element in sudoku1[3:6, 6:9]:
                            print(f"Dla wsp. ({r},{c}) {element} nie spełnia warunku.")
                            element += 1
                        else:
                            print(f"Dla wsp. ({r},{c}) {element} spełnia warunek.")
                            solutions.append(element)
                            d[(r, c)] = solutions
                    for wsp, rozw in d.items():
                        x = wsp[0]
                        y = wsp[1]
                        if len(rozw) == 1:
                            sudoku1[x][y] = rozw[0]
                elif r in range(6, 9) and c in range(3, 6):
                    solutions = []
                    for element in l:
                        if element in sudoku1[:, c] or element in sudoku1[r, :] or element in sudoku1[6:9, 3:6]:
                            print(f"Dla wsp. ({r},{c}) {element} nie spełnia warunku.")
                            element += 1
                        else:
                            print(f"Dla wsp. ({r},{c}) {element} spełnia warunek.")
                            solutions.append(element)
                            d[(r, c)] = solutions
                    for wsp, rozw in d.items():
                        x = wsp[0]
                        y = wsp[1]
                        if len(rozw) == 1:
                            sudoku1[x][y] = rozw[0]
                else:
                    solutions = []
                    for element in l:
                        if element in sudoku1[:, c] or element in sudoku1[r, :] or element in sudoku1[6:9, 6:9]:
                            print(f"Dla wsp. ({r},{c}) {element} nie spełnia warunku.")
                            element += 1
                        else:
                            print(f"Dla wsp. ({r},{c}) {element} spełnia warunek.")
                            solutions.append(element)
                            d[(r, c)] = solutions
                    for wsp, rozw in d.items():
                        x = wsp[0]
                        y = wsp[1]
                        if len(rozw) == 1:
                            sudoku1[x][y] = rozw[0]
        else:
            pass
    print(f"Słownik wsp+rozw : {d}")
    wstawiono=0
    for k,v in d.items():
        if len(v)==1:
            wstawiono+=1
    print(f"Ilość wstawionych pozycji: {wstawiono}")
    return sudoku1

incre=0
while 0 in sudoku1 and incre<15:
    solve(sudoku1)
    print(f"To było podejście nr: {incre+1}")
    incre+=1
else:
    print(sudoku1)

