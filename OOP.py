class Character():

    def __init__(self, x, y, name, className, attack):
        self.hitPoints = 100
        self.coordX = x
        self.coordY = y
        self.name = name
        self.className = className
        self.attack = attack
        self.isDead = False

    def attackEnemy(self):
        print("I attacked you with " + self.attack)

    def getDamage(self, amount):
        if (self.isDead):
            print("GTFO, I am already dead!")
        else:
            self.hitPoints -= amount
            self.isGetKilled()

    def isGetKilled(self):
        if (self.hitPoints <= 0):
            self.isDead = True
            print("Get Killed")

class GoodGuy(Character):

    def __init__(self, x, y, name, className, attack):
        super().__init__(x, y, name, className, attack)
        self.guild = "GOOD GUYS GUILD"

    def attackEnemy(self, character):
        print("I attack you! " + character.name)
        character.getDamage(101)


avgust = GoodGuy(0, 0, "Avgust", "Scholar", "Jelly")

pikachu = GoodGuy(0, 1, "Pikachu", "Pokemon", "PIIIKA!")

print(pikachu.hitPoints)
avgust.attackEnemy(pikachu)
print(pikachu.hitPoints)
avgust.attackEnemy(pikachu)

class Card():
    
    def __init__(self, text, name, manacost, picture):
        self.name = name

class Minion(Card):
    def __init__(self,  text, name, manacost, picture, attack, defence, ability):
        super().__init__(text, name, manacost, picture)
        self.attack = attack
        self.defence = defence
        self.ability = ability

class Ability():
    def __init__(self, name, text):
        self.name = name

    def trigger(self):
        print("When dead, do something!")

class Deathrattle(Ability):









