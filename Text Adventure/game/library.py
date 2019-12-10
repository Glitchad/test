"""library for methods"""
from item import Item
from room import Room
from entity import Entity

COMMANDS = {
    "A": ("attack", Entity.attack),
    "P": ("Pick up"),
    "U": ("Use"),
    "N": ("North",),
    "E": ("East",),
    "S": ("South",),
    "W": ("West",),
}

ITEM_DICT = {
    "IT001": Item(
        "IT001", "potion", "The flask is small and contains a murky liquid.", True, True
    )
}

ROOM_DICT = {
    "RM001": Room(
        "RM001",
        "alchemy lab",
        "The lab is full of dusty lab equipment and horrifying experiments.",
        {Item.name("IT001")},
        None
    )
}
