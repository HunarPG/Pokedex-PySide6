from PySide6.QtWidgets import QWidget

from ui.ui_ability import Ui_AbilityWindow


class AbilityWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_AbilityWindow()
        self.ui.setupUi(self)
