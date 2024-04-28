from ui.ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.PokemonWindow import PokemonWindow
from src.AbilityWindow import AbilityWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Pokedex")

        self.ui.actionAbout_Pokedex.triggered.connect(self.show_about_pokedex)

        self.ui.pushButton_PokemonData.clicked.connect(self.open_pokemon_window)
        self.ui.pushButton_AbilityData.clicked.connect(self.open_move_window)

        self.add_pokemon()
        self.add_ability()
        self.add_move()

    def show_about_pokedex(self):
        title = "About Pokedex"
        text = "This is a pokedex app made by HunarPG"
        dialog = QMessageBox()
        dialog.about(self, title, text)

    def add_pokemon(self):
        with open("database/pokemon.txt", "r") as f:
            for line in f:
                line = line.strip("\n")
                self.ui.comboBox_Pokemon.addItem(line)

    def add_ability(self):
        with open("database/ability.txt", "r") as f:
            for line in f:
                line = line.strip("\n")
                self.ui.combobox_Ability.addItem(line)

    def add_move(self):
        with open("database/move.txt", "r") as f:
            for line in f:
                line = line.strip("\n")
                self.ui.comboBox_Move.addItem(line)
    
    def open_pokemon_window(self):
        self.window = PokemonWindow()
        self.window.show()
    
    def open_move_window(self):
        self.window = AbilityWindow()
        self.window.show()
