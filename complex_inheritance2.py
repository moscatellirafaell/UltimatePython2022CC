class Monster:
    # health = 100
    # mana = 50
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    def move(self):
        print(f'The {type(self)} has moved')


class Dragon(Monster):
    def __init__(self, fire, dragon_health):
        super().__init__(health=dragon_health, mana=monster.mana)
        self.fire = fire

    def fly(self):
        print(f'The {type(self)} has flown')


class Wyrm(Dragon, Monster):
    def __init__(self, scales, wyrm_health, wyrm_mana):
        super().__init__(fire=dragon.fire, dragon_health=wyrm_health)
        self.scales = scales
        self.mana = wyrm_mana

    def fly(self):
        print(f"{type(self)} can't fly")


monster = Monster(150, 50)
dragon = Dragon(20, 200)
wyrm = Wyrm(100, 100, 0)
print(wyrm.mana)
wyrm.move()
wyrm.fly()
