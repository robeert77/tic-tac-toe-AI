import math

class GameAI(object):
    def __init__(self, board, ai_player='O', human_player = 'X'):
        self.__board_game = board
        self.ai_player = ai_player
        self.human_player = human_player

    def get_best_move(self):
        board = self.__board_game.clone_instance()

        best_score = -math.inf
        best_move = None

        for i in range(board.get_board_size()):
            for j in range(board.get_board_size()):
                if board.is_valid_move((i, j)):
                    board.set_grid_cell((i, j), self.ai_player)
                    score = self.__minimax(board,0, -math.inf, math.inf, False)
                    board.clear_grid_cell((i, j))

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

    def __evaluate_position(self, board):
        winner = board.check_winner()

        if winner == self.ai_player:
            return 10
        elif winner == self.human_player:
            return -10
        elif board.is_full():
            return 0

        return None

    def __minimax(self, board, depth, alpha, beta, is_maximizing):
        position_score = self.__evaluate_position(board)
        if position_score is not None:
            return position_score + depth

        if is_maximizing:
            best_score = -math.inf
            for i in range(board.get_board_size()):
                for j in range(board.get_board_size()):
                    if board.is_valid_move((i, j)):
                        board.set_grid_cell((i, j), self.ai_player)
                        score = self.__minimax(board, depth + 1, alpha, beta, False)
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
                        board.set_grid_cell((i, j), self.human_player)
                        score = self.__minimax(board, depth + 1, alpha, beta,True)
                        board.set_grid_cell((i, j), '')
                        best_score = min(score, best_score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return best_score
