# -*- coding: utf-8 -*-
"""Kopie sešitu Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sUZdMkK0fuqd_7bo0P364zahZ4Zh9NXu
"""

import random
while True:

    i = 2
    prvni = random.randrange(1,9)
    druhi = random.randrange(0,9)
    treti = random.randrange(0,9)
    ctvrty = random.randrange(0,9)

    if prvni == druhy:
        i = 1
    elif prvni == treti:
        i = 1
    elif prvni == ctvrty:
        i = 1

    if druhy == treti:
        i = 1
    elif druhy == ctvrty:
        i = 1
    elif treti == ctvrty:
        i = 1

    if i == 2:
        break

kod = (prvni, druhy, treti, ctvrty)
print("Vygeneroval jsem náhodnou kombinaci čtyř číslic. Let's Go Gambling!")
print("-------------------------------------------------------------------")
pokus = 0
    while True:
        a = 2
        bull = 0
        cow = 0
        prvni_cislo = input("napiště první číslo")
        druhy_cislo = input("napište druhé číslo")
        treti_cislo = input("napište třetí číslo")
        ctvrty_cislo = input("napište čtvrté číslo")
        klic = (prvni_cislo, druhy_cislo, treti_cislo, ctvrty_cislo)

        if prvni_cislo == prvni:
            bull = +1
        elif prvni_cislo == druhy:
            cow = +1
        elif prvni_cislo == treti:
            cow = +1
        elif prvni_cislo == ctvrty:
            cow = +1

        if druhy_cislo == druhy:
            bull = +1
        elif druhy_cislo == prvni:
            cow = +1
        elif druhy_cislo == treti:
            cow = +1
        elif druhy_cislo == ctvrty:
            cow = +1

        if treti_cislo == treti:
            bull = +1
        elif treti_cislo == prvni:
            cow = +1
        elif treti_cislo == druhy:
            cow = +1
        elif treti_cislo == ctvrty:
            cow = +1

        if ctvrty_cislo == ctvrty:
            bull = +1
        elif ctvrty_cislo == prvni:
            cow = +1
        elif ctvrty_cislo == druhy:
            cow = +1
        elif ctvrty_cislo == treti:
            cow = +1

        print(prvni_cislo, druhy_cislo, treti_cislo, ctvrty_cislo)
        print(f"bull: {bulls} and cow: {cows}")
        pokus = +1

        if kod == klic:
            print(f"počet pokusů: {pokus}")
            kon = input("Konec hry, chcete si zahrát znovu? ANO/NE")
        else:
            a = 1

        if a == 2:
            break

    if kon == ANO:
        break
    else:
        end