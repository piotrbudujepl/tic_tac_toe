from itertools import starmap

from PySide6.QtCore import QObject, Slot, Signal

from model import Model


class Controller(QObject):
    game_ended = Signal(str)

    def __init__(self, model: Model):
        super(Controller, self).__init__()
        self.model = model

    def is_stalemate(self):
        return not self.model.board_has_empty_field()

    def calc_winner(self):
        win_conditions = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                          ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                          ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))
                          ]
        win_checks = [list(starmap(self.model.field, check)) for check in win_conditions]
        win_checks_x = [map(lambda check: check == "X", check) for check in win_checks]
        win_checks_o = [map(lambda check: check == "O", check) for check in win_checks]
        if any(all(check) for check in win_checks_x):
            return "X"
        if any(all(check) for check in win_checks_o):
            return "O"
        return None

    @Slot()
    def start_new_game(self):
        self.model.reset()

    @Slot(int, int)
    def move(self, y, x):
        if self.model.game_over:
            self.game_ended.emit("Game over! Press 'New game' to play again.")
            return
        if self.model.field_has_value(y, x):
            return
        current_player = self.model.current_player
        next_player = "O" if current_player == "X" else "X"
        self.model.update_field(y, x, current_player)
        self.model.current_player = next_player
        winner = self.calc_winner()
        if winner:
            self.model.game_over = True
            self.game_ended.emit("Game over! Player: '{}' won!".format(winner))
        if self.is_stalemate():
            self.model.game_over = True

            self.game_ended.emit("Game over! No more moves possible.")
