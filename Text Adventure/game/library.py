from random import choice


class entity:
    def __init__(self, name, health, attack_damage, items):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.items = items

    def attack(self):
        self.health -= self.attack_damage
        print(
            f"You took {self.attack_damage} damage. Your health is now: {self.health}."
        )

    def presentation(self):
        print(
            f"Health: {self.health}. attack damage: {self.attack_damage}. Items: {self.items}."
        )


COMMANDS = {
    "A": ("attack", entity.attack),
    "P": ("Pick up"),
    "U": ("Use"),
    "N": ("North",),
    "E": ("East",),
    "S": ("South",),
    "W": ("West",),
}


class player(entity):
    super().__init__()

    def pick_up(self):
        pass

    def use(self):
        pass

    def movement(self):
        pass


class enemy(entity):
    enemy_varieties = (
        "a disharmonious harmonica",
        "a terrible terror",
        "an appalling apparation",
    )
    enemy1 = choice(enemy_varieties)
    print(enemy1)


class Npc(entity):
    pass
