from event_manager import player_turn, enemy_turn

def game_loop(player, enemy):
    while player.health > 0 and enemy.health > 0:
      print(f"Player health: {player.health}, Enemy health: {enemy.health}")

      player_turn(player, enemy)
      if enemy.health <= 0:
        print("Player wins!")
        break

      enemy_turn(enemy, player)
      if player.health <= 0:
        print("Enemy wins!")
        break