# Kto jest Twoim tatą
# program pozwala wprowadzić imie i nazwisko osoby
# i pozwala sprawdzić kto jest jej tatą
# program wykorzystuje słowniki

fathers = {"Krzysztof Burdek": "Bogusław Burdek",
           "Piotr Kopacz": "Włodzimierz Kopacz",
           "Luke Skywalker": "Anakin Skywalker",
            "Włodzimierz Kopacz": "Jan Kopacz",
           "Grzegorz Kwieciński": "Marian Kwieciński",
           "Bogusław Burdek": "Stefan Burdek"}

choice = None


while choice != "0":

    print (
    """
    Kto jest Twoim tatą

    0 - zakończ
    1 - znajdź parę syn-ojciec
    2 - dodaj parę syn-ojciec
    3 - usuń parę syn-ojciec
    4 - zmień parę syn-ojciec
    5 - pokaż dziadka
    """
    )

    choice = input ("Wybierasz: ")
    print ()

    # wyjdź
    if choice == "0":
        print ("Do widzenia!")

    # znajdź parę
    elif choice == "1":
        term = input ("Czyjego ojca mam wyświetlić: ")
        if term in fathers:
            definition = fathers[term]
            print ("\nOjcem", term, "jest", definition)
        else:
            print ("\nNiestety, nie ma takiej osoby")

    # dodaj parę
    elif choice == "2":
        term = input ("Jaką osobę chcesz dodać?: ")
        if term not in fathers:
            definition = input ("Kto jest jego ojcem?: ")
            fathers[term] = definition
            print ("\nSyn", term, "i jego ojciec zostali dodani")
        else:
            print ("Ta osoba już istnieje! Spróbuj zmienićjego ojca")

    # usuń parę
    elif choice == "3":
        term = input ("Jaką osobę i ojca chcesz usunąć?: ")
        if term in fathers:
            del fathers[term]
            print ("\nOk zostali usunięci")
        else:
            print ("Nie ma takiej osoby i jego ojca")

    # zamiana Pary
    elif choice == "4":
        term = input ("Jakiej osobie chcesz zmienić ojca: ")
        if term in fathers:
            definition = input ("Kto jest jego ojcem?: ")
            fathers [term] = definition
            print ("\n Syn", term, "ma nowego ojca")
        else:
            print ("\nNie ma takiej osoby! Spróbuj ją dodać")

    # pokazanie dziadka
    elif choice == "5":
        grandson = input("Wprowadź imię i nazwisko osoby, której dziadka chcesz znaleźć: ")
        if grandson in fathers:
            son = fathers[grandson]
            father = fathers[son]
            print("\nDziadkiem", grandson, "jest", father)
        else:
            print("\nNiestety nie znam dziadka osoby:", grandson)

    else:
        print ("\nNiestety", choice, "to nieprawidłowy wybór")

input ("\nAby zakończyć, naciśnij Enter")
