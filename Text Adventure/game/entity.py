"""details the Entity superclass"""


class Entity:
    """details and initializes properties and methods the entity subclasses use"""

    def __init__(self, name, health, attack_damage, items):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.items = items

    def attack(self):
        """defines attacks"""
        self.health -= self.attack_damage
        print(
            f"You took {self.attack_damage} damage. Your health is now: {self.health}."
        )

    def presentation(self):
        """lets one present an entity's properties"""
        print(
            f"Health: {self.health}. attack damage: {self.attack_damage}. Items: {self.items}."
        )
