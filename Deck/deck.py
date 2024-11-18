import random

class Deck:
    def __init__(self, initial_cards=None):
        self.cards = initial_cards or []
        self.discard_pile = []

    def add_card(self, card):
        """Add a card to the deck"""
        self.cards.append(card)

    def remove_card(self, card):
        """Remove a specific card from the deck"""
        self.cards.remove(card)

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)

    def draw(self, num_cards=1):
        """Draw specified number of cards"""
        drawn_cards = []
        for _ in range(num_cards):
            if not self.cards:
                # Reshuffle discard pile if deck is empty
                self.cards = self.discard_pile.copy()
                self.discard_pile.clear()
                self.shuffle()
            
            if self.cards:
                drawn_cards.append(self.cards.pop())
        
        return drawn_cards

    def discard(self, card):
        """Move a card to the discard pile"""
        self.discard_pile.append(card)

class DeckManager:
    @staticmethod
    def create_starter_deck():
        """Create a basic starter deck for the player"""
        from CardTypes.attack_card import AttackCard
        
        starter_deck = Deck()
        # Add some basic strike cards
        for _ in range(5):
            starter_deck.add_card(AttackCard("Strike", 1, 6, "Deal 6 damage"))
        
        starter_deck.shuffle()
        return starter_deck