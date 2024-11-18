import random
from deck import Deck

class DeckManager:
    def __init__(self, deck: Deck):
        """
        Initializes the DeckManager with a deck instance.
        Manages the deck, draw pile, and discard pile.
        """
        self.deck = deck
        self.draw_pile = self.deck.cards  # The deck's cards to be drawn
        self.discard_pile = []  # Cards that have been used or discarded

    def shuffle_deck(self):
        """
        Shuffle the draw pile to randomize the deck.
        """
        random.shuffle(self.draw_pile)
        print("Deck shuffled.")

    def draw_card(self):
        """
        Draw a card from the draw pile.
        If the draw pile is empty, shuffle the discard pile back into the draw pile.
        """
        if not self.draw_pile:  # If the draw pile is empty, shuffle discard pile back in
            self.shuffle_deck()
            self.draw_pile = self.discard_pile
            self.discard_pile = []

        card = self.draw_pile.pop()  # Draw the top card from the draw pile
        print(f"Drew {card.name} from the deck.")
        return card

    def discard_card(self, card):
        """
        Add a card to the discard pile after it's been used.
        """
        self.discard_pile.append(card)
        print(f"Discarded {card.name}.")

    def cards_in_deck(self):
        """
        Return the number of cards left in the draw pile.
        """
        return len(self.draw_pile)

    def cards_in_discard_pile(self):
        """
        Return the number of cards in the discard pile.
        """
        return len(self.discard_pile)