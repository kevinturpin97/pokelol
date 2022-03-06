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
        self.init = "C'est ce que j'appelle un choix éclairé !"
    
    def get_attack(self):
        if (self.live - 10) <= 0:
            return "Game Over"
        else:
            self.live -= 10
            return "On peut y arriver."
    def get_null(self):
        return "Restons positif !"

class Lux(Champion):

    def __init__(self):
        super().__init__()
        self.init = "C'est ce que j'appelle un choix éclairé !"
    
    def get_attack(self):
        if (self.live - 10) <= 0:
            return "Game Over"
        else:
            self.live -= 10
            return "On peut y arriver."
    def get_null(self):
        return "Restons positif !"