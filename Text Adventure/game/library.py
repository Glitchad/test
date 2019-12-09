from random import choice
from entity import entity

COMMANDS = {
    "A": ("attack", entity.attack),
    "P": ("Pick up"),
    "U": ("Use"),
    "N": ("North",),
    "E": ("East",),
    "S": ("South",),
    "W": ("West",),
}
