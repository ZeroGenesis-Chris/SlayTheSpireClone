# STSClone
Python Slay the Spire clone base template

1. Cards/: 

This directory will hold all the classes related to cards.
card.py: The base class for all cards, containing properties common to all types of cards like name, cost, etc.
attack_card.py, skill_card.py, power_card.py: Derived classes for specific types of cards that implement different effects.

2. characters/:

This directory contains classes for the main characters in the game (e.g., Player, Enemy).
player.py: Contains the Player class with health, energy, deck, and methods related to player actions.
enemy.py: Contains the Enemy class with health, attack methods, etc.

3. deck/:

This directory handles deck-related operations like drawing cards and shuffling.
deck.py: Contains the main Deck class that holds a list of cards.
deck_manager.py: Responsible for managing the deck, including drawing cards, shuffling, and managing the discard pile.

4. game/:

Contains the core game logic, including managing the game loop, handling events, and updating the game state.
game.py: The main game state manager, potentially initializing the player, enemies, and the deck.
game_loop.py: The function for the main game loop, where turns alternate between the player and enemies.
event_manager.py: This can be used to manage random events or other global game-wide events (e.g., upgrading cards, relics, etc.).

5. utils/:

This folder contains helper utilities or functions that might be used across the game.
game_utils.py: For general utility functions, like checking if the game is over, managing turn cycles, etc.

6. main.py:

The main entry point of the game. This is where the game is initialized, the main game loop is started, and you control the flow of the game. It will import classes from other modules as necessary to bring everything together.



