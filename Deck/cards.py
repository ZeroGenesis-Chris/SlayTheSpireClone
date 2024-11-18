class Card:
    def __init__(self, name, card_type, cost, effect):
        self.name = name
        self.card_type = card_type
        self.cost = cost
        self.effect = effect

    def use(self, player, enemy):
        self.effect(player, enemy)  # Apply the card's effect