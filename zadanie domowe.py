print("BAZA DANYCH IMION")

baza_danych = []

while True:
    print("""Menu:
    1: Wyswietl baze
    2: Dodaj imie
    3: Usun imie
    4: Liczba imion
    5: Wyszukaj imie w bazie
    0: Wyjscie
    """)

    wybor_uzytkownika = input("Podaj numer:")
    if wybor_uzytkownika =="1":
        print(baza_danych)

    elif wybor_uzytkownika =="2":
        imie = str(input("Podaj swoje imie:"))
        baza_danych.append(imie)

    elif wybor_uzytkownika =="3":
        usun_imie = str(input("Podaj imie do usuniecia:"))
        baza_danych.remove(usun_imie)

    elif wybor_uzytkownika =="4":
        print(len(baza_danych))

    elif wybor_uzytkownika =="5":
        szukaj_imie = str(input("Podaj imie do wyszukania:"))

        if imie in baza_danych:
            print("Podane imie znajduje sie w bazie danych")
        else:
            print("Brak imienia w bazie!")

    elif wybor_uzytkownika =="0":
        print("Do zobaczenia!")

        break




