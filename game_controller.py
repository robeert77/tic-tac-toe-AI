class GameController:
    __current_player = 'X' # Simbolul jucatorului curent. Mereu jucatorul care incepe, va fi userul(adica X)
    __game_running = False # Proprietate care ne spune daca jocul ruleaza sau nu

    """
    Contrusctorul clasei GameController

       Args:
           board (BoardGame): Instanta pentru clasa BoardGame
           ai (GameAI): Instanta pentru clasa GameAI
           gui (GameGUI): Instanta pentru clasa GameGUI

       Returns:
           None
    """
    def __init__(self, board, ai, gui):
        self.__game_running = True

        self.__board = board
        self.__ai = ai
        self.__gui = gui

        self.__gui.set_buttons_callback(self.on_click_callback) # Setam functia de callback pentru butoanele din interfata grafica
        self.__gui.set_current_player_label(self.__current_player) # Actualizam label-ul din interfata cu jucatorul curent

    """
    Metoda de callback trigger-uita in momentul in care userul da click pe un buton din interfata

    Args:
        row(int): Indica randul din tabla de joc pe care se afla butonul apasat
        col(int): Indica coloana din tabla de joc pe care se afla butonul apasat

    Returns:
        None
    """
    def on_click_callback(self, row, col):
        if (self.__is_ai_turn()
            or not self.__is_game_running()
            or not self.__board.is_valid_move((row, col))):
            return # Folosit pentru a opri executia metodei

        self.__make_move((row, col))

    """
    Metoda care defineste tot ceea ce trebuie sa se intample in momentul in care se cunoaste pozitia celulei pe care utilizatorul a ales sa o marcheze cu simbolul sau

    Args:
        move (touple(int, int)): Indica pozitia de pe tabla pe care userul doreste sa o marcheze

    Returns:
        None
    """
    def __make_move(self, move):
        self.__update_position(move)

        if self.__need_to_stop_game():
            self.__stop_game()
            return # Folosit pentru a opri executia metodei

        self.__switch_player()
        self.__gui.set_current_player_label(self.__current_player)

        # Presupunem ca dupa fiecare alegere a utilizatorului, calculatorul isi va calcula imediat miscarea
        # In cazul in care jocul deja este considerat finalizat, executia acestuia se va opri in apelul recursiv al aceste metode, de mai jos
        if self.__is_ai_turn():
            move = self.__ai.get_best_move()
            self.__make_move(move) # Apelul recursiv al acestei metode, reprezentand mutarea calculatorului

    """
    Metoda care gestioneaza toate instructiunile necesare pentru a actualiza o pozitie, atat in interfata, cat si in tabla de joc

    Args:
        move (touple(int, int)): Indica pozitia de pe tabla pe care dorim sa o actualizam

    Returns:
        None
    """
    def __update_position(self, move):
        self.__gui.update_button_value(move, self.__current_player)
        self.__board.set_grid_cell(move, self.__current_player)

    """
    Metoda care verifica daca jocul trebuie sa se incheie(in caz de victorie sau de remiza)

    Args:
        None

    Returns:
        bool: True in cazul in care jocul trebuie incheiat, False in caz contrar
    """
    def __need_to_stop_game(self):
        if self.__board.check_winner(): # Avem un castigator
            self.__gui.set_winner_player_label(self.__current_player)
            return True

        if self.__board.is_full(): # Avem o remiza
            self.__gui.set_draw_label()
            return True

        return False

    """
    Metoda care gestioneaza toate instructiunile necesare pentru a ne asigura ca jocul nu mai ruleaza

    Args:
        None

    Returns:
        None
    """
    def __stop_game(self):
        self.__game_running = False

    """
    Metoda care ne spune daca jocul mai ruleaza sau nu

    Args:
        None

    Returns:
        bool: True in cazul in care jocul inca ruleaza, False in caz contrar
    """
    def __is_game_running(self):
        return self.__game_running

    """
    Metoda care ne spune daca este randul calculatorului pentru a efectua o miscare

    Args:
        None

    Returns:
        bool: True in cazul in care jucatorul curent este calculatorul, False in caz contrar
    """
    def __is_ai_turn(self):
        return self.__current_player != 'X'

    """
    Metoda care schimba jucatorul curent

    Args:
        None

    Returns:
        None
    """
    def __switch_player(self):
        self.__current_player = 'O' if self.__current_player == 'X' else 'X'