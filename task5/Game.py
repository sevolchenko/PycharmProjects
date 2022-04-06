import random as rnd
from enum import Enum


class GameCell:
    def __init__(self, data: int = -1):
        self._data = data

    @property
    def data(self) -> int:
        return self._data

    def __str__(self):
        return str(self._data)


class GameState(Enum):
    NOT_STARTED = -1
    PLAYING = 0
    WIN = 1


class QuadrotecaGame:
    def __init__(self, level: int, shake_count: int = 20):
        self._level = level
        self._field = [[GameCell()] * 5 for _ in range(5)]

        self._selected_row = -1
        self._selected_col = -1

        self._count_of_moves = -1
        self._count_of_rotations = -1

        self._state = GameState.NOT_STARTED

        self.new_game(shake_count)

    def new_game(self, shake_count: int = 20) -> None:
        if self._level < 1 or self._level > 4:
            raise Exception('Wrong level')
        self._field = QuadrotecaGame.create_field(self._level)
        self._shake_field(shake_count)
        self._selected_row = 0
        self._selected_col = 1
        self._count_of_moves = 0
        self._count_of_rotations = 0
        self._state = GameState.PLAYING

    @property
    def selected_row(self) -> int:
        return self._selected_row

    @property
    def selected_col(self) -> int:
        return self._selected_col

    @property
    def count_of_moves(self) -> int:
        return self._count_of_moves

    @property
    def count_of_rotations(self) -> int:
        return self._count_of_rotations

    @property
    def count_of_ready_cols(self) -> int:
        return self._count_of_ready_cols()

    @property
    def state(self) -> GameState:
        return self._state

    def __getitem__(self, indices: tuple) -> GameCell:
        return self._field[indices[0]][indices[1]]

    @staticmethod
    def create_field(level: int):
        field = [[GameCell()] * 5 for _ in range(5)]
        columns = [0] * 5
        i = 0
        while i < 5:
            columns[i % (level + 1)] += 1
            i += 1
        i = 0
        for j in range(len(columns)):
            for count in range(columns[j]):
                for row in range(len(field)):
                    field[row][i] = GameCell(j)
                i += 1
        return field

    def _shake_field(self, count: int = 20):
        for _ in range(count):
            self._selected_row = rnd.randint(0, 2)
            self._selected_col = rnd.randint(0, 2)
            self._rotate(bool(rnd.random()))

    def _rotate(self, clockwise: bool):
        selected = [row[self._selected_col: self._selected_col + 3]
                    for row in self._field[self._selected_row: self._selected_row + 3]]
        new_matrix = [list(col[::-1] if clockwise else col) for col in zip(*selected)]
        if not clockwise:
            new_matrix = new_matrix[::-1]
        for row in range(len(new_matrix)):
            for col in range(len(new_matrix[0])):
                self._field[row + self._selected_row][col + self._selected_col] = new_matrix[row][col]

    def _update_playing_state(self):
        if self._count_of_ready_cols() == 5:
            self._state = GameState.WIN
        else:
            self._state = GameState.PLAYING

    def _count_of_ready_cols(self) -> int:
        count = 0
        for col in zip(*self._field):
            eq = True
            for i in col:
                eq = eq and i.data == col[0].data
            count += int(eq)
        return count

    def rotation_key_pressed(self, clockwise: bool):
        self._rotate(clockwise)
        self._update_playing_state()
        self._count_of_rotations += 1

    def moving_key_pressed(self, row: int, col: int):
        self._selected_row += row
        self._selected_col += col
        self._count_of_moves += 1
        if self._selected_row < 0 or self._selected_row > 2:
            self._selected_row -= row
            self._count_of_moves -= 1
        if self._selected_col < 0 or self._selected_col > 2:
            self._selected_col -= col
            self._count_of_moves -= 1