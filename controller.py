from PySide6.QtCore import QObject


class Controller(QObject):

    def __init__(self):
        super(Controller, self).__init__()


controller = Controller()
