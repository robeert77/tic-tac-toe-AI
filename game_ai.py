import math

class GameAI(object):
    __depth = 4 # Adancimea maxima pentru care calculatorul calculeaza posibile miscari
    __ai_moves = 0 # Memoram numarul de miscari ale calculatorului

    """
    Contrusctorul clasei GameAI

        Args:
            board (BoardGame): Instanta pentru clasa BoardGame
            ai_player (str): Simbolul folosit de catre calculator pe parcursul jocului
            human_player (str): Simbolul folosit de user pe parcursul jocului

       Returns:
            None
    """
    def __init__(self, board, ai_player='O', human_player = 'X'):
        self.__board_game = board
        self.__ai_player = ai_player
        self.__human_player = human_player

        # In cazul unei matrici de 3x3, putem incaepe cu o adancime mai mare, deoarce nu exista atat de multe
        # posibilitati, iar calculatorul ofera raspuns instant
        if self.__board_game.get_board_size() == 3:
            self.__depth = 6

    """
    Metoda care evalueaza miscarea optima pentru calculator, folosind algoritmul minmax. Aceasta verifica toate pozitile posibile de pe tabla

    Args:
        None

    Returns:
        int: Cea mai buna mutare in momentul de fata pentru calculator
    """
    def get_best_move(self):
        board = self.__board_game.clone_instance() # Clonam instanta obiectului __board_game. O folosim mai departe in calcularea pozitiei

        best_score = -math.inf # Pornim initial cu cel mai rau scor posibil
        best_move = None # Initializam cea mai buna pozitie cu None

        for i in range(board.get_board_size()):
            for j in range(board.get_board_size()):
                if board.is_valid_move((i, j)): # Luam pe rand fiecare pozitie care nu este ocupata deja
                    board.set_grid_cell((i, j), self.__ai_player) # Daca pozitia curenta este libera, simulam ce s-ar intampla daca calculatorul ar alge aceasta pozitie
                    score = self.__minimax(board, self.__depth, -math.inf, math.inf, False) # Apelul algoritmul minmax
                    board.clear_grid_cell((i, j)) # Eliberam pozitia curenta

                    if score > best_score: # Salvam cea mai buna mutare gasita in momentul de fata
                        best_score = score
                        best_move = (i, j)

        self.__increase_depth()
        return best_move

    """
    Metoda care se ocupa cu ajustarea dinamica a adancimii pe care o permitem in algoritmul minmax

    Args:
        None

    Returns:
        None
    """
    def __increase_depth(self):
        self.__ai_moves += 1 # Incrementam numarul de mutari facute de calculator
        increase_at_nr_steps = self.__board_game.get_board_size() - 2 # Calculam din cate in cate miscari dorim sa crestem adancimea (pe masura ce tabla de joc se umple, avem tot mai putine posibilitati, iar timpu de decizie scade)
        self.__depth += (self.__depth < 7 and self.__ai_moves % increase_at_nr_steps == 0) # Actualizam adancimea algoritmului cu 1, daca este respectata conditia din paranteze

    """
    Metoda care evalueaza simularea jocului la momentul actual, pentru algoritmul de cautare a celei mai optime mutarii a calculatorului

    Args:
        board (BoardGame): Obiectul clonat, de tip BoardGame
        depth (int): Adancimea curenta la care a ajuns algoritmul

    Returns:
        int:    10  -> in cazul in care calculatorul castiga(acesta favorizeaza scorul maxim)
                -10 -> in cazul in care userul castiga(acesta favorizeaza scorul minim)
                0   -> in cazul in care este remiza, sau am ajuns la adancimea maxima setata
        None:   in cazul in care nici una dintre aceste conditii nu este indeplinita
    """
    def __evaluate_position(self, board, depth):
        winner = board.check_winner()

        if winner == self.__ai_player:
            return 10
        elif winner == self.__human_player:
            return -10
        elif board.is_full() or depth == 0:
            return 0

        return None

    """
    Metoda care calculeaza cel mai bun scor posibil pentru jucatorul curent

    Args:
        board (BoardGame): Obiectul clonat, de tip BoardGame
        depth (int): Adancimea curenta la care a ajuns algoritmul
        alpha (int): Reprezinta cel mai bun scor pana in momentul de fata, pe care calculatorul il poate asigura daca joaca optim
        beta (int): Reprezinta cel mai bun scor pana in momentul de fata, pe care userul il poate asigura daca joaca optim
        is_maximizing (bool): True daca jucatorul curent favorizeaza un scoar maxim(calculatorul), False in cazul in care jucatorul curent favorizeaza un scor minim(userul)

    Returns:
        int:    10  -> in cazul in care calculatorul castiga(acesta favorizeaza scorul maxim)
                -10 -> in cazul in care userul castiga(acesta favorizeaza scorul minim)
                0   -> in cazul in care este remiza, sau am ajuns la adancimea maxima setata
        None:   in cazul in care nici una dintre aceste conditii nu este indeplinita
    """
    def __minimax(self, board, depth, alpha, beta, is_maximizing):
        position_score = self.__evaluate_position(board, depth)
        if position_score is not None: # Ne oprimt doar in caul in care avem un castigator, egalitate, sau am atins adancimea maxima
            return position_score + depth

        if is_maximizing: # Randul calculatorului(favorizeaza scor maxim)
            best_score = -math.inf # Plecam din start cu cel mai rau scor posibil pentru situatia actuala
            for i in range(board.get_board_size()):
                for j in range(board.get_board_size()): # Luam la rand toate pozitile posibile
                    if board.is_valid_move((i, j)):
                        board.set_grid_cell((i, j), self.__ai_player) # Daca pozitia curenta este libera, simulam ce s-ar intampla daca calculatorul ar alge aceasta pozitie
                        score = self.__minimax(board, depth - 1, alpha, beta, False) # Apelul recursiv pentru algoritmul minmax
                        board.clear_grid_cell((i, j)) # Eliberam inapoi pozitia curenta
                        best_score = max(score, best_score) # Calculam cel mai bun scor gasit pana la pasul curent
                        alpha = max(alpha, score) # Optimizarea Alpha-Beta
                        if beta <= alpha:
                            break
            return best_score
        else: # Randul userului(favorizeaza scor minim)
            best_score = math.inf # Plecam din start cu cel mai rau scor posibil pentru situatia actuala
            for i in range(board.get_board_size()):
                for j in range(board.get_board_size()): # Luam la rand toate pozitile posibile
                    if board.is_valid_move((i, j)):
                        board.set_grid_cell((i, j), self.__human_player) # Daca pozitia curenta este libera, simulam ce s-ar intampla daca userul ar alge aceasta pozitie
                        score = self.__minimax(board, depth - 1, alpha, beta,True) # Apelul recursiv pentru algoritmul minmax
                        board.set_grid_cell((i, j), '') # Eliberam inapoi pozitia curenta
                        best_score = min(score, best_score) # Calculam cel mai bun scor gasit pana la pasul curent
                        beta = min(beta, score) # Optimizarea Alpha-Beta
                        if beta <= alpha:
                            break
            return best_score
