import random

# pobranie imienia użytkownika
imie = input("Podaj swoje imię: ")

# pobranie zakresu liczb
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

# wygenerowanie losowej liczby
liczba = random.randint(poczatek, koniec)

# licznik kroków
kroki = 0

# pętla główna
while True:
    kroki += 1
    # pobranie liczby od użytkownika
    try:
        wpis = input("Zgadnij liczbę (lub X aby zakończyć): ")
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