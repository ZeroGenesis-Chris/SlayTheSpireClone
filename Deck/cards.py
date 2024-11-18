import random
from enum import Enum, auto

class CardType(Enum):
    ATTACK = auto()
    SKILL = auto()
    POWER = auto()

class Card:
    def __init__(self, name, card_type, cost, description):
        self.name = name
        self.type = card_type
        self.cost = cost
        self.description = description
        self.uuid = random.randint(1000, 9999) #Unique Identifier

    def play(self, player, target=None):
        """Base method to be obverridden by subclasses."""
        raise NotImplementedError("Subclasses must implement play method")
    
    def __str__(self):
        return f"{self.name} (Cost: {self.cost} Energy)"
    
    def __repr__(self):
        return self.__str__()