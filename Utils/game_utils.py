import random

def print_divider(character='-', length=50):
    """
    Prints a divider line, used to separate different sections in the game.
    """
    print(character * length)

def roll_dice(sides=6):
    """
    Simulates rolling a dice with a given number of sides (default is 6).
    """
    return random.randint(1, sides)

def heal_player(player, amount):
    """
    Heals the player by the specified amount, ensuring the health doesn't exceed max health.
    """
    max_health = player.max_health  # Assuming `max_health` is an attribute of the player
    player.health = min(player.health + amount, max_health)
    print(f"{player.__class__.__name__} heals for {amount}. Health: {player.health}/{max_health}")

def apply_damage(entity, damage):
    """
    Applies damage to a given entity (player or enemy), ensuring health doesn't go below 0.
    """
    entity.health = max(0, entity.health - damage)
    print(f"{entity.__class__.__name__} takes {damage} damage. Health: {entity.health}")

def display_stats(player):
    """
    Displays the player's current stats (health, energy, etc.).
    """
    print(f"{player.__class__.__name__} Stats:")
    print(f"Health: {player.health}/{player.max_health}")
    print(f"Energy: {player.energy}")
    print(f"Strength: {player.strength}")
    print(f"Gold: {player.gold}")
    print_divider()

def generate_random_event(events):
    """
    Randomly selects and returns an event from the list of available events.
    """
    return random.choice(events)
