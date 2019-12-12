"""details the Entity superclass"""


class Entity:
    """details and initializes properties and methods the entity subclasses use"""

    def __init__(self, code, name, health, attack_damage, items):
        self.__code = code
        self.__name = name
        self.__health = health
        self.__attack_damage = attack_damage
        self.__items = items

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def attack_damage(self):
        return self.__attack_damage

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
