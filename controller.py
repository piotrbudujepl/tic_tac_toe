from PySide6.QtCore import QObject, Slot

from model import Model


class Controller(QObject):

    def __init__(self, model: Model):
        super(Controller, self).__init__()
        self.model = model

    @Slot()
    def start_new_game(self):
        self.model.reset()

    @Slot(int, int)
    def move(self, y, x):
        if self.model.field_has_value(y, x):
            return
        current_player = self.model.current_player
        next_player = "O" if current_player == "X" else "X"
        self.model.update_field(y, x, current_player)
        self.model.current_player = next_player
