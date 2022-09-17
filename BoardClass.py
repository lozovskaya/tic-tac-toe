import copy

from statuses import CellStatus, TurnStatus


class Game:
    def __init__(self, size, first_turn=TurnStatus.PLAYER_TURN):
        self.size = size
        self.board = self.__create_board()
        self.current_turn = first_turn
        self.choice = None

    def __create_board(self) -> list:
        return [[CellStatus.EMPTY_CELL for _ in range(self.size)] for _ in range(self.size)]

    def get_value(self, n) -> str:
        return self.board[n // self.size][n % self.size]

    def __set_value(self, n, new_value) -> None:
        self.board[n // self.size][n % self.size] = new_value

    def display_board(self) -> None:
        for row in self.board:
            print('| ', end='')
            for cell in row:
                print(cell.value, '| ', end="")
            print()
            # print('-' * (4 * self.size + 1))

    def next_turn(self) -> TurnStatus:
        if self.current_turn == TurnStatus.COMPUTER_TURN:
            return TurnStatus.PLAYER_TURN
        else:
            return TurnStatus.COMPUTER_TURN

    def is_board_full(self) -> bool:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == CellStatus.EMPTY_CELL:
                    return False
        return True

    def is_valid_coordinate(self, x, y) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size

    def check_win_from_coordinate(self, x, y, symbol) -> bool:
        win_condition = min(5, self.size)
        dx = [-1, 0, +1]
        dy = [-1, 0, +1]

        for delta_x in dx:
            for delta_y in dy:
                if delta_x == 0 and delta_y == 0:
                    continue
                check_x = x
                check_y = y
                count = 0
                while self.is_valid_coordinate(check_x, check_y) and self.board[check_x][check_y] == symbol:
                    check_x += delta_x
                    check_y += delta_y
                    count += 1
                    if count == win_condition:
                        return True
        return False

    def is_win(self, symbol) -> bool:
        for x in range(self.size):
            for y in range(self.size):
                if self.check_win_from_coordinate(x, y, symbol):
                    return True
        return False

    def is_game_over(self) -> bool:
        return self.is_win(CellStatus.X_CELL) or self.is_win(CellStatus.O_CELL) or self.is_board_full()

    def player_move(self, symbol) -> None:
        x, y = input("Please enter the row and the column: ").split()
        while not x.isdigit() or not x.isdigit() or not self.is_valid_coordinate(int(x) - 1, int(y) - 1) or \
                self.board[int(x) - 1][int(y) - 1] != CellStatus.EMPTY_CELL:
            x, y = input("Please enter valid values: ").split()
        x, y = int(x) - 1, int(y) - 1
        self.board[x][y] = symbol

    def possible_moves(self):
        assert not self.is_board_full()
        possible_moves = []
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == CellStatus.EMPTY_CELL:
                    possible_moves.append((x, y))
        return possible_moves
