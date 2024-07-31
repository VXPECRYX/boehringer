import random

print("Willkommen zum Snackautomat, das sind alle Produkte und ihre Anzahl:")

produkte = ["Snickers", "Twicks", "Dublo", "Mars", "Bounty"]
preise = [1.5, 1.2, 1.3, 1.4, 1.6] 
menge = [7, 4, 3, 4, 8]  

guthaben = 0

def automat():
    global guthaben
    p = True
    while p:
        print("Was willst du machen?")
        print("Guthaben einzahlen - e\nKontostand abfragen - k\nVerfügbare Produkte abfragen - p\nEin Produkt kaufen - kaufen")
        inp = input("")
        if inp == "e":
            print("Wieviel willst du einzahlen?")
            inp1 = input("")
            guthaben += int(inp1)
        elif inp == "k":
            print("Dein Kontostand beträgt " + str(guthaben) + "€")
        elif inp == "p":
            for i in range(0, 5):
                print(f"Es gibt {menge[i]} {produkte[i]} zum Preis von {preise[i]}€")
        elif inp == "kaufen":
            print("Welches Produkt willst du kaufen?")
            for i in range(0, 5):
                print(f"{produkte[i]} - {i} ({preise[i]}€)")
            eingabe = int(input("Gebe eine Zahl ein."))
            if 0 <= eingabe < len(produkte):
                menge1 = int(input("Wie oft?"))
                gesamtpreis = preise[eingabe] * menge1
                if menge[eingabe] >= menge1:
                    if guthaben >= gesamtpreis:
                        menge[eingabe] -= menge1
                        guthaben -= gesamtpreis
                        print(f"Du hast {menge1} {produkte[eingabe]} für {gesamtpreis}€ gekauft.")
                    else:
                        print("Nicht genug Guthaben.")
                else:
                    print("Nicht genug auf Lager.")
            else:
                print("Ungültige Eingabe.")
        else:
            print("Ungültige Auswahl. Bitte versuche es erneut.")

automat()
