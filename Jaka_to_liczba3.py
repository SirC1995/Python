# Jaka to liczba 3
# komputer wybiera losową liczbę z zakresu od 1 do 100
# gracz próbuje jąodgadnać, a komputer go informuje,
# czy podana liczba jest: jest za mała, za duża, prawidłowa
# uzycie funkcji ask_number

import random

print ("Witaj w grze 'Jaka to liczba'")
print ("Komputer wybiera liczbe z zakresu od 1 do 100")
print ("Spróbuj ją zgadnąć")

# definicja funkcji
def ask_number(question, low, high):
    """Poproś o podanie liczby z odpowiedniego zakresu"""
    response = None
    while response not in range(low, high):
        response = int(input (question))
    return response
def main():
    # Ustawienie wartości początkowych
    the_number = random.randint (1,100)
    guess = ask_number("Ta liczba to: ", 1, 100)
    tries = 1

    # pętla zgadywania
    while guess != the_number:
        if guess > the_number:
            print ("Za duża...")
        else:
            print ("Za mała...")

        guess = ask_number("Ta liczba to: ", 1, 100)
        tries +=1

    if guess == the_number:
        print ("Odgadłeś! Ta liczba to", the_number)


main()
input ()
