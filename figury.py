def pole_prostokata(a, b):      # funkcja do obliczenia pola prostokąta
    return a * b

def pole_kwadratu(a):           # funkcja do obliczenia pola kwadratu
    return a ** 2

def pole_trojkata(a, h):        # funkcja do obliczenia pola trójkąta
    return (a * h) / 2

def pole_trapezu(a, b, h):      # funkcaj do obliczenia pola trapezu
    return (a + b) * h / 2

def pole_kola(r):               # funkcaj do obliczwnia pola koła
    pi = 3.14
    return pi * r ** 2

print("""
                        Kalkulator pola

                Wybierz które pole chcesz obliczyć:

                    1 - pole prostokąta
                    2 - pole kwadratu
                    3 - pole trójkąta
                    4 - pole trapezu
                    5 - pole koła
                    6 - wyjście

""")

wybor = None

while wybor != 6:

    wybor = input("Wybierz które pole chcesz obliczyć: ")

    if wybor == "1":
        print("Obliczanie pola prostokąta:")
        a = float(input("Wprowadź wartość boku a: "))
        b = float(input("Wprowadź wartość boku b: "))
        wynik = pole_prostokata(a, b)
        print(wynik)

    elif wybor == "2":
        print("Obliczanie pola kwadratu:")
        a = float(input("Wprowadź wartość boku: "))
        wynik = pole_kwadratu(a)
        print(wynik)

    elif wybor == "3":
        print("Obliczanie pola trójkąta:")
        a = float(input("Wprowadź wartość podstawy a: "))
        h = float(input("Wprowadź wartość wysokości h: "))
        wynik = pole_trojkata(a, h)
        print(wynik)

    elif wybor == "4":
        print("Obliczanie pola trapezu:")
        a = float(input("Wprowadź wartość podstawy a: "))
        b = float(input("Wprowadź wartość podstawy b: "))
        h = float(input("Wprowadź wartość wysokości h: "))
        wynik = pole_trapezu(a, b, h)
        print(wynik)

    elif wybor == "5":
        print("Obliczanie pola koła:")
        r = float(input("Wprowadź wartość promienia r: "))
        wynik = pole_kola(r)
        print(wynik)

    elif wybor == "6":
        print("Koniec liczenia")
        print("Do następnego razu!")
        break

    else:
        print("Wybór", wybor, "Jest zły spróbuj wybrać poprawnie")


    
