class Hero:
    def __init__(self, name, power, energy):
        self.name = name
        self.power = power
        self.energy = energy
    def attack(self):
        return self.power
    def take_damage(self, damage):
        self.energy -= damage
        if self.energy < 0:
            self.energy = 0
    def show_status(self):
        print(f"{self.name}: Energy = {self.energy}")
class SpeedHero(Hero):
    def attack(self):
        print(f"{self.name} uses Lightning Dash")
        return self.power + 5
class FireHero(Hero):
    def attack(self):
        print(f"{self.name} launches Fire Blast")
        return self.power + 10
    
hero1 = SpeedHero("Flash", 20, 100)
hero2 = FireHero("Inferno", 25, 100)

while hero1.energy > 0 and hero2.energy > 0:
    damage = hero1.attack()
    hero2.take_damage(damage)
    hero2.show_status()
    if hero2.energy == 0:
        print(f"{hero1.name} wins!")
        break
    damage = hero2.attack()
    hero1.take_damage(damage)
    hero1.show_status()
    if hero1.energy == 0:
        print(f"{hero2.name} wins!")
        break