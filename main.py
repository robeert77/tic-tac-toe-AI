from game_controller import GameController
from game_gui import GameGUI
from board_game import BoardGame
from game_ai import GameAI

"""
Functia main, care se ocupa de pornirea aplicatiei

Args:
    None
    
Returns:
    None
"""
def main():
    try:
        board_size = int(input("Enter the board size (3-10): "))
        if 3 <= board_size <= 10: # Validari pentru dimensiunea tablei de joc
            board = BoardGame(board_size) # Initalizam obiectul board, de tipul GameBoard
            gui = GameGUI(board_size) # Initalizam obiectul gui, de tipul GameGUI
            ai = GameAI(board) # Initalizam obiectul ai, de tipul GameAI
            game = GameController(board, ai, gui) # Initalizam obiectul game, de tipul GameController
            gui.run() # Pornim interfata grafica
        else:
            print("Please enter a number between 3 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# La executia programului, apelam metoda main()
# Astfel, tot codul este in clase si functii
if __name__ == "__main__":
    main()