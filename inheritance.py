class Monster:
    # health = 50
    # energy = 100
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} of damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print(f'The monster has moved in a speed of {speed}')


class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Monster.__init__(self, health, energy)
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print('The shark has bitten')

    def move(self):
        print(f'The shark has move in a speed of {self.speed}')


shark = Shark(120, 100, 80)
# print(shark.health)
# print(shark.energy)
# print(shark.speed)


class Scorpion(Monster):
    def __init__(self, poison, scorpion_health, scorpion_energy):
        super().__init__(scorpion_health, scorpion_energy)
        self.poison = poison

    def attack(self):
        print(f'The scorpion has dealt a poison damage of {self.poison}')


scorpion = Scorpion(20, 100, 50)
print(scorpion.health)
scorpion.attack()
scorpion.move(5)
