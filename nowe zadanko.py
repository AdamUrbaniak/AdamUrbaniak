import time

def suma_od_1_do_n():
    n = int(input("Podaj liczbę n: "))
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

start_time = time.time()
wynik = suma_od_1_do_n()
end_time = time.time()

execution_time = end_time - start_time
print("Suma od 1 do n wynosi:", wynik)
print("Czas wykonania funkcji:", execution_time, "sekundy")
