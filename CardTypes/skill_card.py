from Deck.cards import Card

class SkillCard(Card):
    def __init__(self, name, effect, cost = 1):
        #Call the parent constructor (Card Class)
        super().__init__(name, card_type="Skill", cost=cost, effect=effect)

    def use(self, player, enemy):
        """
        Use the skill card, triggering its effect.
        """

    def block_effect(self, player):
        """
        Defines the effect of the block card.
        This will block the enemy's attack.
        """
    
    def gain_energy(self, player):
        """
        Gain energy from the skill card.
        """
        

    def __str__(self):
        """
        String representation of the SkillCard for easy display.
        """
        return f"{self.name} (Cost: {self.cost} Energy)"