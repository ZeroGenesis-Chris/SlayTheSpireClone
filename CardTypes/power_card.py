from Deck.cards import Card, CardType

class PowerCard(Card):
    def __init__(self, name, cost, description=""):
        super().__init__(name, CardType.POWER, cost, description)
        self.duration = float('inf')  # Default to permanent effect

class StrengthPowerCard(PowerCard):
    def __init__(self, name="Strength", cost=1, strength_amount=2, description="Increase attack damage"):
        super().__init__(name, cost, description)
        self.strength_amount = strength_amount

    def play(self, player, target=None):
        """Apply strength buff to player"""
        # Note: This would require tracking player's strength in the Player class
        player.strength = getattr(player, 'strength', 0) + self.strength_amount
        return f"{self.name} increases attack damage by {self.strength_amount}"

class VulnerablePowerCard(PowerCard):
    def __init__(self, name="Vulnerable", cost=1, vulnerable_amount=2, description="Apply vulnerability to enemy"):
        super().__init__(name, cost, description)
        self.vulnerable_amount = vulnerable_amount

    def play(self, player, target=None):
        """Apply vulnerability to target"""
        if not target:
            raise ValueError("Vulnerable power card requires a target")
        
        # Note: This would require adding vulnerability tracking to Enemy class
        target.vulnerable = getattr(target, 'vulnerable', 0) + self.vulnerable_amount
        return f"{self.name} makes {target.name} vulnerable for {self.vulnerable_amount} turns"

class ConstantPowerCard(PowerCard):
    def __init__(self, name, cost, effect_func, description=""):
        """
        A more flexible power card that can apply custom effects
        
        :param effect_func: A function that takes (player, target) and applies an effect
        """
        super().__init__(name, cost, description)
        self.effect_func = effect_func

    def play(self, player, target=None):
        """Apply a custom effect"""
        return self.effect_func(player, target)