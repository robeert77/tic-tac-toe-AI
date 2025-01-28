import math

class GameAI(object):
    __depth = 4
    __ai_moves = 0

    def __init__(self, board, ai_player='O', human_player = 'X'):
        self.__board_game = board
        self.__ai_player = ai_player
        self.__human_player = human_player

        if self.__board_game.get_board_size() == 3:
            self.__depth = 6

    def get_best_move(self):
        board = self.__board_game.clone_instance()

        best_score = -math.inf
        best_move = None

        for i in range(board.get_board_size()):
            for j in range(board.get_board_size()):
                if board.is_valid_move((i, j)):
                    board.set_grid_cell((i, j), self.__ai_player)
                    score = self.__minimax(board, self.__depth, -math.inf, math.inf, False)
                    board.clear_grid_cell((i, j))

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        self.__increase_depth()
        return best_move

    def __increase_depth(self):
        self.__ai_moves += 1
        increase_at_nr_steps = self.__board_game.get_board_size() - 2
        self.__depth += (self.__depth < 7 and self.__ai_moves % increase_at_nr_steps == 0)

    def __evaluate_position(self, board, depth):
        winner = board.check_winner()

        if winner == self.__ai_player:
            return 10
        elif winner == self.__human_player:
            return -10
        elif board.is_full() or depth == 0:
            return 0

        return None

    def __minimax(self, board, depth, alpha, beta, is_maximizing):
        position_score = self.__evaluate_position(board, depth)
        if position_score is not None:
            return position_score + depth

        if is_maximizing:
            best_score = -math.inf
            for i in range(board.get_board_size()):
                for j in range(board.get_board_size()):
                    if board.is_valid_move((i, j)):
                        board.set_grid_cell((i, j), self.__ai_player)
                        score = self.__minimax(board, depth - 1, alpha, beta, False)
                        board.clear_grid_cell((i, j))
                        best_score = max(score, best_score)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = math.inf
            for i in range(board.get_board_size()):
                for j in range(board.get_board_size()):
                    if board.is_valid_move((i, j)):
                        board.set_grid_cell((i, j), self.__human_player)
                        score = self.__minimax(board, depth - 1, alpha, beta,True)
                        board.set_grid_cell((i, j), '')
                        best_score = min(score, best_score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return best_score
