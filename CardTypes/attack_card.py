from Deck.cards import Card, CardType

class AttackCard(Card):
    def __init__(self, name, cost, damage, description=""):
        super().__init__(name, CardType.ATTACK, cost, description)
        self.damage = damage

    def play(self, player, target):
        """Apply damage to the target"""
        if not target:
            raise ValueError("Attack card requires a target")
        target.take_damage(self.damage)
        return f"{self.name} deals {self.damage} damage to {target.name}"