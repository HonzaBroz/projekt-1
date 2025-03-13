sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62
film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}
film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}
film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}

filmy = {
    str(film_1["jmeno"]) : dict(film_1.items()),
    str(film_2["jmeno"]) : dict(film_2.items()),
    str(film_3["jmeno"]) : dict(film_3.items())
}

print("Vítej v našem filmovém slovníku!".center(62))
print(oddelovac)
print("dostupné filmy | detaily filmu | seznam režisérů".center(62))

ukol1 = int(input("zadej 1, 2 nebo tři pro vývěr z nabidky: "))
if ukol1 == 1 :
    print("Dostupné filmy jsou".center(62))
    print(oddelovac)
    print(tuple(filmy.keys())[0], tuple(filmy.keys())[2], tuple(filmy.keys())[0], sep="| " )
elif ukol1 == 2:
    ukol2 = int(input("zadej cilo filmu, u ktereho chces videt detail "))
    print(tuple(filmy.values())[-1])
elif ukol1 == 3:
    print("Vsichni reziseri")
    print(oddelovac)
    print(tuple(filmy.values())[0]["reziser"])