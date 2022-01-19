szukanaLiczba = 40

print("Spróbuj odgadnąć liczbę!")

zgadywanaLiczba = int(input("Odgadnij liczbę: "))

while zgadywanaLiczba != szukanaLiczba:

    if zgadywanaLiczba > szukanaLiczba:
        print("Za duża")
        print("Spróbuj jeszcze raz!")

    elif zgadywanaLiczba < szukanaLiczba:
        print("Za mała")
        print("Spróbuj jeszcze raz!")

    else:
        print("Brawo")

    zgadywanaLiczba = int(input("Odgadnij liczbę: "))
