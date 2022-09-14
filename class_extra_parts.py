class Monster:
    """A monster that has some attributes"""
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

        # private attributes
        self._id = 5

    def attack(self, amount):
        print(f'The monster has dealt a damage of {amount}')
        self.energy -= 20

    def move(self, speed):
        print(f'The monster has moved in a speed of {speed}')


monster = Monster(20, 10)

# hasattr and setattr
if hasattr(monster, 'health'):
    print(f'The monster has {monster.health} health')

setattr(monster, 'weapon', 'Sword')
print(monster.weapon)

new_attributes = (['weapon', 'Axe'], ['armor', 'Shield'], ['consumable', 'Potion'])
for attr, value in new_attributes:
    setattr(monster, attr, value)
print(vars(monster))

# doc
print(monster.__doc__)
help(monster)
