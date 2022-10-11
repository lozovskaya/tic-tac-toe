from statuses import CellStatus, TurnStatus, COMPUTER_CELL, PLAYER_CELL


def score(game, depth) -> int:
    if game.is_win(COMPUTER_CELL):
        return 10 - depth
    if game.is_win(PLAYER_CELL):
        return depth - 10
    return 0


conditions = dict()


def already_calculated(game) -> bool:
    return (str(game.board), game.current_turn) in conditions.keys()


def minimax_algorithm(game, depth=0, debug=False) -> int:
    if game.is_game_over():
        return score(game, depth)

    depth += 1
    final_score = None
    final_move = game.possible_moves()[0]

    for move in game.possible_moves():
        if debug:
            game.display_board()
            print(game.current_turn)
            print()

        current_turn = game.current_turn
        game.board[move[0]][move[1]] = PLAYER_CELL if game.current_turn == TurnStatus.PLAYER_TURN else COMPUTER_CELL
        game.current_turn = game.next_turn()

        key = (str(game.board), game.current_turn)
        if already_calculated(game):
            current_score = conditions[key]
        else:
            current_score = minimax_algorithm(game, depth, debug)
            conditions[key] = current_score

        if current_turn == TurnStatus.COMPUTER_TURN:
            if final_score is None or current_score > final_score:
                final_score = current_score
                final_move = move
        else:
            if final_score is None or current_score < final_score:
                final_score = current_score
                final_move = move

        if debug:
            game.display_board()
            print(final_score)
            print('-' * 20)

        game.board[move[0]][move[1]] = CellStatus.EMPTY_CELL
        game.current_turn = current_turn

    game.choice = final_move
    if debug:
        print("final move: ", game.choice, final_score)
    return final_score
