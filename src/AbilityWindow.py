from ui.ui_ability import Ui_AbilityWindow
from PySide6.QtWidgets import QWidget

class AbilityWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_AbilityWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Ability Info")
