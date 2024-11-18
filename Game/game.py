# game/game.py
from Characters.player import Player
from Characters.enemy import Enemy

class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn_count = 0
        self.combat_log = []

    def start_combat(self):
        """Initialize combat and return initial state"""
        self.player.reset_turn()
        self.enemy.choose_intent()
        return f"Combat begins! {self.enemy.name} Appears with intent: {self.enemy.intent}"
    
    def player_turn(self, card, target=None):
        """Process player's turn"""
        try:
            result = self.player.play_card(card, target)
            self.combat_log.append(result)
            return result
        except ValueError as e:
            return str(e)
        
    def enemy_turn(self):
        """Process enemy's turn"""
        intent_result = self.enemy.execute_intent(self.player)
        self.combat_log.append(intent_result)

        # Check if player is defeated
        if self.player.currentHealth <= 0:
            return "Player has been defeated!"

        # Reset enemy intent for next turn
        self.enemy.choose_intent()
        return intent_result
    
    def is_combat_over(self):
        """Check if combat is over"""
        if self.player.currentHealth <= 0:
            return "Player has been defeated!"
        elif self.enemy.is_defeated():
            return "Enemy has been defeated!"
        
        return None


class GameLoop:
    def __init__(self):
        self.player = Player()
        self.current_combat = None

    def start_encounter(self, enemy):
        """Start a new combat encounter"""
        enemy = Enemy("Cultist", maxHealth=10)
        self.current_combat = Game(self.player, enemy)
        return self.current_combat.start_combat()
    
    def player_action(self, card, target=None):
        """Process player's action"""
        if not self.current_combat:
            return "No combat in progress"
        
        # Player's turn
        action_result = self.current_combat.player_turn(card, target)

        # Enemy's turn if player's turn was successful
        if "Not enough energy" not in action_result:
            enemy_result = self.current_combat.enemy_turn()

        # Check combat status
        combat_status = self.current_combat.is_combat_over()

        return {
            "Player_action": action_result,
            "Enemy_action": enemy_result if "enemy_result" in locals() else None,  
            "Combat_status": combat_status
        }

