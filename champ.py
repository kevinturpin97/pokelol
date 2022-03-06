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
        self.init = "allons la"
    
    def get_attack(self):
        if (self.live - 10) <= 0:
            print("Vi: Mort")
            self.live = 0
            pass
        self.live -= 10
        print("Vi: " + str(self.live))
    def get_null(self):
        print("Vi: " + str(self.live))

class Lux(Champion):

    def __init__(self):
        super().__init__()
        self.init = "C'est ce que j'appelle un choix éclairé !"
    
    def get_attack(self):
        if (self.live - 10) <= 0:
            print("Lux: Mort")
            self.live = 0
            pass
        self.live -= 10
        print("Lux: " + str(self.live))

    def get_null(self):
        print("Lux: " + str(self.live))