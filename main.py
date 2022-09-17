from statuses import CellStatus, TurnStatus, COMPUTER_CELL, PLAYER_CELL
from BoardClass import Game
from minimax import minimax_algorithm


def enter_size():
    size = input("Please enter the size of the board (from 3 to 10): ")
    while not size.isdigit() or int(size) < 3 or int(size) > 10:
        size = input("Please enter valid value: ")
    return int(size)


def main():
    print('Welcome to Tic Tac Toe!')

    user_size = enter_size()
    new_Game = Game(user_size, TurnStatus.PLAYER_TURN)

    new_Game.display_board()

    while not new_Game.is_board_full():
        new_Game.player_move(PLAYER_CELL)
        new_Game.display_board()

        if new_Game.is_win(PLAYER_CELL):
            print("Congrats! You won!")
            return

        minimax_algorithm(new_Game)

        print("Computer's turn:", new_Game.choice[0] + 1, new_Game.choice[1] + 1)

        new_Game.board[new_Game.choice[0]][new_Game.choice[1]] = COMPUTER_CELL
        new_Game.display_board()

        if new_Game.is_win(COMPUTER_CELL):
            print("AI won!")
            return

    print("It's a draw")


if __name__ == '__main__':
    main()
