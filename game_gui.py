import tkinter as tk

class GameGUI(object):
    __buttons = None # Matrice care reprezinta obiectele de tip Button din cadrul interfetei grafice

    """
    Contrusctorul clasei GameGUI

        Args:
            board_size (int): Indica dimensiunea tablei de joc, selectata de catre utilizator

        Returns:
            None
    """
    def __init__(self, board_size):
        self.__board_size = board_size
        self.__window = tk.Tk() # Instantam obiectul de tip Tk()
        self.__window.title("Tic Tac Toe") # Definim titlul ferestrei din interfata grafica

        self.__label = tk.Label(self.__window, text='', font=('normal', 20)) # Construim labelul din fereastra, folosit pentru a afisa informatii
        self.__label.pack()

        self.__buttons_frame = tk.Frame(self.__window) # Construim un frame in fereastra interfetei. Acest frame va contine butoanele care reprezinta tabla jocului
        self.__buttons_frame.pack()

        self.__create_buttons()

    """
    Metoda privata care creaza butoanele folosite ca si tabla de joc in interfata grafica

    Args:
        None

    Returns:
        None
    """
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

    """
    Metoda care defineste functia de callback pentru momentul in care un buton este apasat

    Args:
        callback(Callable(row, col): Metoda de callback, care dorim sa fie trigger-uita in momentul in care este apasat un buton din interfata

    Returns:
        None
    """
    def set_buttons_callback(self, callback):
        for row in range(self.__board_size):
            for col in range(self.__board_size):
                self.__buttons[row][col].config(command=lambda r=row, c=col: callback(r, c))

    """
    Metoda care actualizeaza continutul butoanleor din interfata

    Args:
        move (touple(int, int)): Indica pozitia dbutonului pentru care actualizam continutul
        value(str): Simbolul jucatorului care a facut mutarea (X sau O)

    Returns:
        None
    """
    def update_button_value(self, move, value):
        row, col = move
        self.__buttons[row][col]['text'] = value

    """
    Metoda care seteaza label-ul din interfata grafica,faptul ca jocul s-a terminat cu remiza, apeland metoda privata cu mesajul gata definit

    Args:
        player(str): Simbolul jucatorului curent (X sau O)

    Returns:
        None
    """
    def set_draw_label(self):
        self.__set_label(f'Game ended with a draw!')

    """
    Metoda care seteaza label-ul din interfata grafica, indicand jucatorul castigator, apeland metoda privata cu mesajul gata definit

    Args:
        player(str): Simbolul jucatorului care a castigat (X sau O)

    Returns:
        None
    """
    def set_winner_player_label(self, player):
        self.__set_label(f'Player {player} wins!')

    """
    Metoda care seteaza label-ul din interfata grafica, indicand jucatorul curent, apeland metoda privata cu mesajul gata definit

    Args:
        player(str): Simbolul jucatorului curent (X sau O)

    Returns:
        None
    """
    def set_current_player_label(self, player):
        self.__set_label(f'Current Player: {player}')

    """
    Metoda privata care seteaza label-ul din interfata grafica

    Args:
        message(str): Mesajul pe care dorim sa il afisam in interfata

    Returns:
        None
    """
    def __set_label(self, message):
        self.__label.config(text=message)
        self.__window.update()

    """
    Porneste interfata Tkinter, si o menttine deschisa

    Args:
        None

    Returns:
        None
    """
    def run(self):
        self.__window.mainloop()
