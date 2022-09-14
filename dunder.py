class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy

    def __call__(self):
        print('The monster was called')

    def __add__(self, other):
        return self.health + other

    def __sub__(self, other):
        return self.health - other

    def __str__(self):
        return f'A monster with health {self.health} and energy {self.energy}'

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} of damage was dealt')
        self.energy -= 20
        print(self.energy)

    def move(self, speed):
        print(f'The monster has moved in a speed of {speed}')


monster1 = Monster(100, 80)

print(len(monster1))
print(abs(monster1))
monster1()
print(monster1 + 10)
print(monster1 - 10)
print(monster1)
