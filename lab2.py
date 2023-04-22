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

def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    print("Suma cyfr podanej liczby wynosi:", suma)

def potegi_dwojki(n):
    for i in range(n):
        print("2 do potęgi", i, "to", 2**i)

def pierwiastek(Y):
    i = 0
    while i*i <= Y:
        i += 1
    i -= 1
    print("Pierwiastek liczby", Y, "wynosi", i)

while True:
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))

    wybor = (input(""" 
    ######### Co chcesz zrobić? #########
    ## 1 - porównaj liczby             ##
    ## 2 - zwróć wartość bezwględna    ##
    ## 3 - pomnóż                      ##
    ## 4 - oblicz sumę cyfr liczby     ##
    ## 5 - wypisz n kolejnych potęg 2  ##
    ## 6 - znajdź pierwiastek liczby   ##
    ## X - wyjdź z programu            ##
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
    elif wybor == 4:
        nowa_liczba = int(input("Podaj nową liczbę: "))
        suma_cyfr(nowa_liczba)
    elif wybor == 5:
        n = int(input("Podaj liczbę potęg: "))
        potegi_dwojki(n)
    elif wybor == 6:
        Y = int(input("Podaj liczbę: "))
        pierwiastek(Y)
    elif wybor.lower() == 'x':
        break
    else:
        print("Zły wybór")
    
    input("Naciśnij Enter, aby kontynuować...") 