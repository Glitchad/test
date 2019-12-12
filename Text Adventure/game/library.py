"""library for methods"""
from item import Item
from room import Room
from player import Player
from enemy import Enemy

COMMANDS = {
    "A": ("attack", Player.attack),
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
        {ITEM_DICT.get("IT001")},
        None,
    )
}

ENEMY_DICT = {
    "EN001": Enemy("EN001", "ghastly ghoul", 10, 3, None),
    "EN002": Enemy("EN002", "scary skeleton", 7, 2, None),
}
