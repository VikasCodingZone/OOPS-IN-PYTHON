#Q19. Encapsulation in Game

class Player:
    def __init__(self, health):
        self.__health = health

    def damage(self, value):
        self.__health -= value

    def get_health(self):
        return self.__health

p = Player(100)
p.damage(30)
print(p.get_health())


# Logic: Player ka health secure rakha gaya hai.