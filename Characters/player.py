class Player:
    def __init__(self):
        self.health = 100
        self.energy = 3
        self.deck = []
        self.hand = []
        self.draw_pile = []
        self.discard_pile = []
    
    def draw_card(self):
        # Example of drawing a card
        pass

    def play_card(self, card):
        # Example of playing a card
        pass

    def take_damage(self, damage):
        self.health -= damage

    def add_card(self, card):
        self.deck.append(card)