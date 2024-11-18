import random


class Enemy:
    def __init__(self, name, maxHealth, intent=None):
        self.name = name
        self.maxHealth = maxHealth
        self.currentHealth = maxHealth  
        self.block = 0
        self.intent = None

    def take_damage(self, damage):
       """reduce incoming damage by block, then reduce HP"""
       actual_damage = max(damage - self.block, 0)
       self.block = max(self.block - damage, 0)
       self.currentHealth = max(self.currentHealth - actual_damage, 0)
       return actual_damage

    def gain_block(self, amount):
        """Add block to reduce incoming damage"""
        self.block += amount

    def choose_intent(self):
        """Randomly chooses enemy intent for the turn"""
        intents = [
            "Attack",
            "Defend",
            "Special_move"
        ]
        self.intent = random.choice(intents)
        return self.intent
    
    def execute_intent(self, player):
        """Executes the chosen intent for the turn"""
        damage = 0 # Initializing a damage value to 0

        if self.intent == "Attack":
            damage = random.randint(5, 15) # Randomises the damage value
            player.take_damage(damage)
            return f"{self.name} attacks for {damage} damage."
        
        elif self.intent == "Defend":
            blockAmount = random.randint(5, 10) # Randomises the block value
            player.take_damage(damage)
            return f"{self.name} defends with {blockAmount} block."
        
        elif self.intent == "Special_move":
            # Example of a more complex intent
            damage = random.randint(10, 20) # Randomises the damage value
            player.take_damage(damage)
            self.gain_block(5)
            return f"{self.name} uses a special move for {damage} damage and gains 5 block!"

    def is_defeated(self):
        """Checks if the enemy is defeated"""
        return self.currentHealth <= 0
        
class EnhancedEnemy(Enemy):
    def __init__(self, name, maxHealth, intent=None):
        super().__init__(name, maxHealth, intent)
        self.vulnerable = 0
        self.powers = []

    def take_damage(self, damage):
        """Modified damage calculation to account for vulnerability"""
        if self.vulnerable > 0:
            # increase damage by 50% if vulnerable
            amount = int(amount * 1.5)
            self.vulnerable = max(0, self.vulnerable - 1)
            
        return super().take_damage(damage)
    
    def add_power(self, power):
        """Add a power effect to the enemy"""
        self.powers.append(power)

    def reset_turn(self):
        """Reset turn and manage power durations"""
        # Decrement and remove expired powers
        self.powers = [
            power for power in self.powers
            if power.duration > 0
        ]

        # Decrement power durations
        for power in self.powers:
            if power.duration != float("inf"):
                power.duration -= 1