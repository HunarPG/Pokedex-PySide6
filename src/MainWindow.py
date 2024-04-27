from ui.mainwindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox

pokemon_names = []
ability_names = []
move_names = []

with open("database/pokemon.txt", "r") as pokemon_database:
    num_pokemon = 0
    while num_pokemon<1025:
        pokemon_names.append(pokemon_database.readline())
        num_pokemon+=1

with open("database/ability.txt", "r") as ability_database:
    num_ability = 0
    while num_ability<310:
        ability_names.append(ability_database.readline())
        num_ability+=1

with open("database/move.txt", "r") as move_database:
    num_move = 0
    while num_move<934:
        move_names.append(move_database.readline())
        num_move+=1

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Pokedex")

        self.ui.actionAbout_Qt.triggered.connect(self.show_about_qt)
        self.ui.actionAbout_Pokedex.triggered.connect(self.show_about_pokedex)

        self.ui.comboBox_Pokemon.addItems(pokemon_names)
        self.ui.combobox_Ability.addItems(ability_names)
        self.ui.comboBox_Move.addItems(move_names)

    def show_about_qt(self):
        dialog = QMessageBox()
        dialog.aboutQt(self)
    
    def show_about_pokedex(self):
        title = "About Pokedex"
        text = "This is a pokedex app made by HunarPG"
        dialog = QMessageBox()
        dialog.about(self, title, text)
