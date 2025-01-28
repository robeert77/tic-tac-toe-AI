import time

class GameController:
    __current_player = 'X'
    __game_running = False

    def __init__(self, board, ai, gui):
        self.__game_running = True

        self.__board = board
        self.__ai = ai

        self.__gui = gui
        self.__gui.set_buttons_callback(self.on_click_callback)
        self.__gui.set_current_player_label(self.__current_player)

    def on_click_callback(self, row, col):
        if (self.__is_ai_turn()
            or not self.__is_game_running()
            or not self.__board.is_valid_move((row, col))):
            return

        self.__make_move((row, col))

    def __make_move(self, move):
        self.__update_position(move)

        if self.__need_to_stop_game():
            self.__stop_game()
            return

        self.__switch_player()
        self.__gui.set_current_player_label(self.__current_player)

        if self.__is_ai_turn():
            time.sleep(0.4)
            move = self.__ai.get_best_move()
            self.__make_move(move)

    def __update_position(self, move):
        self.__gui.update_button_value(move, self.__current_player)
        self.__board.set_grid_cell(move, self.__current_player)

    def __need_to_stop_game(self):
        if self.__board.check_winner():
            self.__gui.set_winner_player_label(self.__current_player)
            return True

        if self.__board.is_full():
            self.__gui.set_draw_label()
            return True

        return False

    def __stop_game(self):
        self.__game_running = False

    def __is_game_running(self):
        return self.__game_running

    def __is_ai_turn(self):
        return self.__current_player != 'X'

    def __switch_player(self):
        self.__current_player = 'O' if self.__current_player == 'X' else 'X'