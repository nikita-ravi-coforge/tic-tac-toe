"""Menus, prompts, and printing ad per req. The only file that uses print() and input()."""

from game import Game


def read_move(text):
    """Turn what the player typed, like "2 3", into a row, col.

    Return None if the text is not two whole numbers.
    """
    parts = text.split()
    if len(parts) != 2:
        return None
    if not (parts[0].isdigit() and parts[1].isdigit()):
        return None
    return int(parts[0]) - 1, int(parts[1]) - 1


def main():
    print("Welcome to Tic-Tac-Toe!")
    game = Game()
    print()
    print(game.board)

    while not game.is_over:
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