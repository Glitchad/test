"""details the Entity superclass"""


class Entity:
    """details and initializes properties and methods the entity subclasses use"""

    def __init__(self, name, health, attack_damage, items):
        self.__name = name
        self.__health = health
        self.__attack_damage = attack_damage
        self.__items = items

    def attack(self):
        """defines attacks"""
        self.__health -= self.__attack_damage
        print(
            f"You took {self.__attack_damage} damage. Your health is now: {self.__health}."
        )
        return self.attack

    def presentation(self):
        """lets one present an entity's properties"""
        print(
            f"Name: {self.__name}. Health: {self.__health}. attack damage: {self.__attack_damage}. Items: {self.__items}."
        )
