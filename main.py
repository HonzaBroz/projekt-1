"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Brož
email: jan.bro@exekutorsky-urad.cz
"""


TEXTS = [
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



uzivatele =  {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
oddělovač = 40 * "-"

p_jmeno = input ("Přihlašovací jméno: ")
heslo = input ("Heslo: ")

print(oddělovač)

if p_jmeno in uzivatele and uzivatele.setdefault(p_jmeno) == heslo:
    print("Vitej užitateli: ", p_jmeno,"\n"
          "Máme pro tebe tři texty k analyzování","\n",
          oddělovač)
    vyber_text = input("Zadej text 1-3: ")
    print (oddělovač)
    if vyber_text in ("1", "2", "3"):

        rozdelení_slovniku = TEXTS[int(vyber_text) - 1].replace(".", " ").replace(",", " ").split()

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

        
        print("Počet slov je:", počet_slov)
        print("Počet slov s prvním velkým pismenem je:", početslov_s_velkm_prvnim_pismenem)
        print("Počet slov psaných velkými písmeny je:", počet_slov_psanych_velkými_pismeny)
        print("Počet slov psaných malými písmeny je:", počet_slov_s_malym_pismene)
        print("Počet čísel je:", počet_čísel)
        print("Součet všech čísel je:", soucet_cisel2)
        print(oddělovač)
        
        
        

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
  
        
        print("Délka|", "Četnost".center(18), "| Počet")
        print(oddělovač)
        print("   1 |", ("*" * int(delk_slova1)).ljust(18), "|", delk_slova1)
        print("   2 |", ("*" * int(delk_slova2)).ljust(18), "|", delk_slova2)
        print("   3 |", ("*" * int(delk_slova3)).ljust(18), "|", delk_slova3)
        print("   4 |", ("*" * int(delk_slova4)).ljust(18), "|", delk_slova4)
        print("   5 |", ("*" * int(delk_slova5)).ljust(18), "|", delk_slova5)
        print("   6 |", ("*" * int(delk_slova6)).ljust(18), "|", delk_slova6)
        print("   7 |", ("*" * int(delk_slova7)).ljust(18), "|", delk_slova7)
        print("   8 |", ("*" * int(delk_slova8)).ljust(18), "|", delk_slova8)
        print("   9 |", ("*" * int(delk_slova9)).ljust(18), "|", delk_slova9)
        print("   10|", ("*" * int(delk_slova10)).ljust(18), "|", delk_slova10)
        print("   11|", ("*" * int(delk_slova11)).ljust(18), "|", delk_slova11)

    elif vyber_text not in ("1", "2", "3") and vyber_text.isnumeric():
        print ("Nezadal jste možnost z výběru, ukončuji program")
    else: 
        print ("Nezadal jste číslo, ukončuji program")
        

else:
    print("Uživatel není registrovany, ukončuji program")
    
    
