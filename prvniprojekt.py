TEX = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]





TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.'''
]



rozdelení_slovniku = TEXTS[0].replace(".", " ").replace(",", " ").split()
print (rozdelení_slovniku)


počet_slov = 0
početslov_s_velkm_prvnim_pismenem = 0
počet_slov_s_malym_pismene = 0
počet_čísel = 0
počet_slov_psanych_velkými_pismeny = 0
soucet_cisel2 = 0



for velka in rozdelení_slovniku:
    počet_slov = počet_slov + 1
    if velka.istitle():
        početslov_s_velkm_prvnim_pismenem = početslov_s_velkm_prvnim_pismenem + 1
    elif velka.isnumeric():
        počet_čísel = počet_čísel +1
        soucet_cisel2 = soucet_cisel2 + int(velka)
    elif velka.islower():
        počet_slov_s_malym_pismene = počet_slov_s_malym_pismene +1
    elif velka.isupper():
        počet_slov_psanych_velkými_pismeny = počet_slov_psanych_velkými_pismeny + 1


print("počet slov s prvním všlkýmm pismenem je", početslov_s_velkm_prvnim_pismenem)
print("počet čísel je:", počet_čísel)
print("součet čísel je:", soucet_cisel2)
print("počet slov s malým písmenem je:", počet_slov_s_malym_pismene)
print("počet slov psaných velkými písmeny je:", počet_slov_psanych_velkými_pismeny)
print("počet slov je", počet_slov)

delk_slova1 = 0
delk_slova2 = 0
delk_slova3 = 0
delk_slova4 = 0
delk_slova5 = 0
delk_slova6 = 0
delk_slova7 = 0
delk_slova8 = 0
delk_slova9 = 0
delk_slova10 = 0
delk_slova11 = 0

for delka in rozdelení_slovniku:
    if len(delka) == 1:
        delk_slova1 = delk_slova1 + 1
    elif len(delka) == 2:
        delk_slova2 = delk_slova2 + 1
    elif len(delka) == 3:
        delk_slova3 = delk_slova3 + 1
    elif len(delka) == 4:
        delk_slova4 = delk_slova4 + 1
    elif len(delka) == 5:
        delk_slova5 = delk_slova5 + 1
    elif len(delka) == 6:
        delk_slova6 = delk_slova6 + 1
    elif len(delka) == 7:
        delk_slova7 = delk_slova7 + 1
    elif len(delka) == 8:
        delk_slova8 = delk_slova8 + 1
    elif len(delka) == 9:
        delk_slova9 = delk_slova9 + 1
    elif len(delka) == 10:
        delk_slova10 = delk_slova10 + 1
    elif len(delka) == 11:
        delk_slova11 = delk_slova11 + 1
  


print(delk_slova1)
print(delk_slova2)
print(delk_slova3)
print(delk_slova4)
print(delk_slova5)
print(delk_slova6)
print(delk_slova7)
print(delk_slova8)
print(delk_slova9)
print(delk_slova10)
print(delk_slova11)