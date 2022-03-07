import random


class Champion:

    global live, force, shield, magic

    live = 100                 #####################################
    force = 1                  #  force > shield || magic > force  #
    shield = 2                 #  shield > magic ||                #
    magic = 3                  #####################################

    def __init__(self):
        self.live = live
        self.force = force
        self.shield = shield
        self.magic = magic

    def setLive(self, live):
        self.live = live
    
class Vi(Champion):

    def __init__(self):
        super().__init__()
        self.init = "Allons la dalon"
    
    def get_attack(self):
        list_attack = [
            "Chut... Je charge mon laser.",
            "Un mage brillant ? Non, je ne suis qu'un mage ordinaire."
        ]
        if (self.live - 10) <= 0:
            print("Vi: Mort")
            self.live = 0
            return "Au nom de Demacia, je vous punirai."
        else:
            self.live -= 10
            print("Vi: " + str(self.live))
            return random.choice(list_attack)

    def get_null(self):
        list_null = [
            "J'adore qu'un plan se déroule sans accrocs.",
            "On peut y arriver.",
            "Restez positif !",
            "Décision lumineuse."
        ]
        print("Vi: " + str(self.live))
        return random.choice(list_null)

    def get_defend(self):
        list_defend = [
            "Notre tactique est supérieure.",
            "Concentrons-nous sur le combat.",
            "Allumons-les.",
            "Bannissons les ombres.",
            "J'éclaire l'ennemi."
        ]
        return random.choice(list_defend)

class Lux(Champion):

    def __init__(self):
        super().__init__()
        self.init = "C'est ce que j'appelle un choix éclairé !"
    
    def get_attack(self):
        list_attack = [
            "Chut... Je charge mon laser.",
            "Que Démacia soit avec moi"
        ]
        if (self.live - 10) <= 0:
            print("Lux: Mort")
            self.live = 0
            return "Au nom de Demacia, je vous punirai."
        else:
            self.live -= 10
            print("Lux: " + str(self.live))
            return random.choice(list_attack)

    def get_null(self):
        list_null = [
            "J'adore qu'un plan se déroule sans accrocs.",
            "On peut y arriver.",
            "Restez positif !",
            "Décision lumineuse."
        ]
        print("Lux: " + str(self.live))
        return random.choice(list_null)

    def get_defend(self):
        list_defend = [
            "Notre tactique est supérieure.",
            "Concentrons-nous sur le combat.",
            "Allumons-les.",
            "Bannissons les ombres.",
            "J'éclaire l'ennemi."
        ]
        return random.choice(list_defend)