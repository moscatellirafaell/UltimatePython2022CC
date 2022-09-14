def update_health(amount):
    monster.health += amount


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount

    def get_damage(self, amount):
        self.health -= amount


monster = Monster(100, 50)
update_health(20)
monster.update_energy(10)
print(monster.health)
print(monster.energy)


class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)


hero = Hero(15, monster)
hero.attack()
print(monster.health)