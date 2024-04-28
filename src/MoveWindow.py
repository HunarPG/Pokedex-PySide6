from PySide6.QtWidgets import QWidget

from ui.ui_move import Ui_MoveWindow


class MoveWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MoveWindow()
        self.ui.setupUi(self)
