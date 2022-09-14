class Monster:
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    def attack(self, amount):
        print(f'The monster has dealt {amount} of damage')
        self.energy -= 20

    def move(self, speed):
        print(f'The monster has moved in a speed of {speed}')


class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f'The is swimming at a speed of {self.speed}')


class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        super().__init__(health=health, energy=energy, speed=speed,
                         has_scales=has_scales)


# print(Shark.mro())  # method resolution order
shark = Shark(50, 200, 55, 120, False)
print(shark.has_scales)
