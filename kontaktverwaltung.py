kontaktbuch = {
    "Peter": {
        "Telefonnummer": "01234567890",
        "Email": "peter@gmx.de"
    },
    "Laura": {
        "Telefonnummer": "0987654321",
        "Email": "laura@gmx.de"
    }
}

def addcontact(name, nummer, email):
    kontaktbuch[name] = {
        "Telefonnummer": nummer,
        "Email": email
    }



def kontakt():
    print("Was willst du machen im Telefonbuch?")
    inp = input("Neuen Kontakt erstellen - e\nAnzeigen aller Kontakte in einer Liste - a\nSuchen nach einem Kontakt - s\nLöschen eines Kontaktes - l\n")
    if inp == "e":
        name = input("Name: ")
        nummer = input("Nummer: ")
        email = input("Email: ")
        addcontact(name, nummer, email)
        print("Kontakt hinzugefügt!")
        kontakt()
    elif inp == "a":
        for name, details in kontaktbuch.items():
            print(f"Name: {name}")
            print(f"Telefonnummer: {details['Telefonnummer']}")
            print(f"Email: {details['Email']}")
            print("-" * 20)
        kontakt()
    elif inp == "l":
        delname = input("Welchen Namen willst du löschen?")
        del kontaktbuch[delname]
        kontakt()
    elif inp == "s":
        suche = input("Nach welchem Namen willst du suchen?")
        if suche in kontaktbuch:
            print("Kontakt gefunden!")
            print(kontaktbuch[suche])
        else:
            print("Kontakt nicht gefunden!")
        kontakt()
    else:
        print("Ungültige Eingabe!")
        kontakt()
    
kontakt()
