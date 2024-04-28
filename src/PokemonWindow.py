from ui.ui_pokemon import Ui_PokemonWindow
from PySide6.QtWidgets import QWidget


class PokemonWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_PokemonWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Pokemon Info")
