print("Wilkommen zu ihrer Bank!")
print("Einzahlen - e \nAuszahlen - a\nAbfragen des Kontostandes - k")


def start():
    p =True
    anf=0
    while(p):
        inp = input("Was wollen Sie machen?")
        if inp == "e":
            inp1 = input("Was wollen Sie einzahlen?")
            anf += int(inp1)
     
        elif inp == "a":
            inp2 = input("Was wollen Sie auszahlen?")
            anf -= int(inp2)
            
        elif inp == "k":
            print(anf,"€")
        elif inp == "p":
            exit()
        
        else:
            print("Ungültige Eingabe")

start()

