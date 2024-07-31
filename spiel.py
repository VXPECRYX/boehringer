class Pokemon:
    def __init__(self,name,height,weight):
        self._name = name
        self._weight = weight
        self._height = height
        self._health = 20

    def getWeight(self):
        return self._weight
    
    def increaseWeight(self, extraWeight):
        self._weight += extraWeight

    def receiveDamage(self, damage):
        self._health -= damage

    def attack(self, opponent, damage):
        opponent.receiveDamage(damage)

    def getHealth(self):
        return self._health
    


picachu = Pokemon("Picachu", 0.7, 4)
schiggy = Pokemon("Schiggy", 0.4, 7)

picachu.increaseWeight(1)

schiggy.attack(picachu,2)
picachu.getHealth()

print(picachu.getWeight())