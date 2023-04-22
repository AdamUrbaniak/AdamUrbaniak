import random

imie = input("Podaj swoje imię: ")

while True:
    try:
        poczatek = int(input(f"Cześć {imie}, podaj początek zakresu: "))
        koniec = int(input(f"Cześć {imie}, podaj koniec zakresu: "))
        if poczatek >= koniec:
            print("Podaj poprawny zakres!")
            continue
        break
    except ValueError:
        print("Nieprawidłowe dane!")

liczba = random.randint(poczatek, koniec)

kroki = 0

while True:
    kroki += 1
    try:
        wpis = input("Zgadnij liczbe (lub X aby zakończyć): ")
        if wpis == "X":
            print("Poddajesz się...")
            break
        liczba_uzytkownika = int(wpis)
        if liczba_uzytkownika < poczatek or liczba_uzytkownika > koniec:
            print("Liczba spoza zakresu!")
        elif liczba_uzytkownika == liczba:
            print(f"Brawo {imie}, zgadłeś liczbę w {kroki} krokach!")
            break
        elif liczba_uzytkownika < liczba:
            print("Za mało!")
        else:
            print("Za dużo!")
    except ValueError:
        print("Nieprawidłowe dane!")