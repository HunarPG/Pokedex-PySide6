from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from ui.pokemon.ui_bulbasaur import Ui_Form

class BulbasaurWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Bulbasaur")
        pixmap = QPixmap("img/001.png")
        self.ui.label_bulbasaur_image.setPixmap(pixmap)
