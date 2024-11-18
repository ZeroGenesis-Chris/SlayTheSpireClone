class Enemy:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self, player):
        player.take_damage(self.attack)