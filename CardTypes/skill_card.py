from Deck.cards import CardType

class SkillCard:
    def __init__(self, name, cost, description=""):
        super().__init__(name, CardType.SKILL, cost, description)

class DefendCard(SkillCard):
    def __init__(self, name="Defend", cost=1, block_amount=5, description="Gain block"):
        super().__init__(name, cost, description)
        self.block_amount = block_amount

    def play(self, player, target=None):
        """Add block to the player"""
        player.gain_block(self.block_amount)
        return f"{self.name} grants {self.block_amount} block"

class EvasionCard(SkillCard):
    def __init__(self, name="Dodge", cost=1, block_amount=3, draw_cards=1, description="Gain block and draw cards"):
        super().__init__(name, cost, description)
        self.block_amount = block_amount
        self.draw_cards = draw_cards

    def play(self, player, target=None):
        """Add block and draw cards"""
        player.gain_block(self.block_amount)
        drawn = player.draw_cards(self.draw_cards)
        return f"{self.name} grants {self.block_amount} block and draws {len(drawn)} cards"