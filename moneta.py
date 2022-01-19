# rzut moneta
# połączenie pętli z funkcja if i else
# rzut wykonywany bedzie 100 razy

import random

rzut = 0
reszka = 0
orzel = 0

while rzut < 100:

    rzut += 1
    moneta = random.randint (1, 2)
    
    if moneta == 1:
        reszka +=1

    else:
        orzel += 1

print ("\nIlość wyrzuconych reszek to", reszka)
print ("\nIlość wyrzuconych orłów to", orzel)

if orzel > reszka:
    print ("Wygrał ktoś kto wybrał orła")

else:
    print ("Wygrał ktoś kto wybrał rzeszke")

input ("\n\nAby zakończyć naciśnij Enter")
