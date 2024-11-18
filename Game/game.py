# game/game.py
from Characters.player import Player
from Characters.enemy import Enemy
from Deck.deck_manager import DeckManager
from event_manager import EventManager
from Cards.attack_card import AttackCard
from Cards.skill_card import SkillCard
from Cards.power_card import PowerCard

class Game:
    def __init__(self):
        """
        Initializes the game with a player, an enemy, and game systems (deck, events).
        """
        self.player = Player()
        self.enemy = Enemy(health=50, attack=5)
        
        # Initialize the deck
        self.create_deck()
        self.deck_manager = DeckManager(self.deck)

        # Initialize events system
        self.event_manager = EventManager(self.player, self.enemy)

        # Game state flags
        self.is_game_over = False

    def create_deck(self):
        """
        Create a deck for the player by adding attack, skill, and power cards.
        """
        self.deck = [
            AttackCard(name="Strike", damage=10),
            SkillCard(name="Defend", effect=lambda player, enemy: player.take_damage(0), cost=1),
            PowerCard(name="Strength Buff", effect=lambda player, enemy: setattr(player, 'strength', player.strength + 2), cost=2)
        ]

    def start_turn(self):
        """
        Starts the player's turn: draws cards, allows actions, and checks for game over.
        """
        if self.is_game_over:
            print("Game Over!")
            return

        print("\n--- Player's Turn ---")
        # Draw 5 cards (or however many you want)
        self.hand = [self.deck_manager.draw_card() for _ in range(5)]
        print(f"Hand: {[card.name for card in self.hand]}")

        # Here you could allow the player to choose an action (e.g., play a card)
        # For now, let's just use the first card in the hand for simplicity
        self.play_card(self.hand[0])

        # After turn, check for enemy action or end conditions
        self.enemy_turn()

        # Trigger an event at the end of the turn (optional)
        self.event_manager.trigger_random_event()

    def play_card(self, card):
        """
        Play a card from the hand (apply its effect).
        """
        print(f"Player plays {card.name}...")
        card.use(self.player, self.enemy)

        # After playing a card, discard it
        self.deck_manager.discard_card(card)

    def enemy_turn(self):
        """
        Executes the enemy's turn, where the enemy attacks or takes action.
        """
        print("\n--- Enemy's Turn ---")
        # For now, let's just have the enemy attack
        self.enemy.attack_player(self.player)
        print(f"Enemy attacks: {self.enemy.attack} damage")

        # Check if player is defeated
        if self.player.health <= 0:
            print("Player has been defeated!")
            self.is_game_over = True

    def run(self):
        """
        Runs the main game loop.
        """
        while not self.is_game_over:
            self.start_turn()
            if self.player.health <= 0:
                self.is_game_over = True
                print("Game Over - Player Defeated")
            elif self.enemy.health <= 0:
                self.is_game_over = True
                print("Game Over - Enemy Defeated")


if __name__ == "__main__":
    game = Game()
    game.run()
