class BoardGame:
    def __init__(self, board_size):
        self.__board_size = int(board_size)
        self.__grid = [['' for _ in range(self.__board_size)] for _ in range(self.__board_size)]

    def clone_instance(self):
        clone_game = BoardGame(self.get_board_size())
        clone_game.__grid = [row[:] for row in self.__grid]
        return clone_game

    def get_board_size(self):
        return self.__board_size

    def get_grid_cell(self, move):
        row, col = move
        return self.__grid[row][col]

    def set_grid_cell(self, move, value):
        row, col = move
        self.__grid[row][col] = value

    def clear_grid_cell(self, move):
        self.set_grid_cell(move, '')

    def is_valid_move(self, move):
        return self.get_grid_cell(move) == ''

    def is_full(self):
        return all(all(cell != '' for cell in row) for row in self.__grid)

    def check_winner(self):
        size = self.get_board_size()

        for i in range(size):
            if all(self.get_grid_cell((i, j)) == self.get_grid_cell((i, 0)) != '' for j in range(size)):
                return self.get_grid_cell((i, 0))
            if all(self.get_grid_cell((j, i)) == self.get_grid_cell((i, 0)) != '' for j in range(size)):
                return self.get_grid_cell((i, 0))

        if all(self.get_grid_cell((i, i)) == self.get_grid_cell((0, 0)) != '' for i in range(size)):
            return self.get_grid_cell((0, 0))
        if all(self.get_grid_cell((i, size - 1 - i)) == self.get_grid_cell((0, size - 1)) != '' for i in range(size)):
            return self.get_grid_cell((0, size - 1))

        return None