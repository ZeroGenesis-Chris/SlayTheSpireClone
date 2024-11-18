from Deck.cards import Card

class PowerCard(Card):
    def __init__(self, name, effect, cost=1):
        """
        Initializes a PowerCard instance with a name, an effect (function), and a cost.
        The effect of a power card persists for the rest of the game or until removed.
        """
        super().__init__(name, card_type="Power", cost=cost, effect=effect)

    def use(self, player, enemy):
        """
        Use the power card, triggering its persistent effect.
        This effect is typically applied once and lasts for the rest of the battle.
        """
        
    def __str__(self):
        """
        String representation of the PowerCard for easy display.
        """
        return f"{self.name} (Cost: {self.cost} Energy) - Persistent Effect"