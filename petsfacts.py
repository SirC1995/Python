import requests, json

def pet_choice(animal_type, amount):
    params["animal_type"] = animal_type
    params["amount"] = amount
    
    r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

    try:
        content = r.json()
    except json.decoder.JSONDecoderError:
        print("Niepoprawny format")
    else:
        for pet in content:
            print(pet["text"])
        
params = {
    "animal_type" : "cat",
    "amount" : 5
    
}
choice = None

while choice != "0":
    print(
    """
    Fakty o zwierzętach:

    0 - zakończ
    1 - koty
    2 - psy
    """)

    choice = input("Wybierasz: ")

    # Wyjście z programu
    if choice == "0":
        print("Do zobaczenia")

    # Wybór kotów
    elif choice == "1":
        animal_type = "cat"
        amount = int(input("Ile faktów chcesz wyświetlić: "))
        pet_choice(animal_type, amount)

    elif choice == "2":
        animal_type = "dog"
        amount = int(input("Ile faktów chcesz wyświetlić: "))
        pet_choice(animal_type, amount)

    else:
        print("Niestety", choice, "to nieprawidłowy wybór")
        
