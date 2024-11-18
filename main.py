from Game.game import GameLoop, Game

def main():
    game = GameLoop()
    print(game.start_encounter("Cultist"))

    result = game.player_action(game.player.hand[0], game.current_combat.enemy)
    print(result)

if __name__ == "__main__":
    main()