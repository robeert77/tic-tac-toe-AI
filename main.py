from game_controller import GameController
from game_gui import GameGUI
from board_game import BoardGame
from game_ai import GameAI

def main():
    try:
        board_size = int(input("Enter the board size (3-10): "))
        if 3 <= board_size <= 10:
            board = BoardGame(board_size)
            gui = GameGUI(board_size)
            ai = GameAI(board)
            game = GameController(board, ai, gui)
            gui.run()
        else:
            print("Please enter a number between 3 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()