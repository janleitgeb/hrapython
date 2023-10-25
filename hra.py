import random
import time

uvitackaslova = ["Ahoj", "Vítej", "Hello", "Zdravím"]
slovo = random.choice(uvitackaslova)
print(slovo + "!")
time.sleep(1.2)

jmeno = input("Jak se jmenuješ? ")
print(f"Rád tě poznávám, {jmeno}! Hra začíná.")
time.sleep(1.2)

inventar = []
pokracovat = True
vysledek_testu = None

def hlavni_menu():
    print("\nVyber si akci:")
    time.sleep(0.9)
    print("1. Běž do lesa")
    time.sleep(0.9)
    print("2. Běž do jeskyně")
    time.sleep(0.9)
    print("3. Prohledej město")
    time.sleep(0.9)
    print("4. Hovoř s obyvateli")
    time.sleep(0.9)
    print("5. Ukonči hru")
    time.sleep(0.9)

while pokracovat:
    hlavni_menu()
    volba = input("Zadej číslo, co chceš podniknout: ")

    if volba == "1":
        if vysledek_testu is None:
            print("Jdeš do lesa...")
            time.sleep(1.2)
            spravny_vysledek = 7.6
            vysledek = float(input("Našel si svůj starý nepoevedný test ze ZAE. Vypočítej proud odebíraný z transformátoru 230 V a odpor vedení 30 ohmu, počítej v A: "))
            if vysledek == spravny_vysledek:
                print("Správně! Našel jsi tajný výsledek na stromě.")
                inventar.append("Tajná indicie")
                vysledek_testu = spravny_vysledek
            else:
                print("Nesprávný výsledek. Zkus to znovu později.")
        else:
            print("Už jsi našel tajnou indicii ve stromu.")
    elif volba == "2":
        if vysledek_testu == 7.6:
            print("Jdeš do jeskyně...")
            time.sleep(1.2)
            print("Monstrum Pepa tě chytlo jak sis test opravil, nemáš maturitu!.")
            pokracovat = False
        else:
            print("Nemůžeš jít do jeskyně, dokud nevypočítáš správný výsledek testu v lese.")
    elif volba == "3":
        print("Prozkoumáváš město...")
        time.sleep(1.2)
        if "Tajná indicie" in inventar:
            print("Město je v bezpečí díky tajné indicii ze stromu. Můžeme vyrobit generátor jak na vánočním ostrově. Gratuluji!")
        else:
            print("Město nemá elektřinu! Musíš najít tajnou indicii, abys zachránil město.")
    elif volba == "4":
        while True:
            vyber = input("Chceš napsat 5-minutovku (ano/ne)? ")
            time.sleep(0.9)

            if vyber.lower() == "ano":
                print("Obyvatelé ti nabízejí dvě možnosti:")
                time.sleep(0.9)
                print("1. Chceš vědět, jak zachránit město?")
                time.sleep(0.9)
                print("2. Chceš pomoci Veselé s chemtrails?")
                time.sleep(0.9)
                uloha = input("Vyber číslo možnosti: ")
                time.sleep(0.9)

                if uloha == "1":
                    if vysledek_testu is None:
                        print("Abychom zachránili město, musíš nejprve vypočítat správný výsledek testu v lese.")
                    else:
                        print("Musíš vypočítat test v lese, abys mohl zachránit město.")
                    time.sleep(1.2)
                elif uloha == "2":
                    vesela_pomoc = input("Pomohl bys mi přesvědčit všechny chcimíry, že to existuje? (ano/ne) ")
                    if vesela_pomoc.lower() == "ano":
                        print("Díky, tvoje přesvědčení mi stačilo, nic takového neexistuje, umíš dělat jen jednu věc naráz.")
                    elif vesela_pomoc.lower() == "ne":
                        print("Zkapeš! Bašta ti odvolá vládu!")
                    else:
                        print("Neplatná volba. Zkus to znovu.")
                    time.sleep(1.2)
                else:
                    print("Neplatná volba. Zkus to znovu.")
                    time.sleep(1.2)
            elif vyber.lower() == "ne":
                break 
            else:
                print("Neplatná volba. Zkus to znovu.")
                time.sleep(1.2)
    elif volba == "5":
        print("Hra končí. Děkuji za hraní.")
        pokracovat = False
    else:
        print("Neplatná volba. Zkus to znovu.")
