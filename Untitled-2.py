ciselna_rada = (1, 2, 3, "a", 4)

soucet_cisel = 0

for cislo in ciselna_rada:
    if cislo is not int:
        continue
    else:
    soucet_cisel = soucet_cisel + int(cislo)
   
else:
    print(soucet_cisel)

