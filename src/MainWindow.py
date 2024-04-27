from ui.mainwindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Pokedex")

        self.ui.actionAbout_Qt.triggered.connect(self.show_about_qt)

    def show_about_qt(self):
        QMessageBox.aboutQt(self)
