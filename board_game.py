class BoardGame:
    """
    Contrusctorul clasei BoardGame

    Args:
        board_size (int): Indica dimensiunea tablei de joc, selectata de catre utilizator

    Returns:
        None
    """
    def __init__(self, board_size):
        self.__board_size = int(board_size)  # dimensiunea tablei de joc
        self.__grid = [['' for _ in range(self.__board_size)] for _ in range(self.__board_size)]  # tabla de joc

    """
    Cloneaza instanta clasei curente

    Args:
        None

    Returns:
        BoarGame class: Returneaza o noua instanta a clasei curente

    Details:
        - folosim aceasta metoda pentru a generea o instanta identica cu instanta orginala, cea folosita pentru jocul oficial
        - facem acest lucru, pentru a putea folosi metodele deja defninite si in cadrul algoritmului minmax, fara a refactoriza codul
        - clonand instanta jocului original, ne asiguram ca nu influentam jocu pe parcursul operatiol din algoritmului minmax
    """
    def clone_instance(self):
        clone_game = BoardGame(self.get_board_size())
        clone_game.__grid = [row[:] for row in self.__grid]
        return clone_game

    """
    Returneaza dimensiunea tablei de joc

    Args:
        None

    Returns:
        int: Dimensiunea tablei de joc
    """
    def get_board_size(self):
        return self.__board_size

    """
    Returneaza continutul tablei penru pozitia move indicata in argumente

    Args:
        move (touple(int, int)): Indica pozitia de pe tabla pentru care dorim sa aflam continutul

    Returns:
        str: Continutul tablei de joc din pozitia indicata
    """
    def get_grid_cell(self, move):
        row, col = move
        return self.__grid[row][col]

    """
    Seteaza pozitia move din tabla, cu valoarea value primita ca si argument

    Args:
        move (touple(int, int)): Indica pozitia de pe tabla pentru care dorim setam valoarea
        value (str): Reprezinta continutul matricii in pozitia indicata

    Returns:
        None
    """
    def set_grid_cell(self, move, value):
        row, col = move
        self.__grid[row][col] = value

    """
    Aduce la stadiul initial(de nefolosit) o pozitie data

    Args:
        move (touple(int, int)): Indica pozitia de pe tabla pentru care dorim sa facem revenirea

    Returns:
        None
    """
    def clear_grid_cell(self, move):
        self.set_grid_cell(move, '')

    """
    Verifica daca o anumita positie este ocupata sau nu

    Args:
        move (touple(int, int)): Indica pozitia de pe tabla pentru care dorim sa facem verificarea

    Returns:
        bool: True in cazul in care pozitia este una valida(libera), False in caz contrar
    """
    def is_valid_move(self, move):
        return self.get_grid_cell(move) == ''

    """
    Verifica daca tabla are toate pozitiile marcate

    Args:
        None

    Returns:
        bool: True in cazul in care tabla de joc este plina, False in caz contrar.
    """
    def is_full(self):
        return all(all(cell != '' for cell in row) for row in self.__grid)

    """
    Verifica daca este un castigator pe tabla de joc

    Args:
        None

    Returns:
        str sau None: Simbolul utilizatorului (X sau O) daca acesta exista, sau None in caz contrar.
    """
    def check_winner(self):
        size = self.get_board_size()

        for i in range(size):
            if all(self.get_grid_cell((i, j)) == self.get_grid_cell((i, 0)) != '' for j in range(size)):
                return self.get_grid_cell((i, 0))
            if all(self.get_grid_cell((j, i)) == self.get_grid_cell((0, i)) != '' for j in range(size)):
                return self.get_grid_cell((0, i))

        if all(self.get_grid_cell((i, i)) == self.get_grid_cell((0, 0)) != '' for i in range(size)):
            return self.get_grid_cell((0, 0))
        if all(self.get_grid_cell((i, size - 1 - i)) == self.get_grid_cell((0, size - 1)) != '' for i in range(size)):
            return self.get_grid_cell((0, size - 1))

        return None