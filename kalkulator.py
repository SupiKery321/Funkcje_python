import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def kalkulator():
    działanie = input("""Podaj działanie, posługując się odpowiednią liczbą:
     1 Dodawanie, 
     2 Odejmowanie, 
     3 Mnożenie, 
     4 Dzielenie:
     """)


    numer_1 = int(input("Proszę podaj pierwszy numer: "))
    numer_2 = int(input("Proszę podaj drugi numer: "))
    

    if działanie == "1":
        print(numer_1 + numer_2)
    if działanie == "2":
        print(numer_1 - numer_2)
    if działanie == "3":
        print(numer_1 * numer_2)
    if działanie == "4":
        print(numer_1 / numer_2)

kalkulator()        


    