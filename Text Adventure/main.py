import random

class Entity:
    def __init__(self, name, health, attack_damage, items):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.items = items

    def Attack(self):
        self.health -= self.attack_damage
        print(
            f"You took {self.attack_damage} damage. Your health is now: {self.health}."
        )

    def Presentation(self):
        print(
            f"Health: {self.health}. Attack damage: {self.attack_damage}. Items: {self.items}."
        )


COMMANDS = {
    "A": ("Attack", Entity.Attack),
    "P": ("Pick up"),
    "U": ("Use"),
    "N": ("North",),
    "E": ("East",),
    "S": ("South",),
    "W": ("West",),
}


class Player(Entity):
    pass

p = Player(input("Enter your name: "), 10, 3, 0)


class Enemy(Entity):
    EnemyVarieties = ("a disharmonious harmonica", "a terrible terror", "an appalling apparation")
    Enemy1 = random.choice(EnemyVarieties)
    print(Enemy1)

e = Enemy("", 5, 2, 0)

class NPC(Entity):
    pass
