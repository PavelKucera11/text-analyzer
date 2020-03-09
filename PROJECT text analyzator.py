TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

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
# TEXTS je list

print('TEXT ANALYZATOR')
print('=' * 50)

uzivatele = {   #slovnik
    'bob' : '123',
    'ann' : 'pass123',
    'mike' : 'password123',
    'liz' : 'pass123'
     }

jmeno = (input('Zadej jmeno: '))
heslo = (input('Zadej heslo: '))
zvoleny_text = list()
#print(uzivatele.get(jmeno))
prvni_velke = 0
velka_pis = 0
mala_pis = 0
cisla = 0
hodnota = 0
slovnik_cetnosti = dict()

if str(uzivatele.get(jmeno)) != heslo:   # klic (jmeno) vrati hodnotu (heslo), kdyz je klic spatne vrati "None".
    print("Heslo, nebo uživatelské jméno je špatně!")
elif str(uzivatele.get(jmeno)) == heslo:
    print('Povolení pokračovat!')
    volba = int(input('Zadej volbu 1 az 3: '))

    if volba not in (1,2,3):
        print(volba,'neni ve vyberu')
    else:
        zvoleny_text = TEXTS[volba -1]
        zvoleny_list = zvoleny_text.split() #prevadim text (string) na list
        delka = len(zvoleny_list)
        print('VYSLEDEK:')
        print('=' * 50)

        while zvoleny_list:
            akt_slovo = zvoleny_list.pop()
            akt_slovo = akt_slovo.strip('.,') # oriznuti slova o tecku a carku
            delka_slova = len(akt_slovo)
            slovnik_cetnosti.setdefault(delka_slova, 0) # slovniku zdavam klice s hodnotou 0
            slovnik_cetnosti[delka_slova] = int(slovnik_cetnosti.get(delka_slova)) +1
            # slovniku k danemu klici priradim do hodnoty + 1
            # napr . slovnik_cetnosti[5] = int(0) + 1
            if akt_slovo.istitle():
                prvni_velke = prvni_velke + 1
            elif akt_slovo.isupper():
                velka_pis = velka_pis + 1
            elif akt_slovo.islower():
                mala_pis = mala_pis + 1
            elif akt_slovo.isdigit():
                cisla = cisla +1
                hodnota = hodnota + int(akt_slovo)

        print('Pocet slov:', delka)
        print('Pocet slov zacinajici velkymi pismeny:', prvni_velke)
        print('Pocet slov pouze velkymi pismeny:', velka_pis)
        print('Pocet slov pouze malymi pismeny:', mala_pis)
        print('Pocet cisel v textu:', cisla, ' a jejich hodnota:', hodnota)
        print('=' * 50)
        print('GRAFICKE ZNAZORNENI:')
        print('prvni cislo = pocet znaku, \ndruhe cislo a pocet * = pocet slov')
        print('=' * 50)
        # print(slovnik_cetnosti)
        novy = list(slovnik_cetnosti.items())  # pravadim slovnik_cetnosti na list
        novy.sort()  # (reverse=True)
        # print(novy)
        prvky = 0
        # GRAF
        while prvky < len(novy): # prochazim list novy a kazdy prvek dam do stringu, orezu a rozdelim do f a g
            x = str(novy[prvky])
            x = x.strip("()")
            f, g = x.split(', ')
            print(f, end=' ')
            print('*' * int(g), end=' ')
            print(g)
            prvky = prvky + 1
        print('=' * 40)
        print('NASHLEDANOU!')













