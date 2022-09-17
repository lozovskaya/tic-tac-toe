import unittest

from BoardClass import Game
from minimax import minimax_algorithm
from statuses import CellStatus, TurnStatus


class MyTestCase(unittest.TestCase):

    # check is_win function
    def test_win_by_row(self):
        for board_size in range(3, 10):
            win_row = min(5, board_size)
            for x in range(board_size):
                for cell in [CellStatus.X_CELL, CellStatus.O_CELL]:
                    with self.subTest(board_size=board_size):
                        game = Game(board_size)
                        for i in range(win_row):
                            game.board[x][i] = cell
                        self.assertEqual(game.is_win(cell), True)

    def test_win_by_column(self):
        for board_size in range(3, 10):
            win_row = min(5, board_size)
            for y in range(board_size):
                for cell in [CellStatus.X_CELL, CellStatus.O_CELL]:
                    with self.subTest(board_size=board_size):
                        game = Game(board_size)
                        for i in range(win_row):
                            game.board[i][y] = cell
                        self.assertEqual(game.is_win(cell), True)

    def test_win_by_main_diag(self):
        for board_size in range(3, 10):
            win_row = min(5, board_size)
            for cell in [CellStatus.X_CELL, CellStatus.O_CELL]:
                with self.subTest(board_size=board_size):
                    game = Game(board_size)
                    for i in range(win_row):
                        game.board[i][i] = cell
                    self.assertEqual(game.is_win(cell), True)

    def test_win_by_main_diag2(self):
        for board_size in range(3, 10):
            win_row = min(5, board_size)
            for cell in [CellStatus.X_CELL, CellStatus.O_CELL]:
                with self.subTest(board_size=board_size):
                    game = Game(board_size)
                    for i in range(win_row):
                        game.board[i][board_size - i - 1] = cell
                    self.assertEqual(game.is_win(cell), True)

    # check minimax logic

    def test_only_one_possible_move(self):
        game = Game(3, TurnStatus.COMPUTER_TURN)
        game.board = [[CellStatus.X_CELL, CellStatus.EMPTY_CELL, CellStatus.O_CELL],
                      [CellStatus.O_CELL, CellStatus.EMPTY_CELL, CellStatus.EMPTY_CELL],
                      [CellStatus.O_CELL, CellStatus.X_CELL, CellStatus.X_CELL]]
        minimax_algorithm(game)
        self.assertEqual(game.choice, (1, 1))

    def test_computer_ultimately_wins_1(self):
        game = Game(3, TurnStatus.COMPUTER_TURN)
        game.board = [[CellStatus.O_CELL, CellStatus.X_CELL, CellStatus.X_CELL],
                      [CellStatus.X_CELL, CellStatus.O_CELL, CellStatus.EMPTY_CELL],
                      [CellStatus.EMPTY_CELL, CellStatus.X_CELL, CellStatus.EMPTY_CELL]]
        minimax_algorithm(game)
        self.assertEqual(game.choice, (2, 2))

    def test_computer_ultimately_wins_2(self):
        game = Game(3, TurnStatus.COMPUTER_TURN)
        game.board = [[CellStatus.O_CELL, CellStatus.O_CELL, CellStatus.X_CELL],
                      [CellStatus.X_CELL, CellStatus.O_CELL, CellStatus.X_CELL],
                      [CellStatus.X_CELL, CellStatus.EMPTY_CELL, CellStatus.EMPTY_CELL]]
        minimax_algorithm(game)
        self.assertEqual(game.choice, (2, 1))

    def test_computer_ultimately_wins_3(self):
        game = Game(3, TurnStatus.COMPUTER_TURN)
        game.board = [[CellStatus.X_CELL, CellStatus.X_CELL, CellStatus.EMPTY_CELL],
                      [CellStatus.EMPTY_CELL, CellStatus.X_CELL, CellStatus.EMPTY_CELL],
                      [CellStatus.EMPTY_CELL, CellStatus.O_CELL, CellStatus.O_CELL]]
        minimax_algorithm(game)
        self.assertEqual(game.choice, (2, 0))

    def test_computer_is_saving_1(self):
        game = Game(3, TurnStatus.COMPUTER_TURN)
        game.board = [[CellStatus.O_CELL, CellStatus.EMPTY_CELL, CellStatus.EMPTY_CELL],
                      [CellStatus.X_CELL, CellStatus.X_CELL, CellStatus.EMPTY_CELL],
                      [CellStatus.EMPTY_CELL, CellStatus.EMPTY_CELL, CellStatus.EMPTY_CELL]]
        minimax_algorithm(game)
        self.assertEqual(game.choice, (1, 2))

    def test_computer_is_saving_2(self):
        game = Game(3, TurnStatus.COMPUTER_TURN)
        game.board = [[CellStatus.O_CELL, CellStatus.EMPTY_CELL, CellStatus.X_CELL],
                      [CellStatus.X_CELL, CellStatus.X_CELL, CellStatus.O_CELL],
                      [CellStatus.EMPTY_CELL, CellStatus.EMPTY_CELL, CellStatus.EMPTY_CELL]]
        minimax_algorithm(game)
        self.assertEqual(game.choice, (2, 0))

    def test_computer_is_saving_3(self):
        game = Game(3, TurnStatus.COMPUTER_TURN)
        game.board = [[CellStatus.EMPTY_CELL, CellStatus.X_CELL, CellStatus.X_CELL],
                      [CellStatus.EMPTY_CELL, CellStatus.O_CELL, CellStatus.EMPTY_CELL],
                      [CellStatus.EMPTY_CELL, CellStatus.EMPTY_CELL, CellStatus.EMPTY_CELL]]
        minimax_algorithm(game)
        self.assertEqual(game.choice, (0, 0))



if __name__ == '__main__':
    unittest.main()
