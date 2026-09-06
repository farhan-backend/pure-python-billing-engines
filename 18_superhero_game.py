class Hero:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.amount = amount
        
        if self.hp > 0:
            self.hp -= self.amount

            if self.hp < 0:
                self.hp = 0
        
        else:
            return self.hp

    def heal(self, amount):

        self.hp += amount
        return self.hp

    def is_alive(self):
        
        if self.hp > 0:
            return True
        
        else:
            return False


p1 = Hero("Farhan")
print(f"Hero Created!\n\nName: {p1.name}\n\nStarting HP: {p1.hp}/100\n")

p1.take_damage(80)
print(f"Took 30 damage! HP: {p1.hp}/100\n")

p1.heal(15)
print(f"Healed 15 HP! HP: {p1.hp}/100\n")

p1.heal(90)
print(f"Healed 130 HP! HP: {p1.hp}/100\n")

p1.take_damage(80)
print(f"Took 30 damage! HP: {p1.hp}/100\n")

print(f"Is {p1.name} alive: {p1.is_alive()}")