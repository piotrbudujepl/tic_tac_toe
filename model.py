from PySide6.QtCore import QObject, Property, Signal


class Model(QObject):
    def __init__(self):
        super(Model, self).__init__()
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.field_notify_signals = [
            (self.field_0_0_changed,
             self.field_0_1_changed,
             self.field_0_2_changed),
            (self.field_1_0_changed,
             self.field_1_1_changed,
             self.field_1_2_changed),
            (self.field_2_0_changed,
             self.field_2_1_changed,
             self.field_2_2_changed)
        ]
        self._current_player = "O"

    def field_has_value(self, y, x):
        return self.board[y][x] != ""

    def update_field(self, y, x, value):
        self.board[y][x] = value
        self.field_notify_signals[y][x].emit()

    def get_current_player(self):
        return self._current_player

    def set_current_player(self, player):
        self._current_player = player
        self.current_player_changed.emit()

    @Signal
    def current_player_changed(self):
        pass

    def reset(self):
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self._current_player = "O"
        for row in self.field_notify_signals:
            for notify_signal in row:
                notify_signal.emit()
        self.current_player_changed.emit()

    @Signal
    def field_0_0_changed(self):
        pass

    def get_field_0_0(self):
        return self.board[0][0]

    @Signal
    def field_0_1_changed(self):
        pass

    def get_field_0_1(self):
        return self.board[0][1]

    @Signal
    def field_0_2_changed(self):
        pass

    def get_field_0_2(self):
        return self.board[0][2]

    @Signal
    def field_1_0_changed(self):
        pass

    def get_field_1_0(self):
        return self.board[1][0]

    @Signal
    def field_1_1_changed(self):
        pass

    def get_field_1_1(self):
        return self.board[1][1]

    @Signal
    def field_1_2_changed(self):
        pass

    def get_field_1_2(self):
        return self.board[1][2]

    @Signal
    def field_2_0_changed(self):
        pass

    def get_field_2_0(self):
        return self.board[2][0]

    @Signal
    def field_2_1_changed(self):
        pass

    def get_field_2_1(self):
        return self.board[2][1]

    @Signal
    def field_2_2_changed(self):
        pass

    def get_field_2_2(self):
        return self.board[2][2]

    field_0_0 = Property(str, get_field_0_0, notify=field_0_0_changed)
    field_0_1 = Property(str, get_field_0_1, notify=field_0_1_changed)
    field_0_2 = Property(str, get_field_0_2, notify=field_0_2_changed)
    field_1_0 = Property(str, get_field_1_0, notify=field_1_0_changed)
    field_1_1 = Property(str, get_field_1_1, notify=field_1_1_changed)
    field_1_2 = Property(str, get_field_1_2, notify=field_1_2_changed)
    field_2_0 = Property(str, get_field_2_0, notify=field_2_0_changed)
    field_2_1 = Property(str, get_field_2_1, notify=field_2_1_changed)
    field_2_2 = Property(str, get_field_2_2, notify=field_2_2_changed)
    current_player = Property(str, get_current_player, set_current_player, notify=current_player_changed)
