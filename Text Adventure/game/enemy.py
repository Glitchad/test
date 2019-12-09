from entity import entity
from random import choice

class enemy(entity):
    enemy_varieties = (
        "a disharmonious harmonica",
        "a terrible terror",
        "an appalling apparation",
    )
    enemy1 = choice(enemy_varieties)
    print(enemy1)
