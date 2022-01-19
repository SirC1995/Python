# Kreator postaci
# Gracz posiada 30 pkt umiejętności
# może je przeznaczyc na 4 dowolne umijetnosci,
# gracz może odejmować pkt od umijętności i przeznaczać je na inne

um = {"siła": 0,
      "zdrowie": 0,
      "mądrość": 0,
      "zręczność": 0}

choice = None

pkt = 30
print ("Posiadasz", pkt, "pkt umiejętności.")
print ("Na co je przenaczysz")

while choice != "0":

    print (
    """
    Kreator postaci

    0 - zakończ
    1 - dodaj pkt umiejętności
    2 - odejmij pkt umiejętności
    3 - wyświetl pkt umiejętności
    """
    )

    choice = input ("Wybierasz: ")
    print ()

    # zakończenie
    if choice == "0":
        print ("Żegnaj")


    if choice == "1":
        print ("Dodawanie pkt umiejętności")
        umi = input ("Wybierz umiejętność: ")
        if umi in um:
            point = int(input ("Ile pkt umiejętności chcesz przeznaczyć: "))
            um[umi] += point
            pkt = pkt - point
            print ("\nDodałeś", point, "pkt do umiejętności", umi)
            print ("\nPozostało Ci", pkt, "pkt umiejętności")
        else:
            print ("\nNie ma takjej umiejętności")

    elif choice == "2":
        print ("Odejmowanie pkt umiejętności")
        umi = input ("Wybierz umiejętność: ")
        if umi in um:
            point = int (input ("Ile pkt chcesz odjąć od umiejętności: "))
            um[umi] -= point
            pkt = pkt + point
            print ("\nOdjołeś", point, "pkt od umiejętności", umi)
            print ("\nMasz teraz", pkt, "pkt umiejętności")
        else:
            print ("\nNie ma takiej umiejętności")

    elif choice == "3":
        print ("Wyświetlenie ile pkt ma umiejętność")
        umi = input ("Wybierz umiejętność: ")
        if  umi in um:
            point = um [umi]
            print ("\nUmiejętność", umi, "posiada", point, "punktów")
        else:
            print ("\nNie ma takiej umiejętności")
    else:
        print ("\nNiestety", choice, "to nie prawidłowy wybór")

input ("\n\nAby zakończyć, naciśnij Enter")
