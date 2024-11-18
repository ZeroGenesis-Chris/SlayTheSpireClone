from cards import Card

class AttackCard(Card):
    def __init__(self, name, damage, cost = 1):
        #Call the parent constructor (Card Class)
        super().__init__(name, card_type="Attack", cost=cost, effect=self.attack_effect)
        self.damage = damage # Define how much damage the card does

    def attack_effect(self, player, enemy):
        """
        Defines the effect of the attack card.
        This will deal damage to the enemy.
        """
      
    def __str__(self):
        """
        String representation of the AttackCard for easy display.
        """
        return f"{self.name} (Cost: {self.cost} Energy) - Deals {self.damage} damage"