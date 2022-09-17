from enum import Enum


class CellStatus(Enum):
    EMPTY_CELL = " "
    X_CELL = "X"
    O_CELL = "O"


PLAYER_CELL = CellStatus.X_CELL
COMPUTER_CELL = CellStatus.O_CELL


class TurnStatus(Enum):
    PLAYER_TURN = 0
    COMPUTER_TURN = 1
