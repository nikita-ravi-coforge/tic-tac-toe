import random

from ai import EasyAI, HardAI
from game import Game


def read_move(text):
    """Turn what the player typed, like "2 3", into a row, col.

    Return None if the text is not two whole numbers. This is the only place
    that converts from the player's numbers (from 1) to code numbers (from 0).
    """
    parts = text.split()
    if len(parts) != 2:
        return None
    if not (parts[0].isdigit() and parts[1].isdigit()):
        return None
    return int(parts[0]) - 1, int(parts[1]) - 1


def ask_choice(prompt, options):
    """Keep asking until the player types one of the options."""
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print(f"Please type one of: {', '.join(options)}")


def choose_opponent():
    """Return None for two players, or an AI object for versus computer."""
    print("1) Two players")
    print("2) Versus computer")
    mode = ask_choice("Choose a mode: ", ["1", "2"])
    if mode == "1":
        return None

    print("1) Easy")
    print("2) Hard")
    level = ask_choice("Choose a level: ", ["1", "2"])
    rng = random.Random()
    if level == "1":
        return EasyAI(rng)
    return HardAI(rng)


def main():
    print("Welcome to Tic-Tac-Toe!")
    game = Game(choose_opponent())
    print()
    print(game.board)

    while not game.is_over:
        if game.is_computer_turn():
            (row, col), status = game.play_computer_move()
            print(f"\nComputer (O) plays {row + 1} {col + 1}")
        else:
            text = input(f"\nPlayer {game.current_player}, enter row and column (1-3): ")
            move = read_move(text)
            if move is None:
                print("Please type two numbers, like 2 3.")
                continue
            status = game.play_move(*move)
            if status == "invalid":
                print("That cell is taken or off the board. Try again.")
                continue
        print(game.board)

    if game.winner:
        print(f"\n{game.winner} wins!")
    else:
        print("\nIt's a draw!")


if __name__ == "__main__":
    main()