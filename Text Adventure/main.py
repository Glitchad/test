class Entity:
    def __init__(self, health, attack_damage, items):
        self.health = health
        self.attack_damage = attack_damage
        self.items = items
        return

    def doDamage(self):
        self.health -= self.attack_damage
        print(
            f"You took {self.attack_damage} damage. Your health is now: {self.health}."
        )
        return

    def Presentation(self):
        print(
            f"Health: {self.health}. Attack damage: {self.attack_damage}. Items: {self.items}."
        )
        return


class Player(Entity):
    pass


class Enemy(Entity):
    pass


class NPC(Entity):
    pass

Ogre = Enemy(5, 2, 0)

MainPlayer = Player(10, 3, 0)


MainPlayer.Presentation()
