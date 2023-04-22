# KOD do Teamsa: 8n523yb

# from datetime import datetime

# teraz = datetime.now()
# obecny_rok = teraz.year

# # zapytaj użytkownika o imię
# imie = input("Podaj imie: ")
# # Zapytaj użytkownika o rok urodzenia
# urodzony = int(input("Podaj rok urodzenia: "))

# # konwersja zmiennych:
# # int("32")

# # Wyświetl mu informacje:
# # - Cześć, {imię}!
# print("Cześć " + imie)

# # - Masz obecnie {wiek} lat
# wiek = obecny_rok - urodzony
# # print("Masz obecnie "+ str(wiek) + " lat")
# if (wiek > 18):
#     print("Możesz kupić piwo w PL")

# print("to się wydrukuje następne")
# # - 100 lat skończysz w {rok osiągnięcia 100 lat} roku

# if (liczba >=0):
#     print("Wartość bezwględna wynosi: " + str(liczba))
# else :
#     print("Wartość bezwględna wynosi: " + str(-liczba))

# nowa_liczba = int(input("Podaj liczbę: "))
# wartosc_bezwgledna(nowa_liczba)


## Napisz program, który:
# 1. Pobierze od użytkownika 2 liczby
# 2. Da użytkownikowi możliwość wyboru i po naciśnięciu:
# - 1 - zwróci większą liczbę
# - 2 - zwróci wartość bezwględną
# - 3 - pomnoży liczby

def wartosc_bezwgledna(liczba):
    if (liczba >=0):
        print("Wartość bezwględna wynosi: " + str(liczba))
    else :
        print("Wartość bezwględna wynosi: " + str(-liczba))

def porownaj(liczba1, liczba2):
    if(liczba1==liczba2):
        print("Liczby są równe")
    elif(liczba1>liczba2):
        print("Większa jest pierwsza liczba, czyli: ", liczba1)
    else:
       print("Większa jest druga liczba, czyli: ", liczba2)

def pomnoz(liczba1, liczba2):
    print("wynik mnożenia to:", liczba1*liczba2)



liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

wybor = int(input(""" 
######### Co chcesz zrobić? #########
## 1 - porównaj liczby             ##
## 2 - zwróć wartość bezwględną    ##
## 3 - pomnóż                      ##
#####################################
-->
"""))

if wybor == 1:
    porownaj(liczba1, liczba2)
elif wybor == 2:
    wartosc_bezwgledna(liczba1)
    wartosc_bezwgledna(liczba2)
elif wybor == 3:
    pomnoz(liczba1, liczba2)
else: 
    print("Zły wybór")