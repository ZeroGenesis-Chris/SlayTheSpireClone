from Deck.deck import Deck, DeckManager
from Characters.enemy import Enemy

class Player:
    def __init__(self, name="The Wanderer", maxHealth=80):
        self.name = name
        self.maxHealth = maxHealth
        self.currentHealth = maxHealth
        self.block = 0
        self.energy = 3  # Starting energy per turn
        self.max_energy = 3
 
        # Initialize the deck
        self.deck = DeckManager.create_starter_deck()
        self.hand = []
        self.draw_pile = self.deck.cards
        self.discard_pile = []
   

    def take_damage(self, amount):
        """Reduces incoming damage by block, then reduce HP"""
        actual_damage = max(amount - self.block, 0)
        self.block = max(self.block - amount, 0)
        self.currentHealth = max(self.currentHealth - actual_damage, 0)
        return actual_damage

    def gain_block(self, amount):
        """Add block to reduce incoming damage"""
        self.block += amount

    def draw_cards(self, num_cards=5):
        """"Draw Cards from deck to hand"""
        drawn_cards = self.deck.draw(num_cards)
        self.hand.extend(drawn_cards)
        return drawn_cards

    def play_card(self, card, target=None):
        """Play a card from the hand (apply its effect)"""
        if card.cost > self.energy:
            raise ValueError("Not enough energy to play this card")
        
        # Apply card effect
        result = card.play(self, target)

        # Remove energy and card from hand
        self.energy -= card.cost
        self.hand.remove(card)
        self.discard_pile.append(card)
        
        return result
    
    def reset_turn(self):
        """Reset player's turn"""
        self.energy = self.max_energy
        self.block = 0

        # Discard current hand and draw new cards
        self.discard_pile.extend(self.hand)
        self.hand.clear()
        self.draw_cards()

class EnhancedPlayer(Player):
    def __init__(self, name="The Wanderer", maxHealth=80):
        super().__init__(name, maxHealth)
        self.strength = 0
        self.powers = [] # Track Active power effects

    def apply_strength(self, attack_damage):
        """Apply strength buff to attack damage"""
        return attack_damage + self.strength

    def add_power(self, power):
        """Add a power effect to the player"""
        self.powers.append(power)

    def reset_turn(self):
        """Reset turn and manage power durations"""
        super().reset_turn()

        # Decrement and remove expired powers
        self.powers = [
            power for power in self.powers
            if power.duration > 0
        ]

        # Decrement power durations
        for power in self.powers:
            if power.duration != float("inf"):
                power.duration -= 1