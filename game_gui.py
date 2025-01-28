import tkinter as tk

class GameGUI(object):
    __buttons = None

    def __init__(self, board_size):
        self.__board_size = board_size
        self.__window = tk.Tk()
        self.__window.title("Tic Tac Toe")

        self.__label = tk.Label(self.__window, text='', font=('normal', 20))
        self.__label.pack()

        self.__buttons_frame = tk.Frame(self.__window)
        self.__buttons_frame.pack()

        self.__create_buttons()

    def __create_buttons(self):
        self.__buttons = [[None for _ in range(self.__board_size)] for _ in range(self.__board_size)]

        for i in range(self.__board_size):
            for j in range(self.__board_size):
                self.__buttons[i][j] = tk.Button(
                    self.__buttons_frame, text='',
                    font=('normal', 40),
                    width=5,
                    height=2,
                )
                self.__buttons[i][j].grid(row=i, column=j)

    def set_buttons_callback(self, callback):
        for row in range(self.__board_size):
            for col in range(self.__board_size):
                self.__buttons[row][col].config(command=lambda r=row, c=col: callback(r, c))

    def update_button_value(self, move, value):
        row, col = move
        self.__buttons[row][col]['text'] = value

    def set_draw_label(self):
        self.__set_label(f'Game ended with a draw!')

    def set_winner_player_label(self, player):
        self.__set_label(f'Player {player} wins!')

    def set_current_player_label(self, player):
        self.__set_label(f'Current Player: {player}')

    def __set_label(self, message):
        self.__label.config(text=message)
        self.__window.update()

    def run(self):
        self.__window.mainloop()
