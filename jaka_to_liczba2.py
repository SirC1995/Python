# Jaka to liczba 2?
#
# Wybierasz dowolną liczbe od 1 do 100
# Komputer próbuje odgadnąć, dostaje informacje,
# czy podana liczba jest: za duża, za mała
# prawidłowa



import random
print("\tWitaj graczu w grze 'Jaka to liczba 2'")
print("\nPomyśl sobie liczbę od 1 do 100")
print("Komputer spróbuję ją odgadnąć w jak najmniejszej ilośći prób.\n")

# ustaw wartośći początkowe
the_number = int(input("Twoja liczba to: "))
guess = random.randint(1, 100)
print ("Komputer wybrał liczbę:" , guess)
tries = 1

#pętla zgadywania
while guess != the_number:
    if guess > the_number:
        print("Za duża...")
    else:
        print("Za mała...")

    guess = random.randint(1, 100)
    print("Komputer wybrał liczbę: ", guess)
    tries += 1




print("Brawo! Ta liczba to:", the_number)
print("KOmputer do odgadnięcia Twojej liczby potrzebował", tries, "prób\n")
input("\nAby zakończyć naciśnij Enter.")
