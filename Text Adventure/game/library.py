"""library for methods"""

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
