"""#details enemy class module"""
from random import choice
from entity import Entity


class Enemy(Entity):
    """details enemy class"""

    enemy_varieties = (
        "a disharmonious harmonica",
        "a terrible terror",
        "an appalling apparation",
    )
