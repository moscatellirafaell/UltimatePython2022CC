class Monster:
    health = 90
    energy = 40

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} of damage was dealt')
        self.energy -= 20
        print(self.energy)

    def move(self, speed):
        print(f'The monster has moved in a speed of {speed}')


monster1 = Monster()

monster1.move(40)
