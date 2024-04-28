from ui.ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.PokemonWindow import PokemonWindow
from src.MoveWindow import MoveWindow
from src.AbilityWindow import AbilityWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Pokedex")

        self.ui.actionAbout_Pokedex.triggered.connect(self.show_about_pokedex)

        self.ui.pushButton_PokemonData.clicked.connect(self.open_pokemon_window)
        self.ui.pushButton_AbilityData.clicked.connect(self.open_ability_Window)
        self.ui.pushButton_MoveData.clicked.connect(self.open_move_window)

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
                self.ui.comboBox_Ability.addItem(line)

    def add_move(self):
        with open("database/move.txt", "r") as f:
            for line in f:
                line = line.strip("\n")
                self.ui.comboBox_Move.addItem(line)

    def open_pokemon_window(self):
        self.window = PokemonWindow()
        self.window.setWindowTitle(self.ui.comboBox_Pokemon.currentText())
        if self.ui.comboBox_Pokemon.currentText() == "Bulbasaur":
            self.window.ui.label_pokemon.setText("Bulbasaur")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ivysaur":
            self.window.ui.label_pokemon.setText("Ivysaur")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Venusaur":
            self.window.ui.label_pokemon.setText("Venusaur")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Charmander":
            self.window.ui.label_pokemon.setText("Charmander")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Charmeleon":
            self.window.ui.label_pokemon.setText("Charmeleon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Charizard":
            self.window.ui.label_pokemon.setText("Charizard")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Squirtle":
            self.window.ui.label_pokemon.setText("Squirtle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wartortle":
            self.window.ui.label_pokemon.setText("Wartortle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Blastoise":
            self.window.ui.label_pokemon.setText("Blastoise")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Caterpie":
            self.window.ui.label_pokemon.setText("Caterpie")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Metapod":
            self.window.ui.label_pokemon.setText("Metapod")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Butterfree":
            self.window.ui.label_pokemon.setText("Butterfree")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Weedle":
            self.window.ui.label_pokemon.setText("Weedle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kakuna":
            self.window.ui.label_pokemon.setText("Kakuna")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Beedrill":
            self.window.ui.label_pokemon.setText("Beedrill")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pidgey":
            self.window.ui.label_pokemon.setText("Pidgey")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pidgeotto":
            self.window.ui.label_pokemon.setText("Pidgeotto")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pidgeot":
            self.window.ui.label_pokemon.setText("Pidgeot")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rattata":
            self.window.ui.label_pokemon.setText("Rattata")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Raticate":
            self.window.ui.label_pokemon.setText("Raticate")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spearow":
            self.window.ui.label_pokemon.setText("Spearow")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Fearow":
            self.window.ui.label_pokemon.setText("Fearow")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ekans":
            self.window.ui.label_pokemon.setText("Ekans")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Arbok":
            self.window.ui.label_pokemon.setText("Arbok")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pikachu":
            self.window.ui.label_pokemon.setText("Pikachu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Raichu":
            self.window.ui.label_pokemon.setText("Raichu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sandshrew":
            self.window.ui.label_pokemon.setText("Sandshrew")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sandslash":
            self.window.ui.label_pokemon.setText("Sandslash")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nidoran Female":
            self.window.ui.label_pokemon.setText("Nidoran Female")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nidorina":
            self.window.ui.label_pokemon.setText("Nidorina")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nidoqueen":
            self.window.ui.label_pokemon.setText("Nidoqueen")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nidoran Male":
            self.window.ui.label_pokemon.setText("Nidoran Male")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nidorino":
            self.window.ui.label_pokemon.setText("Nidorino")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nidoking":
            self.window.ui.label_pokemon.setText("Nidoking")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Clefairy":
            self.window.ui.label_pokemon.setText("Clefairy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Clefable":
            self.window.ui.label_pokemon.setText("Clefable")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vulpix":
            self.window.ui.label_pokemon.setText("Vulpix")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ninetales":
            self.window.ui.label_pokemon.setText("Ninetales")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Jigglypuff":
            self.window.ui.label_pokemon.setText("Jigglypuff")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wigglytuff":
            self.window.ui.label_pokemon.setText("Wigglytuff")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zubat":
            self.window.ui.label_pokemon.setText("Zubat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Golbat":
            self.window.ui.label_pokemon.setText("Golbat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Oddish":
            self.window.ui.label_pokemon.setText("Oddish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gloom":
            self.window.ui.label_pokemon.setText("Gloom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vileplume":
            self.window.ui.label_pokemon.setText("Vileplume")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Paras":
            self.window.ui.label_pokemon.setText("Paras")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Parasect":
            self.window.ui.label_pokemon.setText("Parasect")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Venonat":
            self.window.ui.label_pokemon.setText("Venonat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Venomoth":
            self.window.ui.label_pokemon.setText("Venomoth")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Diglett":
            self.window.ui.label_pokemon.setText("Diglett")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dugtrio":
            self.window.ui.label_pokemon.setText("Dugtrio")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Meowth":
            self.window.ui.label_pokemon.setText("Meowth")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Persian":
            self.window.ui.label_pokemon.setText("Persian")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Psyduck":
            self.window.ui.label_pokemon.setText("Psyduck")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Golduck":
            self.window.ui.label_pokemon.setText("Golduck")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mankey":
            self.window.ui.label_pokemon.setText("Mankey")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Primeape":
            self.window.ui.label_pokemon.setText("Primeape")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Growlithe":
            self.window.ui.label_pokemon.setText("Growlithe")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Arcanine":
            self.window.ui.label_pokemon.setText("Arcanine")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Poliwag":
            self.window.ui.label_pokemon.setText("Poliwag")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Poliwhirl":
            self.window.ui.label_pokemon.setText("Poliwhirl")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Poliwrath":
            self.window.ui.label_pokemon.setText("Poliwrath")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Abra":
            self.window.ui.label_pokemon.setText("Abra")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kadabra":
            self.window.ui.label_pokemon.setText("Kadabra")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Alakazam":
            self.window.ui.label_pokemon.setText("Alakazam")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Machop":
            self.window.ui.label_pokemon.setText("Machop")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Machoke":
            self.window.ui.label_pokemon.setText("Machoke")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Machamp":
            self.window.ui.label_pokemon.setText("Machamp")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bellsprout":
            self.window.ui.label_pokemon.setText("Bellsprout")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Weepinbell":
            self.window.ui.label_pokemon.setText("Weepinbell")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Victreebel":
            self.window.ui.label_pokemon.setText("Victreebel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tentacool":
            self.window.ui.label_pokemon.setText("Tentacool")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tentacruel":
            self.window.ui.label_pokemon.setText("Tentacruel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Geodude":
            self.window.ui.label_pokemon.setText("Geodude")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Graveler":
            self.window.ui.label_pokemon.setText("Graveler")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Golem":
            self.window.ui.label_pokemon.setText("Golem")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ponyta":
            self.window.ui.label_pokemon.setText("Ponyta")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rapidash":
            self.window.ui.label_pokemon.setText("Rapidash")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Slowpoke":
            self.window.ui.label_pokemon.setText("Slowpoke")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Slowbro":
            self.window.ui.label_pokemon.setText("Slowbro")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Magnemite":
            self.window.ui.label_pokemon.setText("Magnemite")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Magneton":
            self.window.ui.label_pokemon.setText("Magneton")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Farfetch'd":
            self.window.ui.label_pokemon.setText("Farfetch'd")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Doduo":
            self.window.ui.label_pokemon.setText("Doduo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dodrio":
            self.window.ui.label_pokemon.setText("Dodrio")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Seel":
            self.window.ui.label_pokemon.setText("Seel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dewgong":
            self.window.ui.label_pokemon.setText("Dewgong")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Grimer":
            self.window.ui.label_pokemon.setText("Grimer")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Muk":
            self.window.ui.label_pokemon.setText("Muk")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shellder":
            self.window.ui.label_pokemon.setText("Shellder")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cloyster":
            self.window.ui.label_pokemon.setText("Cloyster")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gastly":
            self.window.ui.label_pokemon.setText("Gastly")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Haunter":
            self.window.ui.label_pokemon.setText("Haunter")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gengar":
            self.window.ui.label_pokemon.setText("Gengar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Onix":
            self.window.ui.label_pokemon.setText("Onix")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Drowzee":
            self.window.ui.label_pokemon.setText("Drowzee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hypno":
            self.window.ui.label_pokemon.setText("Hypno")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Krabby":
            self.window.ui.label_pokemon.setText("Krabby")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kingler":
            self.window.ui.label_pokemon.setText("Kingler")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Voltorb":
            self.window.ui.label_pokemon.setText("Voltorb")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Electrode":
            self.window.ui.label_pokemon.setText("Electrode")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Exeggcute":
            self.window.ui.label_pokemon.setText("Exeggcute")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Exeggutor":
            self.window.ui.label_pokemon.setText("Exeggutor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cubone":
            self.window.ui.label_pokemon.setText("Cubone")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Marowak":
            self.window.ui.label_pokemon.setText("Marowak")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hitmonlee":
            self.window.ui.label_pokemon.setText("Hitmonlee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hitmonchan":
            self.window.ui.label_pokemon.setText("Hitmonchan")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lickitung":
            self.window.ui.label_pokemon.setText("Lickitung")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Koffing":
            self.window.ui.label_pokemon.setText("Koffing")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Weezing":
            self.window.ui.label_pokemon.setText("Weezing")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rhyhorn":
            self.window.ui.label_pokemon.setText("Rhyhorn")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rhydon":
            self.window.ui.label_pokemon.setText("Rhydon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chansey":
            self.window.ui.label_pokemon.setText("Chansey")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tangela":
            self.window.ui.label_pokemon.setText("Tangela")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kangaskhan":
            self.window.ui.label_pokemon.setText("Kangaskhan")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Horsea":
            self.window.ui.label_pokemon.setText("Horsea")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Seadra":
            self.window.ui.label_pokemon.setText("Seadra")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Goldeen":
            self.window.ui.label_pokemon.setText("Goldeen")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Seaking":
            self.window.ui.label_pokemon.setText("Seaking")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Staryu":
            self.window.ui.label_pokemon.setText("Staryu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Starmie":
            self.window.ui.label_pokemon.setText("Starmie")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mr. Mime":
            self.window.ui.label_pokemon.setText("Mr. Mime")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Scyther":
            self.window.ui.label_pokemon.setText("Scyther")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Jynx":
            self.window.ui.label_pokemon.setText("Jynx")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Electabuzz":
            self.window.ui.label_pokemon.setText("Electabuzz")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Magmar":
            self.window.ui.label_pokemon.setText("Magmar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pinsir":
            self.window.ui.label_pokemon.setText("Pinsir")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tauros":
            self.window.ui.label_pokemon.setText("Tauros")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Magikarp":
            self.window.ui.label_pokemon.setText("Magikarp")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gyarados":
            self.window.ui.label_pokemon.setText("Gyarados")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lapras":
            self.window.ui.label_pokemon.setText("Lapras")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ditto":
            self.window.ui.label_pokemon.setText("Ditto")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Eevee":
            self.window.ui.label_pokemon.setText("Eevee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vaporeon":
            self.window.ui.label_pokemon.setText("Vaporeon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Jolteon":
            self.window.ui.label_pokemon.setText("Jolteon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Flareon":
            self.window.ui.label_pokemon.setText("Flareon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Porygon":
            self.window.ui.label_pokemon.setText("Porygon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Omanyte":
            self.window.ui.label_pokemon.setText("Omanyte")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Omastar":
            self.window.ui.label_pokemon.setText("Omastar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kabuto":
            self.window.ui.label_pokemon.setText("Kabuto")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kabutops":
            self.window.ui.label_pokemon.setText("Kabutops")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Aerodactyl":
            self.window.ui.label_pokemon.setText("Aerodactyl")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Snorlax":
            self.window.ui.label_pokemon.setText("Snorlax")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Articuno":
            self.window.ui.label_pokemon.setText("Articuno")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zapdos":
            self.window.ui.label_pokemon.setText("Zapdos")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Moltres":
            self.window.ui.label_pokemon.setText("Moltres")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dratini":
            self.window.ui.label_pokemon.setText("Dratini")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dragonair":
            self.window.ui.label_pokemon.setText("Dragonair")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dragonite":
            self.window.ui.label_pokemon.setText("Dragonite")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mewtwo":
            self.window.ui.label_pokemon.setText("Mewtwo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mew":
            self.window.ui.label_pokemon.setText("Mew")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chikorita":
            self.window.ui.label_pokemon.setText("Chikorita")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bayleef":
            self.window.ui.label_pokemon.setText("Bayleef")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Meganium":
            self.window.ui.label_pokemon.setText("Meganium")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cyndaquil":
            self.window.ui.label_pokemon.setText("Cyndaquil")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Quilava":
            self.window.ui.label_pokemon.setText("Quilava")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Typhlosion":
            self.window.ui.label_pokemon.setText("Typhlosion")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Totodile":
            self.window.ui.label_pokemon.setText("Totodile")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Croconaw":
            self.window.ui.label_pokemon.setText("Croconaw")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Feraligatr":
            self.window.ui.label_pokemon.setText("Feraligatr")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sentret":
            self.window.ui.label_pokemon.setText("Sentret")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Furret":
            self.window.ui.label_pokemon.setText("Furret")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hoothoot":
            self.window.ui.label_pokemon.setText("Hoothoot")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Noctowl":
            self.window.ui.label_pokemon.setText("Noctowl")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ledyba":
            self.window.ui.label_pokemon.setText("Ledyba")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ledian":
            self.window.ui.label_pokemon.setText("Ledian")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spinarak":
            self.window.ui.label_pokemon.setText("Spinarak")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ariados":
            self.window.ui.label_pokemon.setText("Ariados")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Crobat":
            self.window.ui.label_pokemon.setText("Crobat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chinchou":
            self.window.ui.label_pokemon.setText("Chinchou")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lanturn":
            self.window.ui.label_pokemon.setText("Lanturn")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pichu":
            self.window.ui.label_pokemon.setText("Pichu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cleffa":
            self.window.ui.label_pokemon.setText("Cleffa")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Igglybuff":
            self.window.ui.label_pokemon.setText("Igglybuff")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Togepi":
            self.window.ui.label_pokemon.setText("Togepi")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Togetic":
            self.window.ui.label_pokemon.setText("Togetic")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Natu":
            self.window.ui.label_pokemon.setText("Natu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Xatu":
            self.window.ui.label_pokemon.setText("Xatu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mareep":
            self.window.ui.label_pokemon.setText("Mareep")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Flaaffy":
            self.window.ui.label_pokemon.setText("Flaaffy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ampharos":
            self.window.ui.label_pokemon.setText("Ampharos")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bellossom":
            self.window.ui.label_pokemon.setText("Bellossom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Marill":
            self.window.ui.label_pokemon.setText("Marill")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Azumarill":
            self.window.ui.label_pokemon.setText("Azumarill")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sudowoodo":
            self.window.ui.label_pokemon.setText("Sudowoodo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Politoed":
            self.window.ui.label_pokemon.setText("Politoed")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hoppip":
            self.window.ui.label_pokemon.setText("Hoppip")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Skiploom":
            self.window.ui.label_pokemon.setText("Skiploom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Jumpluff":
            self.window.ui.label_pokemon.setText("Jumpluff")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Aipom":
            self.window.ui.label_pokemon.setText("Aipom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sunkern":
            self.window.ui.label_pokemon.setText("Sunkern")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sunflora":
            self.window.ui.label_pokemon.setText("Sunflora")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Yanma":
            self.window.ui.label_pokemon.setText("Yanma")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wooper":
            self.window.ui.label_pokemon.setText("Wooper")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Quagsire":
            self.window.ui.label_pokemon.setText("Quagsire")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Espeon":
            self.window.ui.label_pokemon.setText("Espeon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Umbreon":
            self.window.ui.label_pokemon.setText("Umbreon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Murkrow":
            self.window.ui.label_pokemon.setText("Murkrow")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Slowking":
            self.window.ui.label_pokemon.setText("Slowking")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Misdreavus":
            self.window.ui.label_pokemon.setText("Misdreavus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Unown":
            self.window.ui.label_pokemon.setText("Unown")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wobbuffet":
            self.window.ui.label_pokemon.setText("Wobbuffet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Girafarig":
            self.window.ui.label_pokemon.setText("Girafarig")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pineco":
            self.window.ui.label_pokemon.setText("Pineco")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Forretress":
            self.window.ui.label_pokemon.setText("Forretress")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dunsparce":
            self.window.ui.label_pokemon.setText("Dunsparce")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gligar":
            self.window.ui.label_pokemon.setText("Gligar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Steelix":
            self.window.ui.label_pokemon.setText("Steelix")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Snubbull":
            self.window.ui.label_pokemon.setText("Snubbull")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Granbull":
            self.window.ui.label_pokemon.setText("Granbull")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Qwilfish":
            self.window.ui.label_pokemon.setText("Qwilfish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Scizor":
            self.window.ui.label_pokemon.setText("Scizor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shuckle":
            self.window.ui.label_pokemon.setText("Shuckle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Heracross":
            self.window.ui.label_pokemon.setText("Heracross")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sneasel":
            self.window.ui.label_pokemon.setText("Sneasel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Teddiursa":
            self.window.ui.label_pokemon.setText("Teddiursa")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ursaring":
            self.window.ui.label_pokemon.setText("Ursaring")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Slugma":
            self.window.ui.label_pokemon.setText("Slugma")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Magcargo":
            self.window.ui.label_pokemon.setText("Magcargo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Swinub":
            self.window.ui.label_pokemon.setText("Swinub")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Piloswine":
            self.window.ui.label_pokemon.setText("Piloswine")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Corsola":
            self.window.ui.label_pokemon.setText("Corsola")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Remoraid":
            self.window.ui.label_pokemon.setText("Remoraid")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Octillery":
            self.window.ui.label_pokemon.setText("Octillery")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Delibird":
            self.window.ui.label_pokemon.setText("Delibird")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mantine":
            self.window.ui.label_pokemon.setText("Mantine")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Skarmory":
            self.window.ui.label_pokemon.setText("Skarmory")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Houndour":
            self.window.ui.label_pokemon.setText("Houndour")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Houndoom":
            self.window.ui.label_pokemon.setText("Houndoom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kingdra":
            self.window.ui.label_pokemon.setText("Kingdra")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Phanpy":
            self.window.ui.label_pokemon.setText("Phanpy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Donphan":
            self.window.ui.label_pokemon.setText("Donphan")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Porygon2":
            self.window.ui.label_pokemon.setText("Porygon2")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Stantler":
            self.window.ui.label_pokemon.setText("Stantler")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Smeargle":
            self.window.ui.label_pokemon.setText("Smeargle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tyrogue":
            self.window.ui.label_pokemon.setText("Tyrogue")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hitmontop":
            self.window.ui.label_pokemon.setText("Hitmontop")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Smoochum":
            self.window.ui.label_pokemon.setText("Smoochum")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Elekid":
            self.window.ui.label_pokemon.setText("Elekid")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Magby":
            self.window.ui.label_pokemon.setText("Magby")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Miltank":
            self.window.ui.label_pokemon.setText("Miltank")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Blissey":
            self.window.ui.label_pokemon.setText("Blissey")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Raikou":
            self.window.ui.label_pokemon.setText("Raikou")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Entei":
            self.window.ui.label_pokemon.setText("Entei")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Suicune":
            self.window.ui.label_pokemon.setText("Suicune")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Larvitar":
            self.window.ui.label_pokemon.setText("Larvitar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pupitar":
            self.window.ui.label_pokemon.setText("Pupitar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tyranitar":
            self.window.ui.label_pokemon.setText("Tyranitar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lugia":
            self.window.ui.label_pokemon.setText("Lugia")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ho-oh":
            self.window.ui.label_pokemon.setText("Ho-oh")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Celebi":
            self.window.ui.label_pokemon.setText("Celebi")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Treecko":
            self.window.ui.label_pokemon.setText("Treecko")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Grovyle":
            self.window.ui.label_pokemon.setText("Grovyle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sceptile":
            self.window.ui.label_pokemon.setText("Sceptile")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Torchic":
            self.window.ui.label_pokemon.setText("Torchic")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Combusken":
            self.window.ui.label_pokemon.setText("Combusken")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Blaziken":
            self.window.ui.label_pokemon.setText("Blaziken")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mudkip":
            self.window.ui.label_pokemon.setText("Mudkip")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Marshtomp":
            self.window.ui.label_pokemon.setText("Marshtomp")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Swampert":
            self.window.ui.label_pokemon.setText("Swampert")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Poochyena":
            self.window.ui.label_pokemon.setText("Poochyena")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mightyena":
            self.window.ui.label_pokemon.setText("Mightyena")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zigzagoon":
            self.window.ui.label_pokemon.setText("Zigzagoon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Linoone":
            self.window.ui.label_pokemon.setText("Linoone")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wurmple":
            self.window.ui.label_pokemon.setText("Wurmple")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Silcoon":
            self.window.ui.label_pokemon.setText("Silcoon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Beautifly":
            self.window.ui.label_pokemon.setText("Beautifly")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cascoon":
            self.window.ui.label_pokemon.setText("Cascoon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dustox":
            self.window.ui.label_pokemon.setText("Dustox")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lotad":
            self.window.ui.label_pokemon.setText("Lotad")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lombre":
            self.window.ui.label_pokemon.setText("Lombre")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ludicolo":
            self.window.ui.label_pokemon.setText("Ludicolo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Seedot":
            self.window.ui.label_pokemon.setText("Seedot")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nuzleaf":
            self.window.ui.label_pokemon.setText("Nuzleaf")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shiftry":
            self.window.ui.label_pokemon.setText("Shiftry")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Taillow":
            self.window.ui.label_pokemon.setText("Taillow")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Swellow":
            self.window.ui.label_pokemon.setText("Swellow")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wingull":
            self.window.ui.label_pokemon.setText("Wingull")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pelipper":
            self.window.ui.label_pokemon.setText("Pelipper")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ralts":
            self.window.ui.label_pokemon.setText("Ralts")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kirlia":
            self.window.ui.label_pokemon.setText("Kirlia")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gardevoir":
            self.window.ui.label_pokemon.setText("Gardevoir")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Surskit":
            self.window.ui.label_pokemon.setText("Surskit")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Masquerain":
            self.window.ui.label_pokemon.setText("Masquerain")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shroomish":
            self.window.ui.label_pokemon.setText("Shroomish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Breloom":
            self.window.ui.label_pokemon.setText("Breloom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Slakoth":
            self.window.ui.label_pokemon.setText("Slakoth")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vigoroth":
            self.window.ui.label_pokemon.setText("Vigoroth")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Slaking":
            self.window.ui.label_pokemon.setText("Slaking")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nincada":
            self.window.ui.label_pokemon.setText("Nincada")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ninjask":
            self.window.ui.label_pokemon.setText("Ninjask")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shedinja":
            self.window.ui.label_pokemon.setText("Shedinja")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Whismur":
            self.window.ui.label_pokemon.setText("Whismur")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Loudred":
            self.window.ui.label_pokemon.setText("Loudred")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Exploud":
            self.window.ui.label_pokemon.setText("Exploud")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Makuhita":
            self.window.ui.label_pokemon.setText("Makuhita")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hariyama":
            self.window.ui.label_pokemon.setText("Hariyama")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Azurill":
            self.window.ui.label_pokemon.setText("Azurill")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nosepass":
            self.window.ui.label_pokemon.setText("Nosepass")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Skitty":
            self.window.ui.label_pokemon.setText("Skitty")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Delcatty":
            self.window.ui.label_pokemon.setText("Delcatty")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sableye":
            self.window.ui.label_pokemon.setText("Sableye")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mawile":
            self.window.ui.label_pokemon.setText("Mawile")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Aron":
            self.window.ui.label_pokemon.setText("Aron")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lairon":
            self.window.ui.label_pokemon.setText("Lairon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Aggron":
            self.window.ui.label_pokemon.setText("Aggron")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Meditite":
            self.window.ui.label_pokemon.setText("Meditite")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Medicham":
            self.window.ui.label_pokemon.setText("Medicham")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Electrike":
            self.window.ui.label_pokemon.setText("Electrike")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Manectric":
            self.window.ui.label_pokemon.setText("Manectric")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Plusle":
            self.window.ui.label_pokemon.setText("Plusle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Minun":
            self.window.ui.label_pokemon.setText("Minun")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Volbeat":
            self.window.ui.label_pokemon.setText("Volbeat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Illumise":
            self.window.ui.label_pokemon.setText("Illumise")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Roselia":
            self.window.ui.label_pokemon.setText("Roselia")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gulpin":
            self.window.ui.label_pokemon.setText("Gulpin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Swalot":
            self.window.ui.label_pokemon.setText("Swalot")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Carvanha":
            self.window.ui.label_pokemon.setText("Carvanha")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sharpedo":
            self.window.ui.label_pokemon.setText("Sharpedo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wailmer":
            self.window.ui.label_pokemon.setText("Wailmer")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wailord":
            self.window.ui.label_pokemon.setText("Wailord")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Numel":
            self.window.ui.label_pokemon.setText("Numel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Camerupt":
            self.window.ui.label_pokemon.setText("Camerupt")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Torkoal":
            self.window.ui.label_pokemon.setText("Torkoal")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spoink":
            self.window.ui.label_pokemon.setText("Spoink")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Grumpig":
            self.window.ui.label_pokemon.setText("Grumpig")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spinda":
            self.window.ui.label_pokemon.setText("Spinda")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Trapinch":
            self.window.ui.label_pokemon.setText("Trapinch")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vibrava":
            self.window.ui.label_pokemon.setText("Vibrava")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Flygon":
            self.window.ui.label_pokemon.setText("Flygon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cacnea":
            self.window.ui.label_pokemon.setText("Cacnea")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cacturne":
            self.window.ui.label_pokemon.setText("Cacturne")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Swablu":
            self.window.ui.label_pokemon.setText("Swablu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Altaria":
            self.window.ui.label_pokemon.setText("Altaria")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zangoose":
            self.window.ui.label_pokemon.setText("Zangoose")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Seviper":
            self.window.ui.label_pokemon.setText("Seviper")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lunatone":
            self.window.ui.label_pokemon.setText("Lunatone")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Solrock":
            self.window.ui.label_pokemon.setText("Solrock")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Barboach":
            self.window.ui.label_pokemon.setText("Barboach")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Whiscash":
            self.window.ui.label_pokemon.setText("Whiscash")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Corphish":
            self.window.ui.label_pokemon.setText("Corphish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Crawdaunt":
            self.window.ui.label_pokemon.setText("Crawdaunt")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Baltoy":
            self.window.ui.label_pokemon.setText("Baltoy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Claydol":
            self.window.ui.label_pokemon.setText("Claydol")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lileep":
            self.window.ui.label_pokemon.setText("Lileep")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cradily":
            self.window.ui.label_pokemon.setText("Cradily")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Anorith":
            self.window.ui.label_pokemon.setText("Anorith")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Armaldo":
            self.window.ui.label_pokemon.setText("Armaldo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Feebas":
            self.window.ui.label_pokemon.setText("Feebas")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Milotic":
            self.window.ui.label_pokemon.setText("Milotic")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Castform":
            self.window.ui.label_pokemon.setText("Castform")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kecleon":
            self.window.ui.label_pokemon.setText("Kecleon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shuppet":
            self.window.ui.label_pokemon.setText("Shuppet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Banette":
            self.window.ui.label_pokemon.setText("Banette")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Duskull":
            self.window.ui.label_pokemon.setText("Duskull")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dusclops":
            self.window.ui.label_pokemon.setText("Dusclops")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tropius":
            self.window.ui.label_pokemon.setText("Tropius")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chimecho":
            self.window.ui.label_pokemon.setText("Chimecho")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Absol":
            self.window.ui.label_pokemon.setText("Absol")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wynaut":
            self.window.ui.label_pokemon.setText("Wynaut")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Snorunt":
            self.window.ui.label_pokemon.setText("Snorunt")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Glalie":
            self.window.ui.label_pokemon.setText("Glalie")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spheal":
            self.window.ui.label_pokemon.setText("Spheal")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sealeo":
            self.window.ui.label_pokemon.setText("Sealeo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Walrein":
            self.window.ui.label_pokemon.setText("Walrein")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Clamperl":
            self.window.ui.label_pokemon.setText("Clamperl")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Huntail":
            self.window.ui.label_pokemon.setText("Huntail")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gorebyss":
            self.window.ui.label_pokemon.setText("Gorebyss")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Relicanth":
            self.window.ui.label_pokemon.setText("Relicanth")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Luvdisc":
            self.window.ui.label_pokemon.setText("Luvdisc")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bagon":
            self.window.ui.label_pokemon.setText("Bagon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shelgon":
            self.window.ui.label_pokemon.setText("Shelgon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Salamence":
            self.window.ui.label_pokemon.setText("Salamence")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Beldum":
            self.window.ui.label_pokemon.setText("Beldum")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Metang":
            self.window.ui.label_pokemon.setText("Metang")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Metagross":
            self.window.ui.label_pokemon.setText("Metagross")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Regirock":
            self.window.ui.label_pokemon.setText("Regirock")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Regice":
            self.window.ui.label_pokemon.setText("Regice")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Registeel":
            self.window.ui.label_pokemon.setText("Registeel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Latias":
            self.window.ui.label_pokemon.setText("Latias")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Latios":
            self.window.ui.label_pokemon.setText("Latios")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kyogre":
            self.window.ui.label_pokemon.setText("Kyogre")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Groudon":
            self.window.ui.label_pokemon.setText("Groudon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rayquaza":
            self.window.ui.label_pokemon.setText("Rayquaza")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Jirachi":
            self.window.ui.label_pokemon.setText("Jirachi")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Deoxys":
            self.window.ui.label_pokemon.setText("Deoxys")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Turtwig":
            self.window.ui.label_pokemon.setText("Turtwig")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Grotle":
            self.window.ui.label_pokemon.setText("Grotle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Torterra":
            self.window.ui.label_pokemon.setText("Torterra")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chimchar":
            self.window.ui.label_pokemon.setText("Chimchar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Monferno":
            self.window.ui.label_pokemon.setText("Monferno")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Infernape":
            self.window.ui.label_pokemon.setText("Infernape")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Piplup":
            self.window.ui.label_pokemon.setText("Piplup")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Prinplup":
            self.window.ui.label_pokemon.setText("Prinplup")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Empoleon":
            self.window.ui.label_pokemon.setText("Empoleon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Starly":
            self.window.ui.label_pokemon.setText("Starly")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Staravia":
            self.window.ui.label_pokemon.setText("Staravia")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Staraptor":
            self.window.ui.label_pokemon.setText("Staraptor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bidoof":
            self.window.ui.label_pokemon.setText("Bidoof")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bibarel":
            self.window.ui.label_pokemon.setText("Bibarel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kricketot":
            self.window.ui.label_pokemon.setText("Kricketot")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kricketune":
            self.window.ui.label_pokemon.setText("Kricketune")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shinx":
            self.window.ui.label_pokemon.setText("Shinx")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Luxio":
            self.window.ui.label_pokemon.setText("Luxio")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Luxray":
            self.window.ui.label_pokemon.setText("Luxray")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Budew":
            self.window.ui.label_pokemon.setText("Budew")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Roserade":
            self.window.ui.label_pokemon.setText("Roserade")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cranidos":
            self.window.ui.label_pokemon.setText("Cranidos")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rampardos":
            self.window.ui.label_pokemon.setText("Rampardos")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shieldon":
            self.window.ui.label_pokemon.setText("Shieldon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bastiodon":
            self.window.ui.label_pokemon.setText("Bastiodon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Burmy":
            self.window.ui.label_pokemon.setText("Burmy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wormadam":
            self.window.ui.label_pokemon.setText("Wormadam")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mothim":
            self.window.ui.label_pokemon.setText("Mothim")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Combee":
            self.window.ui.label_pokemon.setText("Combee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vespiquen":
            self.window.ui.label_pokemon.setText("Vespiquen")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pachirisu":
            self.window.ui.label_pokemon.setText("Pachirisu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Buizel":
            self.window.ui.label_pokemon.setText("Buizel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Floatzel":
            self.window.ui.label_pokemon.setText("Floatzel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cherubi":
            self.window.ui.label_pokemon.setText("Cherubi")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cherrim":
            self.window.ui.label_pokemon.setText("Cherrim")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shellos":
            self.window.ui.label_pokemon.setText("Shellos")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gastrodon":
            self.window.ui.label_pokemon.setText("Gastrodon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ambipom":
            self.window.ui.label_pokemon.setText("Ambipom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Drifloon":
            self.window.ui.label_pokemon.setText("Drifloon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Drifblim":
            self.window.ui.label_pokemon.setText("Drifblim")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Buneary":
            self.window.ui.label_pokemon.setText("Buneary")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lopunny":
            self.window.ui.label_pokemon.setText("Lopunny")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mismagius":
            self.window.ui.label_pokemon.setText("Mismagius")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Honchkrow":
            self.window.ui.label_pokemon.setText("Honchkrow")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Glameow":
            self.window.ui.label_pokemon.setText("Glameow")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Purugly":
            self.window.ui.label_pokemon.setText("Purugly")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chingling":
            self.window.ui.label_pokemon.setText("Chingling")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Stunky":
            self.window.ui.label_pokemon.setText("Stunky")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Skuntank":
            self.window.ui.label_pokemon.setText("Skuntank")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bronzor":
            self.window.ui.label_pokemon.setText("Bronzor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bronzong":
            self.window.ui.label_pokemon.setText("Bronzong")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bonsly":
            self.window.ui.label_pokemon.setText("Bonsly")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mime Jr.":
            self.window.ui.label_pokemon.setText("Mime Jr.")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Happiny":
            self.window.ui.label_pokemon.setText("Happiny")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chatot":
            self.window.ui.label_pokemon.setText("Chatot")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spiritomb":
            self.window.ui.label_pokemon.setText("Spiritomb")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gible":
            self.window.ui.label_pokemon.setText("Gible")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gabite":
            self.window.ui.label_pokemon.setText("Gabite")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Garchomp":
            self.window.ui.label_pokemon.setText("Garchomp")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Munchlax":
            self.window.ui.label_pokemon.setText("Munchlax")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Riolu":
            self.window.ui.label_pokemon.setText("Riolu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lucario":
            self.window.ui.label_pokemon.setText("Lucario")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hippopotas":
            self.window.ui.label_pokemon.setText("Hippopotas")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hippowdon":
            self.window.ui.label_pokemon.setText("Hippowdon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Skorupi":
            self.window.ui.label_pokemon.setText("Skorupi")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Drapion":
            self.window.ui.label_pokemon.setText("Drapion")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Croagunk":
            self.window.ui.label_pokemon.setText("Croagunk")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Toxicroak":
            self.window.ui.label_pokemon.setText("Toxicroak")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Carnivine":
            self.window.ui.label_pokemon.setText("Carnivine")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Finneon":
            self.window.ui.label_pokemon.setText("Finneon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lumineon":
            self.window.ui.label_pokemon.setText("Lumineon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mantyke":
            self.window.ui.label_pokemon.setText("Mantyke")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Snover":
            self.window.ui.label_pokemon.setText("Snover")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Abomasnow":
            self.window.ui.label_pokemon.setText("Abomasnow")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Weavile":
            self.window.ui.label_pokemon.setText("Weavile")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Magnezone":
            self.window.ui.label_pokemon.setText("Magnezone")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lickilicky":
            self.window.ui.label_pokemon.setText("Lickilicky")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rhyperior":
            self.window.ui.label_pokemon.setText("Rhyperior")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tangrowth":
            self.window.ui.label_pokemon.setText("Tangrowth")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Electivire":
            self.window.ui.label_pokemon.setText("Electivire")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Magmortar":
            self.window.ui.label_pokemon.setText("Magmortar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Togekiss":
            self.window.ui.label_pokemon.setText("Togekiss")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Yanmega":
            self.window.ui.label_pokemon.setText("Yanmega")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Leafeon":
            self.window.ui.label_pokemon.setText("Leafeon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Glaceon":
            self.window.ui.label_pokemon.setText("Glaceon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gliscor":
            self.window.ui.label_pokemon.setText("Gliscor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mamoswine":
            self.window.ui.label_pokemon.setText("Mamoswine")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Porygon-Z":
            self.window.ui.label_pokemon.setText("Porygon-Z")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gallade":
            self.window.ui.label_pokemon.setText("Gallade")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Probopass":
            self.window.ui.label_pokemon.setText("Probopass")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dusknoir":
            self.window.ui.label_pokemon.setText("Dusknoir")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Froslass":
            self.window.ui.label_pokemon.setText("Froslass")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rotom":
            self.window.ui.label_pokemon.setText("Rotom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Uxie":
            self.window.ui.label_pokemon.setText("Uxie")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mesprit":
            self.window.ui.label_pokemon.setText("Mesprit")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Azelf":
            self.window.ui.label_pokemon.setText("Azelf")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dialga":
            self.window.ui.label_pokemon.setText("Dialga")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Palkia":
            self.window.ui.label_pokemon.setText("Palkia")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Heatran":
            self.window.ui.label_pokemon.setText("Heatran")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Regigigas":
            self.window.ui.label_pokemon.setText("Regigigas")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Giratina":
            self.window.ui.label_pokemon.setText("Giratina")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cresselia":
            self.window.ui.label_pokemon.setText("Cresselia")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Phione":
            self.window.ui.label_pokemon.setText("Phione")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Manaphy":
            self.window.ui.label_pokemon.setText("Manaphy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Darkrai":
            self.window.ui.label_pokemon.setText("Darkrai")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shaymin":
            self.window.ui.label_pokemon.setText("Shaymin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Arceus":
            self.window.ui.label_pokemon.setText("Arceus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Victini":
            self.window.ui.label_pokemon.setText("Victini")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Snivy":
            self.window.ui.label_pokemon.setText("Snivy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Servine":
            self.window.ui.label_pokemon.setText("Servine")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Serperior":
            self.window.ui.label_pokemon.setText("Serperior")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tepig":
            self.window.ui.label_pokemon.setText("Tepig")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pignite":
            self.window.ui.label_pokemon.setText("Pignite")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Emboar":
            self.window.ui.label_pokemon.setText("Emboar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Oshawott":
            self.window.ui.label_pokemon.setText("Oshawott")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dewott":
            self.window.ui.label_pokemon.setText("Dewott")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Samurott":
            self.window.ui.label_pokemon.setText("Samurott")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Patrat":
            self.window.ui.label_pokemon.setText("Patrat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Watchog":
            self.window.ui.label_pokemon.setText("Watchog")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lillipup":
            self.window.ui.label_pokemon.setText("Lillipup")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Herdier":
            self.window.ui.label_pokemon.setText("Herdier")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Stoutland":
            self.window.ui.label_pokemon.setText("Stoutland")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Purrloin":
            self.window.ui.label_pokemon.setText("Purrloin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Liepard":
            self.window.ui.label_pokemon.setText("Liepard")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pansage":
            self.window.ui.label_pokemon.setText("Pansage")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Simisage":
            self.window.ui.label_pokemon.setText("Simisage")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pansear":
            self.window.ui.label_pokemon.setText("Pansear")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Simisear":
            self.window.ui.label_pokemon.setText("Simisear")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Panpour":
            self.window.ui.label_pokemon.setText("Panpour")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Simipour":
            self.window.ui.label_pokemon.setText("Simipour")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Munna":
            self.window.ui.label_pokemon.setText("Munna")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Musharna":
            self.window.ui.label_pokemon.setText("Musharna")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pidove":
            self.window.ui.label_pokemon.setText("Pidove")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tranquill":
            self.window.ui.label_pokemon.setText("Tranquill")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Unfezant":
            self.window.ui.label_pokemon.setText("Unfezant")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Blitzle":
            self.window.ui.label_pokemon.setText("Blitzle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zebstrika":
            self.window.ui.label_pokemon.setText("Zebstrika")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Roggenrola":
            self.window.ui.label_pokemon.setText("Roggenrola")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Boldore":
            self.window.ui.label_pokemon.setText("Boldore")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gigalith":
            self.window.ui.label_pokemon.setText("Gigalith")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Woobat":
            self.window.ui.label_pokemon.setText("Woobat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Swoobat":
            self.window.ui.label_pokemon.setText("Swoobat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Drilbur":
            self.window.ui.label_pokemon.setText("Drilbur")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Excadrill":
            self.window.ui.label_pokemon.setText("Excadrill")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Audino":
            self.window.ui.label_pokemon.setText("Audino")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Timburr":
            self.window.ui.label_pokemon.setText("Timburr")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gurdurr":
            self.window.ui.label_pokemon.setText("Gurdurr")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Conkeldurr":
            self.window.ui.label_pokemon.setText("Conkeldurr")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tympole":
            self.window.ui.label_pokemon.setText("Tympole")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Palpitoad":
            self.window.ui.label_pokemon.setText("Palpitoad")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Seismitoad":
            self.window.ui.label_pokemon.setText("Seismitoad")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Throh":
            self.window.ui.label_pokemon.setText("Throh")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sawk":
            self.window.ui.label_pokemon.setText("Sawk")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sewaddle":
            self.window.ui.label_pokemon.setText("Sewaddle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Swadloon":
            self.window.ui.label_pokemon.setText("Swadloon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Leavanny":
            self.window.ui.label_pokemon.setText("Leavanny")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Venipede":
            self.window.ui.label_pokemon.setText("Venipede")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Whirlipede":
            self.window.ui.label_pokemon.setText("Whirlipede")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Scolipede":
            self.window.ui.label_pokemon.setText("Scolipede")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cottonee":
            self.window.ui.label_pokemon.setText("Cottonee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Whimsicott":
            self.window.ui.label_pokemon.setText("Whimsicott")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Petilil":
            self.window.ui.label_pokemon.setText("Petilil")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lilligant":
            self.window.ui.label_pokemon.setText("Lilligant")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Basculin":
            self.window.ui.label_pokemon.setText("Basculin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sandile":
            self.window.ui.label_pokemon.setText("Sandile")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Krokorok":
            self.window.ui.label_pokemon.setText("Krokorok")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Krookodile":
            self.window.ui.label_pokemon.setText("Krookodile")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Darumaka":
            self.window.ui.label_pokemon.setText("Darumaka")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Darmanitan":
            self.window.ui.label_pokemon.setText("Darmanitan")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Maractus":
            self.window.ui.label_pokemon.setText("Maractus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dwebble":
            self.window.ui.label_pokemon.setText("Dwebble")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Crustle":
            self.window.ui.label_pokemon.setText("Crustle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Scraggy":
            self.window.ui.label_pokemon.setText("Scraggy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Scrafty":
            self.window.ui.label_pokemon.setText("Scrafty")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sigilyph":
            self.window.ui.label_pokemon.setText("Sigilyph")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Yamask":
            self.window.ui.label_pokemon.setText("Yamask")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cofagrigus":
            self.window.ui.label_pokemon.setText("Cofagrigus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tirtouga":
            self.window.ui.label_pokemon.setText("Tirtouga")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Carracosta":
            self.window.ui.label_pokemon.setText("Carracosta")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Archen":
            self.window.ui.label_pokemon.setText("Archen")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Archeops":
            self.window.ui.label_pokemon.setText("Archeops")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Trubbish":
            self.window.ui.label_pokemon.setText("Trubbish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Garbodor":
            self.window.ui.label_pokemon.setText("Garbodor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zorua":
            self.window.ui.label_pokemon.setText("Zorua")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zoroark":
            self.window.ui.label_pokemon.setText("Zoroark")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Minccino":
            self.window.ui.label_pokemon.setText("Minccino")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cinccino":
            self.window.ui.label_pokemon.setText("Cinccino")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gothita":
            self.window.ui.label_pokemon.setText("Gothita")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gothorita":
            self.window.ui.label_pokemon.setText("Gothorita")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gothitelle":
            self.window.ui.label_pokemon.setText("Gothitelle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Solosis":
            self.window.ui.label_pokemon.setText("Solosis")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Duosion":
            self.window.ui.label_pokemon.setText("Duosion")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Reuniclus":
            self.window.ui.label_pokemon.setText("Reuniclus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ducklett":
            self.window.ui.label_pokemon.setText("Ducklett")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Swanna":
            self.window.ui.label_pokemon.setText("Swanna")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vanillite":
            self.window.ui.label_pokemon.setText("Vanillite")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vanillish":
            self.window.ui.label_pokemon.setText("Vanillish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vanilluxe":
            self.window.ui.label_pokemon.setText("Vanilluxe")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Deerling":
            self.window.ui.label_pokemon.setText("Deerling")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sawsbuck":
            self.window.ui.label_pokemon.setText("Sawsbuck")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Emolga":
            self.window.ui.label_pokemon.setText("Emolga")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Karrablast":
            self.window.ui.label_pokemon.setText("Karrablast")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Escavalier":
            self.window.ui.label_pokemon.setText("Escavalier")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Foongus":
            self.window.ui.label_pokemon.setText("Foongus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Amoonguss":
            self.window.ui.label_pokemon.setText("Amoonguss")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Frillish":
            self.window.ui.label_pokemon.setText("Frillish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Jellicent":
            self.window.ui.label_pokemon.setText("Jellicent")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Alomomola":
            self.window.ui.label_pokemon.setText("Alomomola")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Joltik":
            self.window.ui.label_pokemon.setText("Joltik")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Galvantula":
            self.window.ui.label_pokemon.setText("Galvantula")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ferroseed":
            self.window.ui.label_pokemon.setText("Ferroseed")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ferrothorn":
            self.window.ui.label_pokemon.setText("Ferrothorn")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Klink":
            self.window.ui.label_pokemon.setText("Klink")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Klang":
            self.window.ui.label_pokemon.setText("Klang")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Klinklang":
            self.window.ui.label_pokemon.setText("Klinklang")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tynamo":
            self.window.ui.label_pokemon.setText("Tynamo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Eelektrik":
            self.window.ui.label_pokemon.setText("Eelektrik")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Eelektross":
            self.window.ui.label_pokemon.setText("Eelektross")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Elgyem":
            self.window.ui.label_pokemon.setText("Elgyem")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Beheeyem":
            self.window.ui.label_pokemon.setText("Beheeyem")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Litwick":
            self.window.ui.label_pokemon.setText("Litwick")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lampent":
            self.window.ui.label_pokemon.setText("Lampent")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chandelure":
            self.window.ui.label_pokemon.setText("Chandelure")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Axew":
            self.window.ui.label_pokemon.setText("Axew")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Fraxure":
            self.window.ui.label_pokemon.setText("Fraxure")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Haxorus":
            self.window.ui.label_pokemon.setText("Haxorus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cubchoo":
            self.window.ui.label_pokemon.setText("Cubchoo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Beartic":
            self.window.ui.label_pokemon.setText("Beartic")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cryogonal":
            self.window.ui.label_pokemon.setText("Cryogonal")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shelmet":
            self.window.ui.label_pokemon.setText("Shelmet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Accelgor":
            self.window.ui.label_pokemon.setText("Accelgor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Stunfisk":
            self.window.ui.label_pokemon.setText("Stunfisk")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mienfoo":
            self.window.ui.label_pokemon.setText("Mienfoo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mienshao":
            self.window.ui.label_pokemon.setText("Mienshao")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Druddigon":
            self.window.ui.label_pokemon.setText("Druddigon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Golett":
            self.window.ui.label_pokemon.setText("Golett")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Golurk":
            self.window.ui.label_pokemon.setText("Golurk")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pawniard":
            self.window.ui.label_pokemon.setText("Pawniard")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bisharp":
            self.window.ui.label_pokemon.setText("Bisharp")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bouffalant":
            self.window.ui.label_pokemon.setText("Bouffalant")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rufflet":
            self.window.ui.label_pokemon.setText("Rufflet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Braviary":
            self.window.ui.label_pokemon.setText("Braviary")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vullaby":
            self.window.ui.label_pokemon.setText("Vullaby")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mandibuzz":
            self.window.ui.label_pokemon.setText("Mandibuzz")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Heatmor":
            self.window.ui.label_pokemon.setText("Heatmor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Durant":
            self.window.ui.label_pokemon.setText("Durant")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Deino":
            self.window.ui.label_pokemon.setText("Deino")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zweilous":
            self.window.ui.label_pokemon.setText("Zweilous")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hydreigon":
            self.window.ui.label_pokemon.setText("Hydreigon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Larvesta":
            self.window.ui.label_pokemon.setText("Larvesta")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Volcarona":
            self.window.ui.label_pokemon.setText("Volcarona")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cobalion":
            self.window.ui.label_pokemon.setText("Cobalion")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Terrakion":
            self.window.ui.label_pokemon.setText("Terrakion")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Virizion":
            self.window.ui.label_pokemon.setText("Virizion")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tornadus":
            self.window.ui.label_pokemon.setText("Tornadus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Thundurus":
            self.window.ui.label_pokemon.setText("Thundurus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Reshiram":
            self.window.ui.label_pokemon.setText("Reshiram")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zekrom":
            self.window.ui.label_pokemon.setText("Zekrom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Landorus":
            self.window.ui.label_pokemon.setText("Landorus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kyurem":
            self.window.ui.label_pokemon.setText("Kyurem")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Keldeo":
            self.window.ui.label_pokemon.setText("Keldeo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Meloetta":
            self.window.ui.label_pokemon.setText("Meloetta")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Genesect":
            self.window.ui.label_pokemon.setText("Genesect")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chespin":
            self.window.ui.label_pokemon.setText("Chespin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Quilladin":
            self.window.ui.label_pokemon.setText("Quilladin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chesnaught":
            self.window.ui.label_pokemon.setText("Chesnaught")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Fennekin":
            self.window.ui.label_pokemon.setText("Fennekin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Braixen":
            self.window.ui.label_pokemon.setText("Braixen")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Delphox":
            self.window.ui.label_pokemon.setText("Delphox")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Froakie":
            self.window.ui.label_pokemon.setText("Froakie")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Frogadier":
            self.window.ui.label_pokemon.setText("Frogadier")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Greninja":
            self.window.ui.label_pokemon.setText("Greninja")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bunnelby":
            self.window.ui.label_pokemon.setText("Bunnelby")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Diggersby":
            self.window.ui.label_pokemon.setText("Diggersby")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Fletchling":
            self.window.ui.label_pokemon.setText("Fletchling")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Fletchinder":
            self.window.ui.label_pokemon.setText("Fletchinder")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Talonflame":
            self.window.ui.label_pokemon.setText("Talonflame")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Scatterbug":
            self.window.ui.label_pokemon.setText("Scatterbug")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spewpa":
            self.window.ui.label_pokemon.setText("Spewpa")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vivillon":
            self.window.ui.label_pokemon.setText("Vivillon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Litleo":
            self.window.ui.label_pokemon.setText("Litleo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pyroar":
            self.window.ui.label_pokemon.setText("Pyroar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Flabébé":
            self.window.ui.label_pokemon.setText("Flabébé")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Floette":
            self.window.ui.label_pokemon.setText("Floette")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Florges":
            self.window.ui.label_pokemon.setText("Florges")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Skiddo":
            self.window.ui.label_pokemon.setText("Skiddo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gogoat":
            self.window.ui.label_pokemon.setText("Gogoat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pancham":
            self.window.ui.label_pokemon.setText("Pancham")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pangoro":
            self.window.ui.label_pokemon.setText("Pangoro")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Furfrou":
            self.window.ui.label_pokemon.setText("Furfrou")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Espurr":
            self.window.ui.label_pokemon.setText("Espurr")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Meowstic":
            self.window.ui.label_pokemon.setText("Meowstic")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Honedge":
            self.window.ui.label_pokemon.setText("Honedge")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Doublade":
            self.window.ui.label_pokemon.setText("Doublade")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Aegislash":
            self.window.ui.label_pokemon.setText("Aegislash")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spritzee":
            self.window.ui.label_pokemon.setText("Spritzee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Aromatisse":
            self.window.ui.label_pokemon.setText("Aromatisse")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Swirlix":
            self.window.ui.label_pokemon.setText("Swirlix")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Slurpuff":
            self.window.ui.label_pokemon.setText("Slurpuff")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Inkay":
            self.window.ui.label_pokemon.setText("Inkay")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Malamar":
            self.window.ui.label_pokemon.setText("Malamar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Binacle":
            self.window.ui.label_pokemon.setText("Binacle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Barbaracle":
            self.window.ui.label_pokemon.setText("Barbaracle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Skrelp":
            self.window.ui.label_pokemon.setText("Skrelp")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dragalge":
            self.window.ui.label_pokemon.setText("Dragalge")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Clauncher":
            self.window.ui.label_pokemon.setText("Clauncher")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Clawitzer":
            self.window.ui.label_pokemon.setText("Clawitzer")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Helioptile":
            self.window.ui.label_pokemon.setText("Helioptile")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Heliolisk":
            self.window.ui.label_pokemon.setText("Heliolisk")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tyrunt":
            self.window.ui.label_pokemon.setText("Tyrunt")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tyrantrum":
            self.window.ui.label_pokemon.setText("Tyrantrum")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Amaura":
            self.window.ui.label_pokemon.setText("Amaura")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Aurorus":
            self.window.ui.label_pokemon.setText("Aurorus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sylveon":
            self.window.ui.label_pokemon.setText("Sylveon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hawlucha":
            self.window.ui.label_pokemon.setText("Hawlucha")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dedenne":
            self.window.ui.label_pokemon.setText("Dedenne")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Carbink":
            self.window.ui.label_pokemon.setText("Carbink")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Goomy":
            self.window.ui.label_pokemon.setText("Goomy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sliggoo":
            self.window.ui.label_pokemon.setText("Sliggoo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Goodra":
            self.window.ui.label_pokemon.setText("Goodra")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Klefki":
            self.window.ui.label_pokemon.setText("Klefki")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Phantump":
            self.window.ui.label_pokemon.setText("Phantump")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Trevenant":
            self.window.ui.label_pokemon.setText("Trevenant")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pumpkaboo":
            self.window.ui.label_pokemon.setText("Pumpkaboo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gourgeist":
            self.window.ui.label_pokemon.setText("Gourgeist")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bergmite":
            self.window.ui.label_pokemon.setText("Bergmite")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Avalugg":
            self.window.ui.label_pokemon.setText("Avalugg")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Noibat":
            self.window.ui.label_pokemon.setText("Noibat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Noivern":
            self.window.ui.label_pokemon.setText("Noivern")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Xerneas":
            self.window.ui.label_pokemon.setText("Xerneas")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Yveltal":
            self.window.ui.label_pokemon.setText("Yveltal")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zygarde":
            self.window.ui.label_pokemon.setText("Zygarde")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Diancie":
            self.window.ui.label_pokemon.setText("Diancie")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hoopa":
            self.window.ui.label_pokemon.setText("Hoopa")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Volcanion":
            self.window.ui.label_pokemon.setText("Volcanion")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rowlet":
            self.window.ui.label_pokemon.setText("Rowlet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dartrix":
            self.window.ui.label_pokemon.setText("Dartrix")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Decidueye":
            self.window.ui.label_pokemon.setText("Decidueye")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Litten":
            self.window.ui.label_pokemon.setText("Litten")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Torracat":
            self.window.ui.label_pokemon.setText("Torracat")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Incineroar":
            self.window.ui.label_pokemon.setText("Incineroar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Popplio":
            self.window.ui.label_pokemon.setText("Popplio")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Brionne":
            self.window.ui.label_pokemon.setText("Brionne")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Primarina":
            self.window.ui.label_pokemon.setText("Primarina")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pikipek":
            self.window.ui.label_pokemon.setText("Pikipek")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Trumbeak":
            self.window.ui.label_pokemon.setText("Trumbeak")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Toucannon":
            self.window.ui.label_pokemon.setText("Toucannon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Yungoos":
            self.window.ui.label_pokemon.setText("Yungoos")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gumshoos":
            self.window.ui.label_pokemon.setText("Gumshoos")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Grubbin":
            self.window.ui.label_pokemon.setText("Grubbin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Charjabug":
            self.window.ui.label_pokemon.setText("Charjabug")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Vikavolt":
            self.window.ui.label_pokemon.setText("Vikavolt")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Crabrawler":
            self.window.ui.label_pokemon.setText("Crabrawler")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Crabominable":
            self.window.ui.label_pokemon.setText("Crabominable")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Oricorio":
            self.window.ui.label_pokemon.setText("Oricorio")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cutiefly":
            self.window.ui.label_pokemon.setText("Cutiefly")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ribombee":
            self.window.ui.label_pokemon.setText("Ribombee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rockruff":
            self.window.ui.label_pokemon.setText("Rockruff")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lycanroc":
            self.window.ui.label_pokemon.setText("Lycanroc")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wishiwashi":
            self.window.ui.label_pokemon.setText("Wishiwashi")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mareanie":
            self.window.ui.label_pokemon.setText("Mareanie")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Toxapex":
            self.window.ui.label_pokemon.setText("Toxapex")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mudbray":
            self.window.ui.label_pokemon.setText("Mudbray")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mudsdale":
            self.window.ui.label_pokemon.setText("Mudsdale")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dewpider":
            self.window.ui.label_pokemon.setText("Dewpider")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Araquanid":
            self.window.ui.label_pokemon.setText("Araquanid")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Fomantis":
            self.window.ui.label_pokemon.setText("Fomantis")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lurantis":
            self.window.ui.label_pokemon.setText("Lurantis")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Morelull":
            self.window.ui.label_pokemon.setText("Morelull")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shiinotic":
            self.window.ui.label_pokemon.setText("Shiinotic")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Salandit":
            self.window.ui.label_pokemon.setText("Salandit")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Salazzle":
            self.window.ui.label_pokemon.setText("Salazzle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Stufful":
            self.window.ui.label_pokemon.setText("Stufful")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bewear":
            self.window.ui.label_pokemon.setText("Bewear")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bounsweet":
            self.window.ui.label_pokemon.setText("Bounsweet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Steenee":
            self.window.ui.label_pokemon.setText("Steenee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tsareena":
            self.window.ui.label_pokemon.setText("Tsareena")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Comfey":
            self.window.ui.label_pokemon.setText("Comfey")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Oranguru":
            self.window.ui.label_pokemon.setText("Oranguru")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Passimian":
            self.window.ui.label_pokemon.setText("Passimian")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wimpod":
            self.window.ui.label_pokemon.setText("Wimpod")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Golisopod":
            self.window.ui.label_pokemon.setText("Golisopod")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sandygast":
            self.window.ui.label_pokemon.setText("Sandygast")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Palossand":
            self.window.ui.label_pokemon.setText("Palossand")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pyukumuku":
            self.window.ui.label_pokemon.setText("Pyukumuku")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Type: Null":
            self.window.ui.label_pokemon.setText("Type: Null")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Silvally":
            self.window.ui.label_pokemon.setText("Silvally")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Minior":
            self.window.ui.label_pokemon.setText("Minior")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Komala":
            self.window.ui.label_pokemon.setText("Komala")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Turtonator":
            self.window.ui.label_pokemon.setText("Turtonator")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Togedemaru":
            self.window.ui.label_pokemon.setText("Togedemaru")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mimikyu":
            self.window.ui.label_pokemon.setText("Mimikyu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bruxish":
            self.window.ui.label_pokemon.setText("Bruxish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Drampa":
            self.window.ui.label_pokemon.setText("Drampa")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dhelmise":
            self.window.ui.label_pokemon.setText("Dhelmise")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Jangmo-o":
            self.window.ui.label_pokemon.setText("Jangmo-o")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hakamo-o":
            self.window.ui.label_pokemon.setText("Hakamo-o")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kommo-o":
            self.window.ui.label_pokemon.setText("Kommo-o")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tapu Koko":
            self.window.ui.label_pokemon.setText("Tapu Koko")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tapu Lele":
            self.window.ui.label_pokemon.setText("Tapu Lele")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tapu Bulu":
            self.window.ui.label_pokemon.setText("Tapu Bulu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tapu Fini":
            self.window.ui.label_pokemon.setText("Tapu Fini")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cosmog":
            self.window.ui.label_pokemon.setText("Cosmog")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cosmoem":
            self.window.ui.label_pokemon.setText("Cosmoem")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Solgaleo":
            self.window.ui.label_pokemon.setText("Solgaleo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lunala":
            self.window.ui.label_pokemon.setText("Lunala")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nihilego":
            self.window.ui.label_pokemon.setText("Nihilego")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Buzzwole":
            self.window.ui.label_pokemon.setText("Buzzwole")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pheromosa":
            self.window.ui.label_pokemon.setText("Pheromosa")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Xurkitree":
            self.window.ui.label_pokemon.setText("Xurkitree")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Celesteela":
            self.window.ui.label_pokemon.setText("Celesteela")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kartana":
            self.window.ui.label_pokemon.setText("Kartana")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Guzzlord":
            self.window.ui.label_pokemon.setText("Guzzlord")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Necrozma":
            self.window.ui.label_pokemon.setText("Necrozma")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Magearna":
            self.window.ui.label_pokemon.setText("Magearna")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Marshadow":
            self.window.ui.label_pokemon.setText("Marshadow")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Poipole":
            self.window.ui.label_pokemon.setText("Poipole")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Naganadel":
            self.window.ui.label_pokemon.setText("Naganadel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Stakataka":
            self.window.ui.label_pokemon.setText("Stakataka")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Blacephalon":
            self.window.ui.label_pokemon.setText("Blacephalon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zeraora":
            self.window.ui.label_pokemon.setText("Zeraora")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Meltan":
            self.window.ui.label_pokemon.setText("Meltan")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Melmetal":
            self.window.ui.label_pokemon.setText("Melmetal")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Grookey":
            self.window.ui.label_pokemon.setText("Grookey")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Thwackey":
            self.window.ui.label_pokemon.setText("Thwackey")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rillaboom":
            self.window.ui.label_pokemon.setText("Rillaboom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Scorbunny":
            self.window.ui.label_pokemon.setText("Scorbunny")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Raboot":
            self.window.ui.label_pokemon.setText("Raboot")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cinderace":
            self.window.ui.label_pokemon.setText("Cinderace")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sobble":
            self.window.ui.label_pokemon.setText("Sobble")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Drizzile":
            self.window.ui.label_pokemon.setText("Drizzile")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Inteleon":
            self.window.ui.label_pokemon.setText("Inteleon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Skwovet":
            self.window.ui.label_pokemon.setText("Skwovet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Greedent":
            self.window.ui.label_pokemon.setText("Greedent")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rookidee":
            self.window.ui.label_pokemon.setText("Rookidee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Corvisquire":
            self.window.ui.label_pokemon.setText("Corvisquire")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Corviknight":
            self.window.ui.label_pokemon.setText("Corviknight")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Blipbug":
            self.window.ui.label_pokemon.setText("Blipbug")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dottler":
            self.window.ui.label_pokemon.setText("Dottler")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Orbeetle":
            self.window.ui.label_pokemon.setText("Orbeetle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nickit":
            self.window.ui.label_pokemon.setText("Nickit")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Thievul":
            self.window.ui.label_pokemon.setText("Thievul")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gossifleur":
            self.window.ui.label_pokemon.setText("Gossifleur")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Eldegoss":
            self.window.ui.label_pokemon.setText("Eldegoss")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wooloo":
            self.window.ui.label_pokemon.setText("Wooloo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dubwool":
            self.window.ui.label_pokemon.setText("Dubwool")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chewtle":
            self.window.ui.label_pokemon.setText("Chewtle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Drednaw":
            self.window.ui.label_pokemon.setText("Drednaw")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Yamper":
            self.window.ui.label_pokemon.setText("Yamper")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Boltund":
            self.window.ui.label_pokemon.setText("Boltund")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rolycoly":
            self.window.ui.label_pokemon.setText("Rolycoly")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Carkol":
            self.window.ui.label_pokemon.setText("Carkol")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Coalossal":
            self.window.ui.label_pokemon.setText("Coalossal")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Applin":
            self.window.ui.label_pokemon.setText("Applin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Flapple":
            self.window.ui.label_pokemon.setText("Flapple")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Appletun":
            self.window.ui.label_pokemon.setText("Appletun")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Silicobra":
            self.window.ui.label_pokemon.setText("Silicobra")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sandaconda":
            self.window.ui.label_pokemon.setText("Sandaconda")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cramorant":
            self.window.ui.label_pokemon.setText("Cramorant")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Arrokuda":
            self.window.ui.label_pokemon.setText("Arrokuda")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Barraskewda":
            self.window.ui.label_pokemon.setText("Barraskewda")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Toxel":
            self.window.ui.label_pokemon.setText("Toxel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Toxtricity":
            self.window.ui.label_pokemon.setText("Toxtricity")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sizzlipede":
            self.window.ui.label_pokemon.setText("Sizzlipede")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Centiskorch":
            self.window.ui.label_pokemon.setText("Centiskorch")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Clobbopus":
            self.window.ui.label_pokemon.setText("Clobbopus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Grapploct":
            self.window.ui.label_pokemon.setText("Grapploct")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sinistea":
            self.window.ui.label_pokemon.setText("Sinistea")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Polteageist":
            self.window.ui.label_pokemon.setText("Polteageist")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hatenna":
            self.window.ui.label_pokemon.setText("Hatenna")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hattrem":
            self.window.ui.label_pokemon.setText("Hattrem")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hatterene":
            self.window.ui.label_pokemon.setText("Hatterene")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Impidimp":
            self.window.ui.label_pokemon.setText("Impidimp")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Morgrem":
            self.window.ui.label_pokemon.setText("Morgrem")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Grimmsnarl":
            self.window.ui.label_pokemon.setText("Grimmsnarl")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Obstagoon":
            self.window.ui.label_pokemon.setText("Obstagoon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Perrserker":
            self.window.ui.label_pokemon.setText("Perrserker")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cursola":
            self.window.ui.label_pokemon.setText("Cursola")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sirfetch'd":
            self.window.ui.label_pokemon.setText("Sirfetch'd")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mr. Rime":
            self.window.ui.label_pokemon.setText("Mr. Rime")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Runerigus":
            self.window.ui.label_pokemon.setText("Runerigus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Milcery":
            self.window.ui.label_pokemon.setText("Milcery")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Alcremie":
            self.window.ui.label_pokemon.setText("Alcremie")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Falinks":
            self.window.ui.label_pokemon.setText("Falinks")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pincurchin":
            self.window.ui.label_pokemon.setText("Pincurchin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Snom":
            self.window.ui.label_pokemon.setText("Snom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Frosmoth":
            self.window.ui.label_pokemon.setText("Frosmoth")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Stonjourner":
            self.window.ui.label_pokemon.setText("Stonjourner")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Eiscue":
            self.window.ui.label_pokemon.setText("Eiscue")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Indeedee":
            self.window.ui.label_pokemon.setText("Indeedee")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Morpeko":
            self.window.ui.label_pokemon.setText("Morpeko")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cufant":
            self.window.ui.label_pokemon.setText("Cufant")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Copperajah":
            self.window.ui.label_pokemon.setText("Copperajah")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dracozolt":
            self.window.ui.label_pokemon.setText("Dracozolt")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Arctozolt":
            self.window.ui.label_pokemon.setText("Arctozolt")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dracovish":
            self.window.ui.label_pokemon.setText("Dracovish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Arctovish":
            self.window.ui.label_pokemon.setText("Arctovish")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Duraludon":
            self.window.ui.label_pokemon.setText("Duraludon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dreepy":
            self.window.ui.label_pokemon.setText("Dreepy")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Drakloak":
            self.window.ui.label_pokemon.setText("Drakloak")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dragapult":
            self.window.ui.label_pokemon.setText("Dragapult")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zacian":
            self.window.ui.label_pokemon.setText("Zacian")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zamazenta":
            self.window.ui.label_pokemon.setText("Zamazenta")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Eternatus":
            self.window.ui.label_pokemon.setText("Eternatus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kubfu":
            self.window.ui.label_pokemon.setText("Kubfu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Urshifu":
            self.window.ui.label_pokemon.setText("Urshifu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Zarude":
            self.window.ui.label_pokemon.setText("Zarude")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Regieleki":
            self.window.ui.label_pokemon.setText("Regieleki")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Regidrago":
            self.window.ui.label_pokemon.setText("Regidrago")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Glastrier":
            self.window.ui.label_pokemon.setText("Glastrier")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spectrier":
            self.window.ui.label_pokemon.setText("Spectrier")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Calyrex":
            self.window.ui.label_pokemon.setText("Calyrex")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wyrdeer":
            self.window.ui.label_pokemon.setText("Wyrdeer")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kleavor":
            self.window.ui.label_pokemon.setText("Kleavor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ursaluna":
            self.window.ui.label_pokemon.setText("Ursaluna")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Basculegion":
            self.window.ui.label_pokemon.setText("Basculegion")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sneasler":
            self.window.ui.label_pokemon.setText("Sneasler")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Overqwil":
            self.window.ui.label_pokemon.setText("Overqwil")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Enamorus":
            self.window.ui.label_pokemon.setText("Enamorus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sprigatito":
            self.window.ui.label_pokemon.setText("Sprigatito")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Floragato":
            self.window.ui.label_pokemon.setText("Floragato")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Meowscarada":
            self.window.ui.label_pokemon.setText("Meowscarada")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Fuecoco":
            self.window.ui.label_pokemon.setText("Fuecoco")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Crocalor":
            self.window.ui.label_pokemon.setText("Crocalor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Skeledirge":
            self.window.ui.label_pokemon.setText("Skeledirge")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Quaxly":
            self.window.ui.label_pokemon.setText("Quaxly")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Quaxwell":
            self.window.ui.label_pokemon.setText("Quaxwell")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Quaquaval":
            self.window.ui.label_pokemon.setText("Quaquaval")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lechonk":
            self.window.ui.label_pokemon.setText("Lechonk")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Oinkologne":
            self.window.ui.label_pokemon.setText("Oinkologne")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tarountula":
            self.window.ui.label_pokemon.setText("Tarountula")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Spidops":
            self.window.ui.label_pokemon.setText("Spidops")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nymble":
            self.window.ui.label_pokemon.setText("Nymble")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Lokix":
            self.window.ui.label_pokemon.setText("Lokix")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pawmi":
            self.window.ui.label_pokemon.setText("Pawmi")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pawmo":
            self.window.ui.label_pokemon.setText("Pawmo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Pawmot":
            self.window.ui.label_pokemon.setText("Pawmot")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tandemaus":
            self.window.ui.label_pokemon.setText("Tandemaus")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Maushold":
            self.window.ui.label_pokemon.setText("Maushold")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Fidough":
            self.window.ui.label_pokemon.setText("Fidough")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dachsbun":
            self.window.ui.label_pokemon.setText("Dachsbun")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Smoliv":
            self.window.ui.label_pokemon.setText("Smoliv")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dolliv":
            self.window.ui.label_pokemon.setText("Dolliv")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Arboliva":
            self.window.ui.label_pokemon.setText("Arboliva")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Squawkabilly":
            self.window.ui.label_pokemon.setText("Squawkabilly")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Nacli":
            self.window.ui.label_pokemon.setText("Nacli")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Naclstack":
            self.window.ui.label_pokemon.setText("Naclstack")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Garganacl":
            self.window.ui.label_pokemon.setText("Garganacl")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Charcadet":
            self.window.ui.label_pokemon.setText("Charcadet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Armarouge":
            self.window.ui.label_pokemon.setText("Armarouge")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ceruledge":
            self.window.ui.label_pokemon.setText("Ceruledge")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tadbulb":
            self.window.ui.label_pokemon.setText("Tadbulb")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bellibolt":
            self.window.ui.label_pokemon.setText("Bellibolt")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wattrel":
            self.window.ui.label_pokemon.setText("Wattrel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kilowattrel":
            self.window.ui.label_pokemon.setText("Kilowattrel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Maschiff":
            self.window.ui.label_pokemon.setText("Maschiff")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Mabosstiff":
            self.window.ui.label_pokemon.setText("Mabosstiff")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Shroodle":
            self.window.ui.label_pokemon.setText("Shroodle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Grafaiai":
            self.window.ui.label_pokemon.setText("Grafaiai")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bramblin":
            self.window.ui.label_pokemon.setText("Bramblin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Brambleghast":
            self.window.ui.label_pokemon.setText("Brambleghast")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Toedscool":
            self.window.ui.label_pokemon.setText("Toedscool")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Toedscruel":
            self.window.ui.label_pokemon.setText("Toedscruel")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Klawf":
            self.window.ui.label_pokemon.setText("Klawf")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Capsakid":
            self.window.ui.label_pokemon.setText("Capsakid")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Scovillain":
            self.window.ui.label_pokemon.setText("Scovillain")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rellor":
            self.window.ui.label_pokemon.setText("Rellor")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Rabsca":
            self.window.ui.label_pokemon.setText("Rabsca")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Flittle":
            self.window.ui.label_pokemon.setText("Flittle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Espathra":
            self.window.ui.label_pokemon.setText("Espathra")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tinkatink":
            self.window.ui.label_pokemon.setText("Tinkatink")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tinkatuff":
            self.window.ui.label_pokemon.setText("Tinkatuff")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tinkaton":
            self.window.ui.label_pokemon.setText("Tinkaton")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wiglett":
            self.window.ui.label_pokemon.setText("Wiglett")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wugtrio":
            self.window.ui.label_pokemon.setText("Wugtrio")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Bombirdier":
            self.window.ui.label_pokemon.setText("Bombirdier")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Finizen":
            self.window.ui.label_pokemon.setText("Finizen")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Palafin":
            self.window.ui.label_pokemon.setText("Palafin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Varoom":
            self.window.ui.label_pokemon.setText("Varoom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Revavroom":
            self.window.ui.label_pokemon.setText("Revavroom")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cyclizar":
            self.window.ui.label_pokemon.setText("Cyclizar")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Orthworm":
            self.window.ui.label_pokemon.setText("Orthworm")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Glimmet":
            self.window.ui.label_pokemon.setText("Glimmet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Glimmora":
            self.window.ui.label_pokemon.setText("Glimmora")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Greavard":
            self.window.ui.label_pokemon.setText("Greavard")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Houndstone":
            self.window.ui.label_pokemon.setText("Houndstone")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Flamigo":
            self.window.ui.label_pokemon.setText("Flamigo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cetoddle":
            self.window.ui.label_pokemon.setText("Cetoddle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Cetitan":
            self.window.ui.label_pokemon.setText("Cetitan")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Veluza":
            self.window.ui.label_pokemon.setText("Veluza")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dondozo":
            self.window.ui.label_pokemon.setText("Dondozo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Tatsugiri":
            self.window.ui.label_pokemon.setText("Tatsugiri")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Annihilape":
            self.window.ui.label_pokemon.setText("Annihilape")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Clodsire":
            self.window.ui.label_pokemon.setText("Clodsire")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Farigiraf":
            self.window.ui.label_pokemon.setText("Farigiraf")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dudunsparce":
            self.window.ui.label_pokemon.setText("Dudunsparce")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Kingambit":
            self.window.ui.label_pokemon.setText("Kingambit")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Great Tusk":
            self.window.ui.label_pokemon.setText("Great Tusk")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Scream Tail":
            self.window.ui.label_pokemon.setText("Scream Tail")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Brute Bonnet":
            self.window.ui.label_pokemon.setText("Brute Bonnet")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Flutter Mane":
            self.window.ui.label_pokemon.setText("Flutter Mane")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Slither Wing":
            self.window.ui.label_pokemon.setText("Slither Wing")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sandy Shocks":
            self.window.ui.label_pokemon.setText("Sandy Shocks")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Treads":
            self.window.ui.label_pokemon.setText("Iron Treads")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Bundle":
            self.window.ui.label_pokemon.setText("Iron Bundle")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Hands":
            self.window.ui.label_pokemon.setText("Iron Hands")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Jugulis":
            self.window.ui.label_pokemon.setText("Iron Jugulis")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Moth":
            self.window.ui.label_pokemon.setText("Iron Moth")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Thorns":
            self.window.ui.label_pokemon.setText("Iron Thorns")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Frigibax":
            self.window.ui.label_pokemon.setText("Frigibax")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Arctibax":
            self.window.ui.label_pokemon.setText("Arctibax")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Baxcalibur":
            self.window.ui.label_pokemon.setText("Baxcalibur")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gimmighoul":
            self.window.ui.label_pokemon.setText("Gimmighoul")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gholdengo":
            self.window.ui.label_pokemon.setText("Gholdengo")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Wo-Chien":
            self.window.ui.label_pokemon.setText("Wo-Chien")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chien-Pao":
            self.window.ui.label_pokemon.setText("Chien-Pao")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ting-Lu":
            self.window.ui.label_pokemon.setText("Ting-Lu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Chi-Yu":
            self.window.ui.label_pokemon.setText("Chi-Yu")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Roaring Moon":
            self.window.ui.label_pokemon.setText("Roaring Moon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Valiant":
            self.window.ui.label_pokemon.setText("Iron Valiant")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Koraidon":
            self.window.ui.label_pokemon.setText("Koraidon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Miraidon":
            self.window.ui.label_pokemon.setText("Miraidon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Walking Wake":
            self.window.ui.label_pokemon.setText("Walking Wake")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Leaves":
            self.window.ui.label_pokemon.setText("Iron Leaves")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Dipplin":
            self.window.ui.label_pokemon.setText("Dipplin")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Poltchageist":
            self.window.ui.label_pokemon.setText("Poltchageist")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Sinistcha":
            self.window.ui.label_pokemon.setText("Sinistcha")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Okidogi":
            self.window.ui.label_pokemon.setText("Okidogi")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Munkidori":
            self.window.ui.label_pokemon.setText("Munkidori")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Fezandipiti":
            self.window.ui.label_pokemon.setText("Fezandipiti")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Ogerpon":
            self.window.ui.label_pokemon.setText("Ogerpon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Archaludon":
            self.window.ui.label_pokemon.setText("Archaludon")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Hydrapple":
            self.window.ui.label_pokemon.setText("Hydrapple")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Gouging Fire":
            self.window.ui.label_pokemon.setText("Gouging Fire")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Raging Bolt":
            self.window.ui.label_pokemon.setText("Raging Bolt")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Boulder":
            self.window.ui.label_pokemon.setText("Iron Boulder")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Iron Crown":
            self.window.ui.label_pokemon.setText("Iron Crown")
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText()  == "Terapagos":
            self.window.ui.label_pokemon.setText("Terapagos")
            self.window.show()
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pecharunt":
            self.window.ui.label_pokemon.setText("Pecharunt")
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Error")
            dialog.setText(f"{self.ui.comboBox_Pokemon.currentText()} is not a valid Pokemon")
            dialog.exec()

    def open_move_window(self):
        self.window = MoveWindow()
        self.window.setWindowTitle(self.ui.comboBox_Move.currentText())
        if self.ui.comboBox_Move.currentText() == "Pound":
            self.window.ui.label_move.setText("Pound")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Karate Chop":
            self.window.ui.label_move.setText("Karate Chop")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Double Slap":
            self.window.ui.label_move.setText("Double Slap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Comet Punch":
            self.window.ui.label_move.setText("Comet Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mega Punch":
            self.window.ui.label_move.setText("Mega Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pay Day":
            self.window.ui.label_move.setText("Pay Day")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fire Punch":
            self.window.ui.label_move.setText("Fire Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ice Punch":
            self.window.ui.label_move.setText("Ice Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thunder Punch":
            self.window.ui.label_move.setText("Thunder Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Scratch":
            self.window.ui.label_move.setText("Scratch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Vise Grip":
            self.window.ui.label_move.setText("Vise Grip")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Guillotine":
            self.window.ui.label_move.setText("Guillotine")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Razor Wind":
            self.window.ui.label_move.setText("Razor Wind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Swords Dance":
            self.window.ui.label_move.setText("Swords Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Cut":
            self.window.ui.label_move.setText("Cut")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Gust":
            self.window.ui.label_move.setText("Gust")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wing Attack":
            self.window.ui.label_move.setText("Wing Attack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Whirlwind":
            self.window.ui.label_move.setText("Whirlwind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fly":
            self.window.ui.label_move.setText("Fly")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bind":
            self.window.ui.label_move.setText("Bind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Slam":
            self.window.ui.label_move.setText("Slam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Vine Whip":
            self.window.ui.label_move.setText("Vine Whip")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stomp":
            self.window.ui.label_move.setText("Stomp")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Double Kick":
            self.window.ui.label_move.setText("Double Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mega Kick":
            self.window.ui.label_move.setText("Mega Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Jump Kick":
            self.window.ui.label_move.setText("Jump Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rolling Kick":
            self.window.ui.label_move.setText("Rolling Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sand Attack":
            self.window.ui.label_move.setText("Sand Attack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Headbutt":
            self.window.ui.label_move.setText("Headbutt")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Horn Attack":
            self.window.ui.label_move.setText("Horn Attack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fury Attack":
            self.window.ui.label_move.setText("Fury Attack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Horn Drill":
            self.window.ui.label_move.setText("Horn Drill")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tackle":
            self.window.ui.label_move.setText("Tackle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Body Slam":
            self.window.ui.label_move.setText("Body Slam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wrap":
            self.window.ui.label_move.setText("Wrap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Take Down":
            self.window.ui.label_move.setText("Take Down")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thrash":
            self.window.ui.label_move.setText("Thrash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Double Edge":
            self.window.ui.label_move.setText("Double Edge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tail Whip":
            self.window.ui.label_move.setText("Tail Whip")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Poison Sting":
            self.window.ui.label_move.setText("Poison Sting")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Twineedle":
            self.window.ui.label_move.setText("Twineedle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pin Missile":
            self.window.ui.label_move.setText("Pin Missile")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Leer":
            self.window.ui.label_move.setText("Leer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bite":
            self.window.ui.label_move.setText("Bite")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Growl":
            self.window.ui.label_move.setText("Growl")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Roar":
            self.window.ui.label_move.setText("Roar")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sing":
            self.window.ui.label_move.setText("Sing")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Supersonic":
            self.window.ui.label_move.setText("Supersonic")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sonic Boom":
            self.window.ui.label_move.setText("Sonic Boom")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Disable":
            self.window.ui.label_move.setText("Disable")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Acid":
            self.window.ui.label_move.setText("Acid")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ember":
            self.window.ui.label_move.setText("Ember")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flamethrower":
            self.window.ui.label_move.setText("Flamethrower")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mist":
            self.window.ui.label_move.setText("Mist")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Water Gun":
            self.window.ui.label_move.setText("Water Gun")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hydro Pump":
            self.window.ui.label_move.setText("Hydro Pump")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Surf":
            self.window.ui.label_move.setText("Surf")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ice Beam":
            self.window.ui.label_move.setText("Ice Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Blizzard":
            self.window.ui.label_move.setText("Blizzard")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psybeam":
            self.window.ui.label_move.setText("Psybeam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bubble Beam":
            self.window.ui.label_move.setText("Bubble Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aurora Beam":
            self.window.ui.label_move.setText("Aurora Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hyper Beam":
            self.window.ui.label_move.setText("Hyper Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Peck":
            self.window.ui.label_move.setText("Peck")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Drill Peck":
            self.window.ui.label_move.setText("Drill Peck")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Submission":
            self.window.ui.label_move.setText("Submission")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Low Kick":
            self.window.ui.label_move.setText("Low Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Counter":
            self.window.ui.label_move.setText("Counter")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Seismic Toss":
            self.window.ui.label_move.setText("Seismic Toss")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Strength":
            self.window.ui.label_move.setText("Strength")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Absorb":
            self.window.ui.label_move.setText("Absorb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mega Drain":
            self.window.ui.label_move.setText("Mega Drain")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Leech Seed":
            self.window.ui.label_move.setText("Leech Seed")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Growth":
            self.window.ui.label_move.setText("Growth")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Razor Leaf":
            self.window.ui.label_move.setText("Razor Leaf")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Solar Beam":
            self.window.ui.label_move.setText("Solar Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Poison Powder":
            self.window.ui.label_move.setText("Poison Powder")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stun Spore":
            self.window.ui.label_move.setText("Stun Spore")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sleep Powder":
            self.window.ui.label_move.setText("Sleep Powder")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Petal Dance":
            self.window.ui.label_move.setText("Petal Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "String Shot":
            self.window.ui.label_move.setText("String Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Rage":
            self.window.ui.label_move.setText("Dragon Rage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fire Spin":
            self.window.ui.label_move.setText("Fire Spin")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thunder Shock":
            self.window.ui.label_move.setText("Thunder Shock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thunderbolt":
            self.window.ui.label_move.setText("Thunderbolt")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thunder Wave":
            self.window.ui.label_move.setText("Thunder Wave")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thunder":
            self.window.ui.label_move.setText("Thunder")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rock Throw":
            self.window.ui.label_move.setText("Rock Throw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Earthquake":
            self.window.ui.label_move.setText("Earthquake")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fissure":
            self.window.ui.label_move.setText("Fissure")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dig":
            self.window.ui.label_move.setText("Dig")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Toxic":
            self.window.ui.label_move.setText("Toxic")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Confusion":
            self.window.ui.label_move.setText("Confusion")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psychic":
            self.window.ui.label_move.setText("Psychic")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hypnosis":
            self.window.ui.label_move.setText("Hypnosis")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Meditate":
            self.window.ui.label_move.setText("Meditate")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Agility":
            self.window.ui.label_move.setText("Agility")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Quick Attack":
            self.window.ui.label_move.setText("Quick Attack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rage":
            self.window.ui.label_move.setText("Rage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Teleport":
            self.window.ui.label_move.setText("Teleport")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Night Shade":
            self.window.ui.label_move.setText("Night Shade")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mimic":
            self.window.ui.label_move.setText("Mimic")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Screech":
            self.window.ui.label_move.setText("Screech")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Double Team":
            self.window.ui.label_move.setText("Double Team")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Recover":
            self.window.ui.label_move.setText("Recover")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Harden":
            self.window.ui.label_move.setText("Harden")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Minimize":
            self.window.ui.label_move.setText("Minimize")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Smokescreen":
            self.window.ui.label_move.setText("Smokescreen")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Confuse Ray":
            self.window.ui.label_move.setText("Confuse Ray")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Withdraw":
            self.window.ui.label_move.setText("Withdraw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Defense Curl":
            self.window.ui.label_move.setText("Defense Curl")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Barrier":
            self.window.ui.label_move.setText("Barrier")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Light Screen":
            self.window.ui.label_move.setText("Light Screen")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Haze":
            self.window.ui.label_move.setText("Haze")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Reflect":
            self.window.ui.label_move.setText("Reflect")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Focus Energy":
            self.window.ui.label_move.setText("Focus Energy")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bide":
            self.window.ui.label_move.setText("Bide")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Metronome":
            self.window.ui.label_move.setText("Metronome")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mirror Move":
            self.window.ui.label_move.setText("Mirror Move")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Self Destruct":
            self.window.ui.label_move.setText("Self Destruct")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Egg Bomb":
            self.window.ui.label_move.setText("Egg Bomb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lick":
            self.window.ui.label_move.setText("Lick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Smog":
            self.window.ui.label_move.setText("Smog")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sludge":
            self.window.ui.label_move.setText("Sludge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bone Club":
            self.window.ui.label_move.setText("Bone Club")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fire Blast":
            self.window.ui.label_move.setText("Fire Blast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Waterfall":
            self.window.ui.label_move.setText("Waterfall")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Clamp":
            self.window.ui.label_move.setText("Clamp")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Swift":
            self.window.ui.label_move.setText("Swift")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Skull Bash":
            self.window.ui.label_move.setText("Skull Bash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spike Cannon":
            self.window.ui.label_move.setText("Spike Cannon")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Constrict":
            self.window.ui.label_move.setText("Constrict")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Amnesia":
            self.window.ui.label_move.setText("Amnesia")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Kinesis":
            self.window.ui.label_move.setText("Kinesis")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Soft Boiled":
            self.window.ui.label_move.setText("Soft Boiled")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "High Jump Kick":
            self.window.ui.label_move.setText("High Jump Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Glare":
            self.window.ui.label_move.setText("Glare")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dream Eater":
            self.window.ui.label_move.setText("Dream Eater")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Poison Gas":
            self.window.ui.label_move.setText("Poison Gas")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Barrage":
            self.window.ui.label_move.setText("Barrage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Leech Life":
            self.window.ui.label_move.setText("Leech Life")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lovely Kiss":
            self.window.ui.label_move.setText("Lovely Kiss")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sky Attack":
            self.window.ui.label_move.setText("Sky Attack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Transform":
            self.window.ui.label_move.setText("Transform")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bubble":
            self.window.ui.label_move.setText("Bubble")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dizzy Punch":
            self.window.ui.label_move.setText("Dizzy Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spore":
            self.window.ui.label_move.setText("Spore")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flash":
            self.window.ui.label_move.setText("Flash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psywave":
            self.window.ui.label_move.setText("Psywave")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Splash":
            self.window.ui.label_move.setText("Splash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Acid Armor":
            self.window.ui.label_move.setText("Acid Armor")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Crabhammer":
            self.window.ui.label_move.setText("Crabhammer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Explosion":
            self.window.ui.label_move.setText("Explosion")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fury Swipes":
            self.window.ui.label_move.setText("Fury Swipes")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bonemerang":
            self.window.ui.label_move.setText("Bonemerang")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rest":
            self.window.ui.label_move.setText("Rest")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rock Slide":
            self.window.ui.label_move.setText("Rock Slide")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hyper Fang":
            self.window.ui.label_move.setText("Hyper Fang")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sharpen":
            self.window.ui.label_move.setText("Sharpen")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Conversion":
            self.window.ui.label_move.setText("Conversion")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tri Attack":
            self.window.ui.label_move.setText("Tri Attack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Super Fang":
            self.window.ui.label_move.setText("Super Fang")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Slash":
            self.window.ui.label_move.setText("Slash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Substitute":
            self.window.ui.label_move.setText("Substitute")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Struggle":
            self.window.ui.label_move.setText("Struggle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sketch":
            self.window.ui.label_move.setText("Sketch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Triple Kick":
            self.window.ui.label_move.setText("Triple Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thief":
            self.window.ui.label_move.setText("Thief")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spider Web":
            self.window.ui.label_move.setText("Spider Web")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mind Reader":
            self.window.ui.label_move.setText("Mind Reader")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Nightmare":
            self.window.ui.label_move.setText("Nightmare")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flame Wheel":
            self.window.ui.label_move.setText("Flame Wheel")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Snore":
            self.window.ui.label_move.setText("Snore")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Curse":
            self.window.ui.label_move.setText("Curse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flail":
            self.window.ui.label_move.setText("Flail")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Conversion ":
            self.window.ui.label_move.setText("Conversion ")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aeroblast":
            self.window.ui.label_move.setText("Aeroblast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Cotton Spore":
            self.window.ui.label_move.setText("Cotton Spore")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Reversal":
            self.window.ui.label_move.setText("Reversal")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spite":
            self.window.ui.label_move.setText("Spite")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Powder Snow":
            self.window.ui.label_move.setText("Powder Snow")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Protect":
            self.window.ui.label_move.setText("Protect")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mach Punch":
            self.window.ui.label_move.setText("Mach Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Scary Face":
            self.window.ui.label_move.setText("Scary Face")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Feint Attack":
            self.window.ui.label_move.setText("Feint Attack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sweet Kiss":
            self.window.ui.label_move.setText("Sweet Kiss")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Belly Drum":
            self.window.ui.label_move.setText("Belly Drum")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sludge Bomb":
            self.window.ui.label_move.setText("Sludge Bomb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mud Slap":
            self.window.ui.label_move.setText("Mud Slap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Octazooka":
            self.window.ui.label_move.setText("Octazooka")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spikes":
            self.window.ui.label_move.setText("Spikes")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Zap Cannon":
            self.window.ui.label_move.setText("Zap Cannon")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Foresight":
            self.window.ui.label_move.setText("Foresight")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Destiny Bond":
            self.window.ui.label_move.setText("Destiny Bond")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Perish Song":
            self.window.ui.label_move.setText("Perish Song")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Icy Wind":
            self.window.ui.label_move.setText("Icy Wind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Detect":
            self.window.ui.label_move.setText("Detect")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bone Rush":
            self.window.ui.label_move.setText("Bone Rush")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lock On":
            self.window.ui.label_move.setText("Lock On")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Outrage":
            self.window.ui.label_move.setText("Outrage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sandstorm":
            self.window.ui.label_move.setText("Sandstorm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Giga Drain":
            self.window.ui.label_move.setText("Giga Drain")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Endure":
            self.window.ui.label_move.setText("Endure")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Charm":
            self.window.ui.label_move.setText("Charm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rollout":
            self.window.ui.label_move.setText("Rollout")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "False Swipe":
            self.window.ui.label_move.setText("False Swipe")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Swagger":
            self.window.ui.label_move.setText("Swagger")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Milk Drink":
            self.window.ui.label_move.setText("Milk Drink")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spark":
            self.window.ui.label_move.setText("Spark")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fury Cutter":
            self.window.ui.label_move.setText("Fury Cutter")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Steel Wing":
            self.window.ui.label_move.setText("Steel Wing")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mean Look":
            self.window.ui.label_move.setText("Mean Look")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Attract":
            self.window.ui.label_move.setText("Attract")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sleep Talk":
            self.window.ui.label_move.setText("Sleep Talk")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Heal Bell":
            self.window.ui.label_move.setText("Heal Bell")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Return":
            self.window.ui.label_move.setText("Return")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Present":
            self.window.ui.label_move.setText("Present")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Frustration":
            self.window.ui.label_move.setText("Frustration")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Safeguard":
            self.window.ui.label_move.setText("Safeguard")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pain Split":
            self.window.ui.label_move.setText("Pain Split")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sacred Fire":
            self.window.ui.label_move.setText("Sacred Fire")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magnitude":
            self.window.ui.label_move.setText("Magnitude")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dynamic Punch":
            self.window.ui.label_move.setText("Dynamic Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Megahorn":
            self.window.ui.label_move.setText("Megahorn")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Breath":
            self.window.ui.label_move.setText("Dragon Breath")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Baton Pass":
            self.window.ui.label_move.setText("Baton Pass")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Encore":
            self.window.ui.label_move.setText("Encore")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pursuit":
            self.window.ui.label_move.setText("Pursuit")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rapid Spin":
            self.window.ui.label_move.setText("Rapid Spin")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sweet Scent":
            self.window.ui.label_move.setText("Sweet Scent")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Iron Tail":
            self.window.ui.label_move.setText("Iron Tail")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Metal Claw":
            self.window.ui.label_move.setText("Metal Claw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Vital Throw":
            self.window.ui.label_move.setText("Vital Throw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Morning Sun":
            self.window.ui.label_move.setText("Morning Sun")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Synthesis":
            self.window.ui.label_move.setText("Synthesis")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Moonlight":
            self.window.ui.label_move.setText("Moonlight")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hidden Power":
            self.window.ui.label_move.setText("Hidden Power")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Cross Chop":
            self.window.ui.label_move.setText("Cross Chop")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Twister":
            self.window.ui.label_move.setText("Twister")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rain Dance":
            self.window.ui.label_move.setText("Rain Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sunny Day":
            self.window.ui.label_move.setText("Sunny Day")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Crunch":
            self.window.ui.label_move.setText("Crunch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mirror Coat":
            self.window.ui.label_move.setText("Mirror Coat")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psych Up":
            self.window.ui.label_move.setText("Psych Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Extreme Speed":
            self.window.ui.label_move.setText("Extreme Speed")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ancient Power":
            self.window.ui.label_move.setText("Ancient Power")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shadow Ball":
            self.window.ui.label_move.setText("Shadow Ball")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Future Sight":
            self.window.ui.label_move.setText("Future Sight")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rock Smash":
            self.window.ui.label_move.setText("Rock Smash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Whirlpool":
            self.window.ui.label_move.setText("Whirlpool")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Beat Up":
            self.window.ui.label_move.setText("Beat Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fake Out":
            self.window.ui.label_move.setText("Fake Out")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Uproar":
            self.window.ui.label_move.setText("Uproar")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stockpile":
            self.window.ui.label_move.setText("Stockpile")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spit Up":
            self.window.ui.label_move.setText("Spit Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Swallow":
            self.window.ui.label_move.setText("Swallow")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Heat Wave":
            self.window.ui.label_move.setText("Heat Wave")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hail":
            self.window.ui.label_move.setText("Hail")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Torment":
            self.window.ui.label_move.setText("Torment")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flatter":
            self.window.ui.label_move.setText("Flatter")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Will O Wisp":
            self.window.ui.label_move.setText("Will O Wisp")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Memento":
            self.window.ui.label_move.setText("Memento")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Facade":
            self.window.ui.label_move.setText("Facade")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Focus Punch":
            self.window.ui.label_move.setText("Focus Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Smelling Salts":
            self.window.ui.label_move.setText("Smelling Salts")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Follow Me":
            self.window.ui.label_move.setText("Follow Me")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Nature Power":
            self.window.ui.label_move.setText("Nature Power")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Charge":
            self.window.ui.label_move.setText("Charge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Taunt":
            self.window.ui.label_move.setText("Taunt")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Helping Hand":
            self.window.ui.label_move.setText("Helping Hand")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Trick":
            self.window.ui.label_move.setText("Trick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Role Play":
            self.window.ui.label_move.setText("Role Play")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wish":
            self.window.ui.label_move.setText("Wish")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Assist":
            self.window.ui.label_move.setText("Assist")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ingrain":
            self.window.ui.label_move.setText("Ingrain")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Superpower":
            self.window.ui.label_move.setText("Superpower")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magic Coat":
            self.window.ui.label_move.setText("Magic Coat")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Recycle":
            self.window.ui.label_move.setText("Recycle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Revenge":
            self.window.ui.label_move.setText("Revenge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Brick Break":
            self.window.ui.label_move.setText("Brick Break")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Yawn":
            self.window.ui.label_move.setText("Yawn")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Knock Off":
            self.window.ui.label_move.setText("Knock Off")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Endeavor":
            self.window.ui.label_move.setText("Endeavor")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Eruption":
            self.window.ui.label_move.setText("Eruption")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Skill Swap":
            self.window.ui.label_move.setText("Skill Swap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Imprison":
            self.window.ui.label_move.setText("Imprison")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Refresh":
            self.window.ui.label_move.setText("Refresh")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Grudge":
            self.window.ui.label_move.setText("Grudge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Snatch":
            self.window.ui.label_move.setText("Snatch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Secret Power":
            self.window.ui.label_move.setText("Secret Power")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dive":
            self.window.ui.label_move.setText("Dive")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Arm Thrust":
            self.window.ui.label_move.setText("Arm Thrust")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Camouflage":
            self.window.ui.label_move.setText("Camouflage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tail Glow":
            self.window.ui.label_move.setText("Tail Glow")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Luster Purge":
            self.window.ui.label_move.setText("Luster Purge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mist Ball":
            self.window.ui.label_move.setText("Mist Ball")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Feather Dance":
            self.window.ui.label_move.setText("Feather Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Teeter Dance":
            self.window.ui.label_move.setText("Teeter Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Blaze Kick":
            self.window.ui.label_move.setText("Blaze Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mud Sport":
            self.window.ui.label_move.setText("Mud Sport")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ice Ball":
            self.window.ui.label_move.setText("Ice Ball")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Needle Arm":
            self.window.ui.label_move.setText("Needle Arm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Slack Off":
            self.window.ui.label_move.setText("Slack Off")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hyper Voice":
            self.window.ui.label_move.setText("Hyper Voice")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Poison Fang":
            self.window.ui.label_move.setText("Poison Fang")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Crush Claw":
            self.window.ui.label_move.setText("Crush Claw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Blast Burn":
            self.window.ui.label_move.setText("Blast Burn")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hydro Cannon":
            self.window.ui.label_move.setText("Hydro Cannon")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Meteor Mash":
            self.window.ui.label_move.setText("Meteor Mash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Astonish":
            self.window.ui.label_move.setText("Astonish")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Weather Ball":
            self.window.ui.label_move.setText("Weather Ball")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aromatherapy":
            self.window.ui.label_move.setText("Aromatherapy")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fake Tears":
            self.window.ui.label_move.setText("Fake Tears")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Air Cutter":
            self.window.ui.label_move.setText("Air Cutter")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Overheat":
            self.window.ui.label_move.setText("Overheat")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Odor Sleuth":
            self.window.ui.label_move.setText("Odor Sleuth")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rock Tomb":
            self.window.ui.label_move.setText("Rock Tomb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Silver Wind":
            self.window.ui.label_move.setText("Silver Wind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Metal Sound":
            self.window.ui.label_move.setText("Metal Sound")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Grass Whistle":
            self.window.ui.label_move.setText("Grass Whistle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tickle":
            self.window.ui.label_move.setText("Tickle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Cosmic Power":
            self.window.ui.label_move.setText("Cosmic Power")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Water Spout":
            self.window.ui.label_move.setText("Water Spout")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Signal Beam":
            self.window.ui.label_move.setText("Signal Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shadow Punch":
            self.window.ui.label_move.setText("Shadow Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Extrasensory":
            self.window.ui.label_move.setText("Extrasensory")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sky Uppercut":
            self.window.ui.label_move.setText("Sky Uppercut")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sand Tomb":
            self.window.ui.label_move.setText("Sand Tomb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sheer Cold":
            self.window.ui.label_move.setText("Sheer Cold")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Muddy Water":
            self.window.ui.label_move.setText("Muddy Water")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bullet Seed":
            self.window.ui.label_move.setText("Bullet Seed")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aerial Ace":
            self.window.ui.label_move.setText("Aerial Ace")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Icicle Spear":
            self.window.ui.label_move.setText("Icicle Spear")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Iron Defense":
            self.window.ui.label_move.setText("Iron Defense")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Block":
            self.window.ui.label_move.setText("Block")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Howl":
            self.window.ui.label_move.setText("Howl")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Claw":
            self.window.ui.label_move.setText("Dragon Claw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Frenzy Plant":
            self.window.ui.label_move.setText("Frenzy Plant")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bulk Up":
            self.window.ui.label_move.setText("Bulk Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bounce":
            self.window.ui.label_move.setText("Bounce")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mud Shot":
            self.window.ui.label_move.setText("Mud Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Poison Tail":
            self.window.ui.label_move.setText("Poison Tail")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Covet":
            self.window.ui.label_move.setText("Covet")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Volt Tackle":
            self.window.ui.label_move.setText("Volt Tackle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magical Leaf":
            self.window.ui.label_move.setText("Magical Leaf")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Water Sport":
            self.window.ui.label_move.setText("Water Sport")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Calm Mind":
            self.window.ui.label_move.setText("Calm Mind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Leaf Blade":
            self.window.ui.label_move.setText("Leaf Blade")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Dance":
            self.window.ui.label_move.setText("Dragon Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rock Blast":
            self.window.ui.label_move.setText("Rock Blast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shock Wave":
            self.window.ui.label_move.setText("Shock Wave")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Water Pulse":
            self.window.ui.label_move.setText("Water Pulse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Doom Desire":
            self.window.ui.label_move.setText("Doom Desire")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psycho Boost":
            self.window.ui.label_move.setText("Psycho Boost")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Roost":
            self.window.ui.label_move.setText("Roost")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Gravity":
            self.window.ui.label_move.setText("Gravity")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Miracle Eye":
            self.window.ui.label_move.setText("Miracle Eye")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wake Up Slap":
            self.window.ui.label_move.setText("Wake Up Slap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hammer Arm":
            self.window.ui.label_move.setText("Hammer Arm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Gyro Ball":
            self.window.ui.label_move.setText("Gyro Ball")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Healing Wish":
            self.window.ui.label_move.setText("Healing Wish")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Brine":
            self.window.ui.label_move.setText("Brine")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Natural Gift":
            self.window.ui.label_move.setText("Natural Gift")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Feint":
            self.window.ui.label_move.setText("Feint")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pluck":
            self.window.ui.label_move.setText("Pluck")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tailwind":
            self.window.ui.label_move.setText("Tailwind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Acupressure":
            self.window.ui.label_move.setText("Acupressure")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Metal Burst":
            self.window.ui.label_move.setText("Metal Burst")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "U Turn":
            self.window.ui.label_move.setText("U Turn")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Close Combat":
            self.window.ui.label_move.setText("Close Combat")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Payback":
            self.window.ui.label_move.setText("Payback")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Assurance":
            self.window.ui.label_move.setText("Assurance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Embargo":
            self.window.ui.label_move.setText("Embargo")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fling":
            self.window.ui.label_move.setText("Fling")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psycho Shift":
            self.window.ui.label_move.setText("Psycho Shift")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Trump Card":
            self.window.ui.label_move.setText("Trump Card")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Heal Block":
            self.window.ui.label_move.setText("Heal Block")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wring Out":
            self.window.ui.label_move.setText("Wring Out")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Power Trick":
            self.window.ui.label_move.setText("Power Trick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Gastro Acid":
            self.window.ui.label_move.setText("Gastro Acid")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lucky Chant":
            self.window.ui.label_move.setText("Lucky Chant")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Me First":
            self.window.ui.label_move.setText("Me First")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Copycat":
            self.window.ui.label_move.setText("Copycat")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Power Swap":
            self.window.ui.label_move.setText("Power Swap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Guard Swap":
            self.window.ui.label_move.setText("Guard Swap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Punishment":
            self.window.ui.label_move.setText("Punishment")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Last Resort":
            self.window.ui.label_move.setText("Last Resort")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Worry Seed":
            self.window.ui.label_move.setText("Worry Seed")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sucker Punch":
            self.window.ui.label_move.setText("Sucker Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Toxic Spikes":
            self.window.ui.label_move.setText("Toxic Spikes")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Heart Swap":
            self.window.ui.label_move.setText("Heart Swap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aqua Ring":
            self.window.ui.label_move.setText("Aqua Ring")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magnet Rise":
            self.window.ui.label_move.setText("Magnet Rise")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flare Blitz":
            self.window.ui.label_move.setText("Flare Blitz")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Force Palm":
            self.window.ui.label_move.setText("Force Palm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aura Sphere":
            self.window.ui.label_move.setText("Aura Sphere")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rock Polish":
            self.window.ui.label_move.setText("Rock Polish")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Poison Jab":
            self.window.ui.label_move.setText("Poison Jab")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dark Pulse":
            self.window.ui.label_move.setText("Dark Pulse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Night Slash":
            self.window.ui.label_move.setText("Night Slash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aqua Tail":
            self.window.ui.label_move.setText("Aqua Tail")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Seed Bomb":
            self.window.ui.label_move.setText("Seed Bomb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Air Slash":
            self.window.ui.label_move.setText("Air Slash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "X Scissor":
            self.window.ui.label_move.setText("X Scissor")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bug Buzz":
            self.window.ui.label_move.setText("Bug Buzz")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Pulse":
            self.window.ui.label_move.setText("Dragon Pulse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Rush":
            self.window.ui.label_move.setText("Dragon Rush")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Power Gem":
            self.window.ui.label_move.setText("Power Gem")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Drain Punch":
            self.window.ui.label_move.setText("Drain Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Vacuum Wave":
            self.window.ui.label_move.setText("Vacuum Wave")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Focus Blast":
            self.window.ui.label_move.setText("Focus Blast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Energy Ball":
            self.window.ui.label_move.setText("Energy Ball")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Brave Bird":
            self.window.ui.label_move.setText("Brave Bird")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Earth Power":
            self.window.ui.label_move.setText("Earth Power")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Switcheroo":
            self.window.ui.label_move.setText("Switcheroo")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Giga Impact":
            self.window.ui.label_move.setText("Giga Impact")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Nasty Plot":
            self.window.ui.label_move.setText("Nasty Plot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bullet Punch":
            self.window.ui.label_move.setText("Bullet Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Avalanche":
            self.window.ui.label_move.setText("Avalanche")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ice Shard":
            self.window.ui.label_move.setText("Ice Shard")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shadow Claw":
            self.window.ui.label_move.setText("Shadow Claw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thunder Fang":
            self.window.ui.label_move.setText("Thunder Fang")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ice Fang":
            self.window.ui.label_move.setText("Ice Fang")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fire Fang":
            self.window.ui.label_move.setText("Fire Fang")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shadow Sneak":
            self.window.ui.label_move.setText("Shadow Sneak")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mud Bomb":
            self.window.ui.label_move.setText("Mud Bomb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psycho Cut":
            self.window.ui.label_move.setText("Psycho Cut")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Zen Headbutt":
            self.window.ui.label_move.setText("Zen Headbutt")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mirror Shot":
            self.window.ui.label_move.setText("Mirror Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flash Cannon":
            self.window.ui.label_move.setText("Flash Cannon")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rock Climb":
            self.window.ui.label_move.setText("Rock Climb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Defog":
            self.window.ui.label_move.setText("Defog")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Trick Room":
            self.window.ui.label_move.setText("Trick Room")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Draco Meteor":
            self.window.ui.label_move.setText("Draco Meteor")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Discharge":
            self.window.ui.label_move.setText("Discharge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lava Plume":
            self.window.ui.label_move.setText("Lava Plume")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Leaf Storm":
            self.window.ui.label_move.setText("Leaf Storm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Power Whip":
            self.window.ui.label_move.setText("Power Whip")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rock Wrecker":
            self.window.ui.label_move.setText("Rock Wrecker")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Cross Poison":
            self.window.ui.label_move.setText("Cross Poison")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Gunk Shot":
            self.window.ui.label_move.setText("Gunk Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Iron Head":
            self.window.ui.label_move.setText("Iron Head")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magnet Bomb":
            self.window.ui.label_move.setText("Magnet Bomb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stone Edge":
            self.window.ui.label_move.setText("Stone Edge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Captivate":
            self.window.ui.label_move.setText("Captivate")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stealth Rock":
            self.window.ui.label_move.setText("Stealth Rock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Grass Knot":
            self.window.ui.label_move.setText("Grass Knot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Chatter":
            self.window.ui.label_move.setText("Chatter")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Judgment":
            self.window.ui.label_move.setText("Judgment")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bug Bite":
            self.window.ui.label_move.setText("Bug Bite")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Charge Beam":
            self.window.ui.label_move.setText("Charge Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wood Hammer":
            self.window.ui.label_move.setText("Wood Hammer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aqua Jet":
            self.window.ui.label_move.setText("Aqua Jet")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Attack Order":
            self.window.ui.label_move.setText("Attack Order")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Defend Order":
            self.window.ui.label_move.setText("Defend Order")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Heal Order":
            self.window.ui.label_move.setText("Heal Order")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Head Smash":
            self.window.ui.label_move.setText("Head Smash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Double Hit":
            self.window.ui.label_move.setText("Double Hit")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Roar Of Time":
            self.window.ui.label_move.setText("Roar Of Time")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spacial Rend":
            self.window.ui.label_move.setText("Spacial Rend")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lunar Dance":
            self.window.ui.label_move.setText("Lunar Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Crush Grip":
            self.window.ui.label_move.setText("Crush Grip")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magma Storm":
            self.window.ui.label_move.setText("Magma Storm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dark Void":
            self.window.ui.label_move.setText("Dark Void")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Seed Flare":
            self.window.ui.label_move.setText("Seed Flare")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ominous Wind":
            self.window.ui.label_move.setText("Ominous Wind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shadow Force":
            self.window.ui.label_move.setText("Shadow Force")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hone Claws":
            self.window.ui.label_move.setText("Hone Claws")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wide Guard":
            self.window.ui.label_move.setText("Wide Guard")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Guard Split":
            self.window.ui.label_move.setText("Guard Split")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Power Split":
            self.window.ui.label_move.setText("Power Split")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wonder Room":
            self.window.ui.label_move.setText("Wonder Room")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psyshock":
            self.window.ui.label_move.setText("Psyshock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Venoshock":
            self.window.ui.label_move.setText("Venoshock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Autotomize":
            self.window.ui.label_move.setText("Autotomize")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rage Powder":
            self.window.ui.label_move.setText("Rage Powder")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Telekinesis":
            self.window.ui.label_move.setText("Telekinesis")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magic Room":
            self.window.ui.label_move.setText("Magic Room")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Smack Down":
            self.window.ui.label_move.setText("Smack Down")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Storm Throw":
            self.window.ui.label_move.setText("Storm Throw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flame Burst":
            self.window.ui.label_move.setText("Flame Burst")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sludge Wave":
            self.window.ui.label_move.setText("Sludge Wave")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Quiver Dance":
            self.window.ui.label_move.setText("Quiver Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Heavy Slam":
            self.window.ui.label_move.setText("Heavy Slam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Synchronoise":
            self.window.ui.label_move.setText("Synchronoise")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Electro Ball":
            self.window.ui.label_move.setText("Electro Ball")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Soak":
            self.window.ui.label_move.setText("Soak")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flame Charge":
            self.window.ui.label_move.setText("Flame Charge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Coil":
            self.window.ui.label_move.setText("Coil")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Low Sweep":
            self.window.ui.label_move.setText("Low Sweep")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Acid Spray":
            self.window.ui.label_move.setText("Acid Spray")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Foul Play":
            self.window.ui.label_move.setText("Foul Play")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Simple Beam":
            self.window.ui.label_move.setText("Simple Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Entrainment":
            self.window.ui.label_move.setText("Entrainment")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "After You":
            self.window.ui.label_move.setText("After You")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Round":
            self.window.ui.label_move.setText("Round")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Echoed Voice":
            self.window.ui.label_move.setText("Echoed Voice")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Chip Away":
            self.window.ui.label_move.setText("Chip Away")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Clear Smog":
            self.window.ui.label_move.setText("Clear Smog")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stored Power":
            self.window.ui.label_move.setText("Stored Power")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Quick Guard":
            self.window.ui.label_move.setText("Quick Guard")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ally Switch":
            self.window.ui.label_move.setText("Ally Switch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Scald":
            self.window.ui.label_move.setText("Scald")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shell Smash":
            self.window.ui.label_move.setText("Shell Smash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Heal Pulse":
            self.window.ui.label_move.setText("Heal Pulse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hex":
            self.window.ui.label_move.setText("Hex")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sky Drop":
            self.window.ui.label_move.setText("Sky Drop")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shift Gear":
            self.window.ui.label_move.setText("Shift Gear")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Circle Throw":
            self.window.ui.label_move.setText("Circle Throw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Incinerate":
            self.window.ui.label_move.setText("Incinerate")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Quash":
            self.window.ui.label_move.setText("Quash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Acrobatics":
            self.window.ui.label_move.setText("Acrobatics")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Reflect Type":
            self.window.ui.label_move.setText("Reflect Type")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Retaliate":
            self.window.ui.label_move.setText("Retaliate")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Final Gambit":
            self.window.ui.label_move.setText("Final Gambit")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bestow":
            self.window.ui.label_move.setText("Bestow")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Inferno":
            self.window.ui.label_move.setText("Inferno")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Water Pledge":
            self.window.ui.label_move.setText("Water Pledge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fire Pledge":
            self.window.ui.label_move.setText("Fire Pledge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Grass Pledge":
            self.window.ui.label_move.setText("Grass Pledge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Volt Switch":
            self.window.ui.label_move.setText("Volt Switch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Struggle Bug":
            self.window.ui.label_move.setText("Struggle Bug")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bulldoze":
            self.window.ui.label_move.setText("Bulldoze")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Frost Breath":
            self.window.ui.label_move.setText("Frost Breath")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Tail":
            self.window.ui.label_move.setText("Dragon Tail")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Work Up":
            self.window.ui.label_move.setText("Work Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Electroweb":
            self.window.ui.label_move.setText("Electroweb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wild Charge":
            self.window.ui.label_move.setText("Wild Charge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Drill Run":
            self.window.ui.label_move.setText("Drill Run")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dual Chop":
            self.window.ui.label_move.setText("Dual Chop")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Heart Stamp":
            self.window.ui.label_move.setText("Heart Stamp")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Horn Leech":
            self.window.ui.label_move.setText("Horn Leech")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sacred Sword":
            self.window.ui.label_move.setText("Sacred Sword")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Razor Shell":
            self.window.ui.label_move.setText("Razor Shell")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Heat Crash":
            self.window.ui.label_move.setText("Heat Crash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Leaf Tornado":
            self.window.ui.label_move.setText("Leaf Tornado")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Steamroller":
            self.window.ui.label_move.setText("Steamroller")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Cotton Guard":
            self.window.ui.label_move.setText("Cotton Guard")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Night Daze":
            self.window.ui.label_move.setText("Night Daze")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psystrike":
            self.window.ui.label_move.setText("Psystrike")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tail Slap":
            self.window.ui.label_move.setText("Tail Slap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hurricane":
            self.window.ui.label_move.setText("Hurricane")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Head Charge":
            self.window.ui.label_move.setText("Head Charge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Gear Grind":
            self.window.ui.label_move.setText("Gear Grind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Searing Shot":
            self.window.ui.label_move.setText("Searing Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Techno Blast":
            self.window.ui.label_move.setText("Techno Blast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Relic Song":
            self.window.ui.label_move.setText("Relic Song")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Secret Sword":
            self.window.ui.label_move.setText("Secret Sword")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Glaciate":
            self.window.ui.label_move.setText("Glaciate")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bolt Strike":
            self.window.ui.label_move.setText("Bolt Strike")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Blue Flare":
            self.window.ui.label_move.setText("Blue Flare")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fiery Dance":
            self.window.ui.label_move.setText("Fiery Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Freeze Shock":
            self.window.ui.label_move.setText("Freeze Shock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ice Burn":
            self.window.ui.label_move.setText("Ice Burn")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Snarl":
            self.window.ui.label_move.setText("Snarl")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Icicle Crash":
            self.window.ui.label_move.setText("Icicle Crash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "V Create":
            self.window.ui.label_move.setText("V Create")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fusion Flare":
            self.window.ui.label_move.setText("Fusion Flare")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fusion Bolt":
            self.window.ui.label_move.setText("Fusion Bolt")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flying Press":
            self.window.ui.label_move.setText("Flying Press")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mat Block":
            self.window.ui.label_move.setText("Mat Block")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Belch":
            self.window.ui.label_move.setText("Belch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rototiller":
            self.window.ui.label_move.setText("Rototiller")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sticky Web":
            self.window.ui.label_move.setText("Sticky Web")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fell Stinger":
            self.window.ui.label_move.setText("Fell Stinger")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Phantom Force":
            self.window.ui.label_move.setText("Phantom Force")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Trick Or Treat":
            self.window.ui.label_move.setText("Trick Or Treat")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Noble Roar":
            self.window.ui.label_move.setText("Noble Roar")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ion Deluge":
            self.window.ui.label_move.setText("Ion Deluge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Parabolic Charge":
            self.window.ui.label_move.setText("Parabolic Charge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Forests Curse":
            self.window.ui.label_move.setText("Forests Curse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Petal Blizzard":
            self.window.ui.label_move.setText("Petal Blizzard")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Freeze Dry":
            self.window.ui.label_move.setText("Freeze Dry")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Disarming Voice":
            self.window.ui.label_move.setText("Disarming Voice")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Parting Shot":
            self.window.ui.label_move.setText("Parting Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Topsy Turvy":
            self.window.ui.label_move.setText("Topsy Turvy")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Draining Kiss":
            self.window.ui.label_move.setText("Draining Kiss")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Crafty Shield":
            self.window.ui.label_move.setText("Crafty Shield")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flower Shield":
            self.window.ui.label_move.setText("Flower Shield")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Grassy Terrain":
            self.window.ui.label_move.setText("Grassy Terrain")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Misty Terrain":
            self.window.ui.label_move.setText("Misty Terrain")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Electrify":
            self.window.ui.label_move.setText("Electrify")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Play Rough":
            self.window.ui.label_move.setText("Play Rough")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fairy Wind":
            self.window.ui.label_move.setText("Fairy Wind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Moonblast":
            self.window.ui.label_move.setText("Moonblast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Boomburst":
            self.window.ui.label_move.setText("Boomburst")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fairy Lock":
            self.window.ui.label_move.setText("Fairy Lock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Kings Shield":
            self.window.ui.label_move.setText("Kings Shield")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Play Nice":
            self.window.ui.label_move.setText("Play Nice")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Confide":
            self.window.ui.label_move.setText("Confide")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Diamond Storm":
            self.window.ui.label_move.setText("Diamond Storm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Steam Eruption":
            self.window.ui.label_move.setText("Steam Eruption")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hyperspace Hole":
            self.window.ui.label_move.setText("Hyperspace Hole")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Water Shuriken":
            self.window.ui.label_move.setText("Water Shuriken")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mystical Fire":
            self.window.ui.label_move.setText("Mystical Fire")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spiky Shield":
            self.window.ui.label_move.setText("Spiky Shield")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aromatic Mist":
            self.window.ui.label_move.setText("Aromatic Mist")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Eerie Impulse":
            self.window.ui.label_move.setText("Eerie Impulse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Venom Drench":
            self.window.ui.label_move.setText("Venom Drench")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Powder":
            self.window.ui.label_move.setText("Powder")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Geomancy":
            self.window.ui.label_move.setText("Geomancy")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magnetic Flux":
            self.window.ui.label_move.setText("Magnetic Flux")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Happy Hour":
            self.window.ui.label_move.setText("Happy Hour")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Electric Terrain":
            self.window.ui.label_move.setText("Electric Terrain")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dazzling Gleam":
            self.window.ui.label_move.setText("Dazzling Gleam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Celebrate":
            self.window.ui.label_move.setText("Celebrate")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hold Hands":
            self.window.ui.label_move.setText("Hold Hands")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Baby Doll Eyes":
            self.window.ui.label_move.setText("Baby Doll Eyes")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Nuzzle":
            self.window.ui.label_move.setText("Nuzzle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hold Back":
            self.window.ui.label_move.setText("Hold Back")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Infestation":
            self.window.ui.label_move.setText("Infestation")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Power Up Punch":
            self.window.ui.label_move.setText("Power Up Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Oblivion Wing":
            self.window.ui.label_move.setText("Oblivion Wing")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thousand Arrows":
            self.window.ui.label_move.setText("Thousand Arrows")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thousand Waves":
            self.window.ui.label_move.setText("Thousand Waves")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lands Wrath":
            self.window.ui.label_move.setText("Lands Wrath")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Light Of Ruin":
            self.window.ui.label_move.setText("Light Of Ruin")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Origin Pulse":
            self.window.ui.label_move.setText("Origin Pulse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Precipice Blades":
            self.window.ui.label_move.setText("Precipice Blades")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Ascent":
            self.window.ui.label_move.setText("Dragon Ascent")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hyperspace Fury":
            self.window.ui.label_move.setText("Hyperspace Fury")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shore Up":
            self.window.ui.label_move.setText("Shore Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "First Impression":
            self.window.ui.label_move.setText("First Impression")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Baneful Bunker":
            self.window.ui.label_move.setText("Baneful Bunker")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spirit Shackle":
            self.window.ui.label_move.setText("Spirit Shackle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Darkest Lariat":
            self.window.ui.label_move.setText("Darkest Lariat")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sparkling Aria":
            self.window.ui.label_move.setText("Sparkling Aria")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ice Hammer":
            self.window.ui.label_move.setText("Ice Hammer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Floral Healing":
            self.window.ui.label_move.setText("Floral Healing")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "High Horsepower":
            self.window.ui.label_move.setText("High Horsepower")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Strength Sap":
            self.window.ui.label_move.setText("Strength Sap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Solar Blade":
            self.window.ui.label_move.setText("Solar Blade")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Leafage":
            self.window.ui.label_move.setText("Leafage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spotlight":
            self.window.ui.label_move.setText("Spotlight")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Toxic Thread":
            self.window.ui.label_move.setText("Toxic Thread")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Laser Focus":
            self.window.ui.label_move.setText("Laser Focus")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Gear Up":
            self.window.ui.label_move.setText("Gear Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Throat Chop":
            self.window.ui.label_move.setText("Throat Chop")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pollen Puff":
            self.window.ui.label_move.setText("Pollen Puff")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Anchor Shot":
            self.window.ui.label_move.setText("Anchor Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psychic Terrain":
            self.window.ui.label_move.setText("Psychic Terrain")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lunge":
            self.window.ui.label_move.setText("Lunge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fire Lash":
            self.window.ui.label_move.setText("Fire Lash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Power Trip":
            self.window.ui.label_move.setText("Power Trip")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Burn Up":
            self.window.ui.label_move.setText("Burn Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Speed Swap":
            self.window.ui.label_move.setText("Speed Swap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Smart Strike":
            self.window.ui.label_move.setText("Smart Strike")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Purify":
            self.window.ui.label_move.setText("Purify")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Revelation Dance":
            self.window.ui.label_move.setText("Revelation Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Core Enforcer":
            self.window.ui.label_move.setText("Core Enforcer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Trop Kick":
            self.window.ui.label_move.setText("Trop Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Instruct":
            self.window.ui.label_move.setText("Instruct")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Beak Blast":
            self.window.ui.label_move.setText("Beak Blast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Clanging Scales":
            self.window.ui.label_move.setText("Clanging Scales")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Hammer":
            self.window.ui.label_move.setText("Dragon Hammer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Brutal Swing":
            self.window.ui.label_move.setText("Brutal Swing")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aurora Veil":
            self.window.ui.label_move.setText("Aurora Veil")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shell Trap":
            self.window.ui.label_move.setText("Shell Trap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fleur Cannon":
            self.window.ui.label_move.setText("Fleur Cannon")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psychic Fangs":
            self.window.ui.label_move.setText("Psychic Fangs")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stomping Tantrum":
            self.window.ui.label_move.setText("Stomping Tantrum")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shadow Bone":
            self.window.ui.label_move.setText("Shadow Bone")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Accelerock":
            self.window.ui.label_move.setText("Accelerock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Liquidation":
            self.window.ui.label_move.setText("Liquidation")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Prismatic Laser":
            self.window.ui.label_move.setText("Prismatic Laser")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spectral Thief":
            self.window.ui.label_move.setText("Spectral Thief")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sunsteel Strike":
            self.window.ui.label_move.setText("Sunsteel Strike")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Moongeist Beam":
            self.window.ui.label_move.setText("Moongeist Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tearful Look":
            self.window.ui.label_move.setText("Tearful Look")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Zing Zap":
            self.window.ui.label_move.setText("Zing Zap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Natures Madness":
            self.window.ui.label_move.setText("Natures Madness")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Multi Attack":
            self.window.ui.label_move.setText("Multi Attack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mind Blown":
            self.window.ui.label_move.setText("Mind Blown")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Plasma Fists":
            self.window.ui.label_move.setText("Plasma Fists")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Photon Geyser":
            self.window.ui.label_move.setText("Photon Geyser")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Zippy Zap":
            self.window.ui.label_move.setText("Zippy Zap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Splishy Splash":
            self.window.ui.label_move.setText("Splishy Splash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Floaty Fall":
            self.window.ui.label_move.setText("Floaty Fall")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pika Papow":
            self.window.ui.label_move.setText("Pika Papow")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bouncy Bubble":
            self.window.ui.label_move.setText("Bouncy Bubble")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Buzzy Buzz":
            self.window.ui.label_move.setText("Buzzy Buzz")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sizzly Slide":
            self.window.ui.label_move.setText("Sizzly Slide")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Glitzy Glow":
            self.window.ui.label_move.setText("Glitzy Glow")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Baddy Bad":
            self.window.ui.label_move.setText("Baddy Bad")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sappy Seed":
            self.window.ui.label_move.setText("Sappy Seed")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Freezy Frost":
            self.window.ui.label_move.setText("Freezy Frost")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sparkly Swirl":
            self.window.ui.label_move.setText("Sparkly Swirl")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Veevee Volley":
            self.window.ui.label_move.setText("Veevee Volley")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Double Iron Bash":
            self.window.ui.label_move.setText("Double Iron Bash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Breakneck Blitz":
            self.window.ui.label_move.setText("Breakneck Blitz")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "All Out Pummeling":
            self.window.ui.label_move.setText("All Out Pummeling")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Supersonic Skystrike":
            self.window.ui.label_move.setText("Supersonic Skystrike")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Acid Downpour":
            self.window.ui.label_move.setText("Acid Downpour")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tectonic Rage":
            self.window.ui.label_move.setText("Tectonic Rage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Continental Crush":
            self.window.ui.label_move.setText("Continental Crush")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Savage Spin Out":
            self.window.ui.label_move.setText("Savage Spin Out")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Never Ending Nightmare":
            self.window.ui.label_move.setText("Never Ending Nightmare")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Corkscrew Crash":
            self.window.ui.label_move.setText("Corkscrew Crash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Inferno Overdrive":
            self.window.ui.label_move.setText("Inferno Overdrive")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hydro Vortex":
            self.window.ui.label_move.setText("Hydro Vortex")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bloom Doom":
            self.window.ui.label_move.setText("Bloom Doom")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Gigavolt Havoc":
            self.window.ui.label_move.setText("Gigavolt Havoc")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shattered Psyche":
            self.window.ui.label_move.setText("Shattered Psyche")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Subzero Slammer":
            self.window.ui.label_move.setText("Subzero Slammer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Devastating Drake":
            self.window.ui.label_move.setText("Devastating Drake")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Black Hole Eclipse":
            self.window.ui.label_move.setText("Black Hole Eclipse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Twinkle Tackle":
            self.window.ui.label_move.setText("Twinkle Tackle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Catastropika":
            self.window.ui.label_move.setText("Catastropika")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Move 10000000 Volt Thunderbolt":
            self.window.ui.label_move.setText("Move 10000000 Volt Thunderbolt")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stoked Sparksurfer":
            self.window.ui.label_move.setText("Stoked Sparksurfer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Extreme Evoboost":
            self.window.ui.label_move.setText("Extreme Evoboost")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pulverizing Pancake":
            self.window.ui.label_move.setText("Pulverizing Pancake")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Genesis Supernova":
            self.window.ui.label_move.setText("Genesis Supernova")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sinister Arrow Raid":
            self.window.ui.label_move.setText("Sinister Arrow Raid")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Malicious Moonsault":
            self.window.ui.label_move.setText("Malicious Moonsault")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Oceanic Operetta":
            self.window.ui.label_move.setText("Oceanic Operetta")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Splintered Stormshards":
            self.window.ui.label_move.setText("Splintered Stormshards")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lets Snuggle Forever":
            self.window.ui.label_move.setText("Lets Snuggle Forever")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Clangorous Soulblaze":
            self.window.ui.label_move.setText("Clangorous Soulblaze")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Guardian Of Alola":
            self.window.ui.label_move.setText("Guardian Of Alola")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Searing Sunraze Smash":
            self.window.ui.label_move.setText("Searing Sunraze Smash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Menacing Moonraze Maelstrom":
            self.window.ui.label_move.setText("Menacing Moonraze Maelstrom")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Light That Burns The Sky":
            self.window.ui.label_move.setText("Light That Burns The Sky")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Soul Stealing  Star Strike":
            self.window.ui.label_move.setText("Soul Stealing  Star Strike")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dynamax Cannon":
            self.window.ui.label_move.setText("Dynamax Cannon")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Snipe Shot":
            self.window.ui.label_move.setText("Snipe Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Jaw Lock":
            self.window.ui.label_move.setText("Jaw Lock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stuff Cheeks":
            self.window.ui.label_move.setText("Stuff Cheeks")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "No Retreat":
            self.window.ui.label_move.setText("No Retreat")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tar Shot":
            self.window.ui.label_move.setText("Tar Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magic Powder":
            self.window.ui.label_move.setText("Magic Powder")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Darts":
            self.window.ui.label_move.setText("Dragon Darts")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Teatime":
            self.window.ui.label_move.setText("Teatime")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Octolock":
            self.window.ui.label_move.setText("Octolock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bolt Beak":
            self.window.ui.label_move.setText("Bolt Beak")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fishious Rend":
            self.window.ui.label_move.setText("Fishious Rend")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Court Change":
            self.window.ui.label_move.setText("Court Change")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Clangorous Soul":
            self.window.ui.label_move.setText("Clangorous Soul")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Body Press":
            self.window.ui.label_move.setText("Body Press")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Decorate":
            self.window.ui.label_move.setText("Decorate")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Drum Beating":
            self.window.ui.label_move.setText("Drum Beating")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Snap Trap":
            self.window.ui.label_move.setText("Snap Trap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pyro Ball":
            self.window.ui.label_move.setText("Pyro Ball")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Behemoth Blade":
            self.window.ui.label_move.setText("Behemoth Blade")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Behemoth Bash":
            self.window.ui.label_move.setText("Behemoth Bash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aura Wheel":
            self.window.ui.label_move.setText("Aura Wheel")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Breaking Swipe":
            self.window.ui.label_move.setText("Breaking Swipe")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Branch Poke":
            self.window.ui.label_move.setText("Branch Poke")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Overdrive":
            self.window.ui.label_move.setText("Overdrive")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Apple Acid":
            self.window.ui.label_move.setText("Apple Acid")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Grav Apple":
            self.window.ui.label_move.setText("Grav Apple")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spirit Break":
            self.window.ui.label_move.setText("Spirit Break")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Strange Steam":
            self.window.ui.label_move.setText("Strange Steam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Life Dew":
            self.window.ui.label_move.setText("Life Dew")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Obstruct":
            self.window.ui.label_move.setText("Obstruct")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "False Surrender":
            self.window.ui.label_move.setText("False Surrender")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Meteor Assault":
            self.window.ui.label_move.setText("Meteor Assault")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Eternabeam":
            self.window.ui.label_move.setText("Eternabeam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Steel Beam":
            self.window.ui.label_move.setText("Steel Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Expanding Force":
            self.window.ui.label_move.setText("Expanding Force")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Steel Roller":
            self.window.ui.label_move.setText("Steel Roller")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Scale Shot":
            self.window.ui.label_move.setText("Scale Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Meteor Beam":
            self.window.ui.label_move.setText("Meteor Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shell Side Arm":
            self.window.ui.label_move.setText("Shell Side Arm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Misty Explosion":
            self.window.ui.label_move.setText("Misty Explosion")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Grassy Glide":
            self.window.ui.label_move.setText("Grassy Glide")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rising Voltage":
            self.window.ui.label_move.setText("Rising Voltage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Terrain Pulse":
            self.window.ui.label_move.setText("Terrain Pulse")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Skitter Smack":
            self.window.ui.label_move.setText("Skitter Smack")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Burning Jealousy":
            self.window.ui.label_move.setText("Burning Jealousy")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lash Out":
            self.window.ui.label_move.setText("Lash Out")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Poltergeist":
            self.window.ui.label_move.setText("Poltergeist")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Corrosive Gas":
            self.window.ui.label_move.setText("Corrosive Gas")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Coaching":
            self.window.ui.label_move.setText("Coaching")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flip Turn":
            self.window.ui.label_move.setText("Flip Turn")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Triple Axel":
            self.window.ui.label_move.setText("Triple Axel")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dual Wingbeat":
            self.window.ui.label_move.setText("Dual Wingbeat")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Scorching Sands":
            self.window.ui.label_move.setText("Scorching Sands")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Jungle Healing":
            self.window.ui.label_move.setText("Jungle Healing")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wicked Blow":
            self.window.ui.label_move.setText("Wicked Blow")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Surging Strikes":
            self.window.ui.label_move.setText("Surging Strikes")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thunder Cage":
            self.window.ui.label_move.setText("Thunder Cage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Energy":
            self.window.ui.label_move.setText("Dragon Energy")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Freezing Glare":
            self.window.ui.label_move.setText("Freezing Glare")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fiery Wrath":
            self.window.ui.label_move.setText("Fiery Wrath")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thunderous Kick":
            self.window.ui.label_move.setText("Thunderous Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Glacial Lance":
            self.window.ui.label_move.setText("Glacial Lance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Astral Barrage":
            self.window.ui.label_move.setText("Astral Barrage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Eerie Spell":
            self.window.ui.label_move.setText("Eerie Spell")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dire Claw":
            self.window.ui.label_move.setText("Dire Claw")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psyshield Bash":
            self.window.ui.label_move.setText("Psyshield Bash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Power Shift":
            self.window.ui.label_move.setText("Power Shift")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Stone Axe":
            self.window.ui.label_move.setText("Stone Axe")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Springtide Storm":
            self.window.ui.label_move.setText("Springtide Storm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mystical Power":
            self.window.ui.label_move.setText("Mystical Power")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Raging Fury":
            self.window.ui.label_move.setText("Raging Fury")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wave Crash":
            self.window.ui.label_move.setText("Wave Crash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Chloroblast":
            self.window.ui.label_move.setText("Chloroblast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mountain Gale":
            self.window.ui.label_move.setText("Mountain Gale")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Victory Dance":
            self.window.ui.label_move.setText("Victory Dance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Headlong Rush":
            self.window.ui.label_move.setText("Headlong Rush")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Barb Barrage":
            self.window.ui.label_move.setText("Barb Barrage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Esper Wing":
            self.window.ui.label_move.setText("Esper Wing")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bitter Malice":
            self.window.ui.label_move.setText("Bitter Malice")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shelter":
            self.window.ui.label_move.setText("Shelter")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Triple Arrows":
            self.window.ui.label_move.setText("Triple Arrows")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Infernal Parade":
            self.window.ui.label_move.setText("Infernal Parade")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ceaseless Edge":
            self.window.ui.label_move.setText("Ceaseless Edge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bleakwind Storm":
            self.window.ui.label_move.setText("Bleakwind Storm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wildbolt Storm":
            self.window.ui.label_move.setText("Wildbolt Storm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Sandsear Storm":
            self.window.ui.label_move.setText("Sandsear Storm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lunar Blessing":
            self.window.ui.label_move.setText("Lunar Blessing")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Take Heart":
            self.window.ui.label_move.setText("Take Heart")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Guard":
            self.window.ui.label_move.setText("Max Guard")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Strike":
            self.window.ui.label_move.setText("Max Strike")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Knuckle":
            self.window.ui.label_move.setText("Max Knuckle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Airstream":
            self.window.ui.label_move.setText("Max Airstream")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Ooze":
            self.window.ui.label_move.setText("Max Ooze")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Quake":
            self.window.ui.label_move.setText("Max Quake")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Rockfall":
            self.window.ui.label_move.setText("Max Rockfall")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Flutterby":
            self.window.ui.label_move.setText("Max Flutterby")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Phantasm":
            self.window.ui.label_move.setText("Max Phantasm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Steelspike":
            self.window.ui.label_move.setText("Max Steelspike")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Flare":
            self.window.ui.label_move.setText("Max Flare")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Geyser":
            self.window.ui.label_move.setText("Max Geyser")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Overgrowth":
            self.window.ui.label_move.setText("Max Overgrowth")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Lightning":
            self.window.ui.label_move.setText("Max Lightning")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Mindstorm":
            self.window.ui.label_move.setText("Max Mindstorm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Hailstorm":
            self.window.ui.label_move.setText("Max Hailstorm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Wyrmwind":
            self.window.ui.label_move.setText("Max Wyrmwind")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Darkness":
            self.window.ui.label_move.setText("Max Darkness")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Max Starfall":
            self.window.ui.label_move.setText("Max Starfall")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Vine Lash":
            self.window.ui.label_move.setText("G Max Vine Lash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Wildfire":
            self.window.ui.label_move.setText("G Max Wildfire")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Cannonade":
            self.window.ui.label_move.setText("G Max Cannonade")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Befuddle":
            self.window.ui.label_move.setText("G Max Befuddle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Volt Crash":
            self.window.ui.label_move.setText("G Max Volt Crash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Gold Rush":
            self.window.ui.label_move.setText("G Max Gold Rush")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Chi Strike":
            self.window.ui.label_move.setText("G Max Chi Strike")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Terror":
            self.window.ui.label_move.setText("G Max Terror")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Foam Burst":
            self.window.ui.label_move.setText("G Max Foam Burst")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Resonance":
            self.window.ui.label_move.setText("G Max Resonance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Cuddle":
            self.window.ui.label_move.setText("G Max Cuddle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Replenish":
            self.window.ui.label_move.setText("G Max Replenish")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Malodor":
            self.window.ui.label_move.setText("G Max Malodor")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Meltdown":
            self.window.ui.label_move.setText("G Max Meltdown")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Drum Solo":
            self.window.ui.label_move.setText("G Max Drum Solo")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Fireball":
            self.window.ui.label_move.setText("G Max Fireball")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Hydrosnipe":
            self.window.ui.label_move.setText("G Max Hydrosnipe")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Wind Rage":
            self.window.ui.label_move.setText("G Max Wind Rage")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Gravitas":
            self.window.ui.label_move.setText("G Max Gravitas")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Stonesurge":
            self.window.ui.label_move.setText("G Max Stonesurge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Volcalith":
            self.window.ui.label_move.setText("G Max Volcalith")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Tartness":
            self.window.ui.label_move.setText("G Max Tartness")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Sweetness":
            self.window.ui.label_move.setText("G Max Sweetness")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Sandblast":
            self.window.ui.label_move.setText("G Max Sandblast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Stun Shock":
            self.window.ui.label_move.setText("G Max Stun Shock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Centiferno":
            self.window.ui.label_move.setText("G Max Centiferno")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Smite":
            self.window.ui.label_move.setText("G Max Smite")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Snooze":
            self.window.ui.label_move.setText("G Max Snooze")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Finale":
            self.window.ui.label_move.setText("G Max Finale")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Steelsurge":
            self.window.ui.label_move.setText("G Max Steelsurge")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Depletion":
            self.window.ui.label_move.setText("G Max Depletion")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max One Blow":
            self.window.ui.label_move.setText("G Max One Blow")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "G Max Rapid Flow":
            self.window.ui.label_move.setText("G Max Rapid Flow")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tera Blast":
            self.window.ui.label_move.setText("Tera Blast")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Silk Trap":
            self.window.ui.label_move.setText("Silk Trap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Axe Kick":
            self.window.ui.label_move.setText("Axe Kick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Last Respects":
            self.window.ui.label_move.setText("Last Respects")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Lumina Crash":
            self.window.ui.label_move.setText("Lumina Crash")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Order Up":
            self.window.ui.label_move.setText("Order Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Jet Punch":
            self.window.ui.label_move.setText("Jet Punch")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spicy Extract":
            self.window.ui.label_move.setText("Spicy Extract")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Spin Out":
            self.window.ui.label_move.setText("Spin Out")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Population Bomb":
            self.window.ui.label_move.setText("Population Bomb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ice Spinner":
            self.window.ui.label_move.setText("Ice Spinner")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Glaive Rush":
            self.window.ui.label_move.setText("Glaive Rush")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Revival Blessing":
            self.window.ui.label_move.setText("Revival Blessing")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Salt Cure":
            self.window.ui.label_move.setText("Salt Cure")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Triple Dive":
            self.window.ui.label_move.setText("Triple Dive")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mortal Spin":
            self.window.ui.label_move.setText("Mortal Spin")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Doodle":
            self.window.ui.label_move.setText("Doodle")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fillet Away":
            self.window.ui.label_move.setText("Fillet Away")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Kowtow Cleave":
            self.window.ui.label_move.setText("Kowtow Cleave")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Flower Trick":
            self.window.ui.label_move.setText("Flower Trick")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Torch Song":
            self.window.ui.label_move.setText("Torch Song")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aqua Step":
            self.window.ui.label_move.setText("Aqua Step")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Raging Bull":
            self.window.ui.label_move.setText("Raging Bull")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Make It Rain":
            self.window.ui.label_move.setText("Make It Rain")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ruination":
            self.window.ui.label_move.setText("Ruination")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Collision Course":
            self.window.ui.label_move.setText("Collision Course")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Electro Drift":
            self.window.ui.label_move.setText("Electro Drift")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Shed Tail":
            self.window.ui.label_move.setText("Shed Tail")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Chilly Reception":
            self.window.ui.label_move.setText("Chilly Reception")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tidy Up":
            self.window.ui.label_move.setText("Tidy Up")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Snowscape":
            self.window.ui.label_move.setText("Snowscape")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Pounce":
            self.window.ui.label_move.setText("Pounce")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Trailblaze":
            self.window.ui.label_move.setText("Trailblaze")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Chilling Water":
            self.window.ui.label_move.setText("Chilling Water")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hyper Drill":
            self.window.ui.label_move.setText("Hyper Drill")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Twin Beam":
            self.window.ui.label_move.setText("Twin Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Rage Fist":
            self.window.ui.label_move.setText("Rage Fist")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Armor Cannon":
            self.window.ui.label_move.setText("Armor Cannon")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Bitter Blade":
            self.window.ui.label_move.setText("Bitter Blade")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Double Shock":
            self.window.ui.label_move.setText("Double Shock")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Gigaton Hammer":
            self.window.ui.label_move.setText("Gigaton Hammer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Comeuppance":
            self.window.ui.label_move.setText("Comeuppance")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Aqua Cutter":
            self.window.ui.label_move.setText("Aqua Cutter")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Blazing Torque":
            self.window.ui.label_move.setText("Blazing Torque")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Wicked Torque":
            self.window.ui.label_move.setText("Wicked Torque")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Noxious Torque":
            self.window.ui.label_move.setText("Noxious Torque")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Combat Torque":
            self.window.ui.label_move.setText("Combat Torque")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Magical Torque":
            self.window.ui.label_move.setText("Magical Torque")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psyblade":
            self.window.ui.label_move.setText("Psyblade")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hydro Steam":
            self.window.ui.label_move.setText("Hydro Steam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Blood Moon":
            self.window.ui.label_move.setText("Blood Moon")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Matcha Gotcha":
            self.window.ui.label_move.setText("Matcha Gotcha")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Syrup Bomb":
            self.window.ui.label_move.setText("Syrup Bomb")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Ivy Cudgel":
            self.window.ui.label_move.setText("Ivy Cudgel")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Electro Shot":
            self.window.ui.label_move.setText("Electro Shot")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tera Starstorm":
            self.window.ui.label_move.setText("Tera Starstorm")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Fickle Beam":
            self.window.ui.label_move.setText("Fickle Beam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Burning Bulwark":
            self.window.ui.label_move.setText("Burning Bulwark")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Thunderclap":
            self.window.ui.label_move.setText("Thunderclap")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Mighty Cleave":
            self.window.ui.label_move.setText("Mighty Cleave")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Tachyon Cutter":
            self.window.ui.label_move.setText("Tachyon Cutter")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Hard Press":
            self.window.ui.label_move.setText("Hard Press")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Dragon Cheer":
            self.window.ui.label_move.setText("Dragon Cheer")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Alluring Voice":
            self.window.ui.label_move.setText("Alluring Voice")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Temper Flare":
            self.window.ui.label_move.setText("Temper Flare")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Supercell Slam":
            self.window.ui.label_move.setText("Supercell Slam")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Psychic Noise":
            self.window.ui.label_move.setText("Psychic Noise")
            self.window.show()
        elif self.ui.comboBox_Move.currentText()  == "Upper Hand":
            self.window.ui.label_move.setText("Upper Hand")
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Malignant Chain":
            self.window.ui.label_move.setText("Malignant Chain")
            self.window.show()
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Error")
            dialog.setText(f"{self.ui.comboBox_Move.currentText()} is not a valid Move")
            dialog.exec()

    def open_ability_Window(self):
        self.window = AbilityWindow()
        self.window.setWindowTitle(self.ui.comboBox_Ability.currentText())
        if self.ui.comboBox_Ability.currentText() == "Stench":
            self.window.ui.label_ability.setText("Stench")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Drizzle":
            self.window.ui.label_ability.setText("Drizzle")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Speed Boost":
            self.window.ui.label_ability.setText("Speed Boost")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Battle Armor":
            self.window.ui.label_ability.setText("Battle Armor")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sturdy":
            self.window.ui.label_ability.setText("Sturdy")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Damp":
            self.window.ui.label_ability.setText("Damp")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Limber":
            self.window.ui.label_ability.setText("Limber")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sand Veil":
            self.window.ui.label_ability.setText("Sand Veil")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Static":
            self.window.ui.label_ability.setText("Static")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Volt Absorb":
            self.window.ui.label_ability.setText("Volt Absorb")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Water Absorb":
            self.window.ui.label_ability.setText("Water Absorb")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Oblivious":
            self.window.ui.label_ability.setText("Oblivious")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Cloud Nine":
            self.window.ui.label_ability.setText("Cloud Nine")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Compound Eyes":
            self.window.ui.label_ability.setText("Compound Eyes")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Insomnia":
            self.window.ui.label_ability.setText("Insomnia")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Color Change":
            self.window.ui.label_ability.setText("Color Change")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Immunity":
            self.window.ui.label_ability.setText("Immunity")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Flash Fire":
            self.window.ui.label_ability.setText("Flash Fire")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Shield Dust":
            self.window.ui.label_ability.setText("Shield Dust")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Own Tempo":
            self.window.ui.label_ability.setText("Own Tempo")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Suction Cups":
            self.window.ui.label_ability.setText("Suction Cups")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Intimidate":
            self.window.ui.label_ability.setText("Intimidate")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Shadow Tag":
            self.window.ui.label_ability.setText("Shadow Tag")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Rough Skin":
            self.window.ui.label_ability.setText("Rough Skin")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Wonder Guard":
            self.window.ui.label_ability.setText("Wonder Guard")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Levitate":
            self.window.ui.label_ability.setText("Levitate")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Effect Spore":
            self.window.ui.label_ability.setText("Effect Spore")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Synchronize":
            self.window.ui.label_ability.setText("Synchronize")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Clear Body":
            self.window.ui.label_ability.setText("Clear Body")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Natural Cure":
            self.window.ui.label_ability.setText("Natural Cure")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Lightning Rod":
            self.window.ui.label_ability.setText("Lightning Rod")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Serene Grace":
            self.window.ui.label_ability.setText("Serene Grace")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Swift Swim":
            self.window.ui.label_ability.setText("Swift Swim")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Chlorophyll":
            self.window.ui.label_ability.setText("Chlorophyll")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Illuminate":
            self.window.ui.label_ability.setText("Illuminate")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Trace":
            self.window.ui.label_ability.setText("Trace")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Huge Power":
            self.window.ui.label_ability.setText("Huge Power")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Poison Point":
            self.window.ui.label_ability.setText("Poison Point")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Inner Focus":
            self.window.ui.label_ability.setText("Inner Focus")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Magma Armor":
            self.window.ui.label_ability.setText("Magma Armor")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Water Veil":
            self.window.ui.label_ability.setText("Water Veil")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Magnet Pull":
            self.window.ui.label_ability.setText("Magnet Pull")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Soundproof":
            self.window.ui.label_ability.setText("Soundproof")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Rain Dish":
            self.window.ui.label_ability.setText("Rain Dish")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sand Stream":
            self.window.ui.label_ability.setText("Sand Stream")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Pressure":
            self.window.ui.label_ability.setText("Pressure")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Thick Fat":
            self.window.ui.label_ability.setText("Thick Fat")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Early Bird":
            self.window.ui.label_ability.setText("Early Bird")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Flame Body":
            self.window.ui.label_ability.setText("Flame Body")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Run Away":
            self.window.ui.label_ability.setText("Run Away")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Keen Eye":
            self.window.ui.label_ability.setText("Keen Eye")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Hyper Cutter":
            self.window.ui.label_ability.setText("Hyper Cutter")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Pickup":
            self.window.ui.label_ability.setText("Pickup")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Truant":
            self.window.ui.label_ability.setText("Truant")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Hustle":
            self.window.ui.label_ability.setText("Hustle")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Cute Charm":
            self.window.ui.label_ability.setText("Cute Charm")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Plus":
            self.window.ui.label_ability.setText("Plus")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Minus":
            self.window.ui.label_ability.setText("Minus")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Forecast":
            self.window.ui.label_ability.setText("Forecast")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sticky Hold":
            self.window.ui.label_ability.setText("Sticky Hold")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Shed Skin":
            self.window.ui.label_ability.setText("Shed Skin")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Guts":
            self.window.ui.label_ability.setText("Guts")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Marvel Scale":
            self.window.ui.label_ability.setText("Marvel Scale")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Liquid Ooze":
            self.window.ui.label_ability.setText("Liquid Ooze")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Overgrow":
            self.window.ui.label_ability.setText("Overgrow")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Blaze":
            self.window.ui.label_ability.setText("Blaze")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Torrent":
            self.window.ui.label_ability.setText("Torrent")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Swarm":
            self.window.ui.label_ability.setText("Swarm")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Rock Head":
            self.window.ui.label_ability.setText("Rock Head")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Drought":
            self.window.ui.label_ability.setText("Drought")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Arena Trap":
            self.window.ui.label_ability.setText("Arena Trap")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Vital Spirit":
            self.window.ui.label_ability.setText("Vital Spirit")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "White Smoke":
            self.window.ui.label_ability.setText("White Smoke")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Pure Power":
            self.window.ui.label_ability.setText("Pure Power")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Shell Armor":
            self.window.ui.label_ability.setText("Shell Armor")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Air Lock":
            self.window.ui.label_ability.setText("Air Lock")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Tangled Feet":
            self.window.ui.label_ability.setText("Tangled Feet")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Motor Drive":
            self.window.ui.label_ability.setText("Motor Drive")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Rivalry":
            self.window.ui.label_ability.setText("Rivalry")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Steadfast":
            self.window.ui.label_ability.setText("Steadfast")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Snow Cloak":
            self.window.ui.label_ability.setText("Snow Cloak")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Gluttony":
            self.window.ui.label_ability.setText("Gluttony")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Anger Point":
            self.window.ui.label_ability.setText("Anger Point")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Unburden":
            self.window.ui.label_ability.setText("Unburden")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Heatproof":
            self.window.ui.label_ability.setText("Heatproof")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Simple":
            self.window.ui.label_ability.setText("Simple")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Dry Skin":
            self.window.ui.label_ability.setText("Dry Skin")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Download":
            self.window.ui.label_ability.setText("Download")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Iron Fist":
            self.window.ui.label_ability.setText("Iron Fist")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Poison Heal":
            self.window.ui.label_ability.setText("Poison Heal")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Adaptability":
            self.window.ui.label_ability.setText("Adaptability")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Skill Link":
            self.window.ui.label_ability.setText("Skill Link")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Hydration":
            self.window.ui.label_ability.setText("Hydration")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Solar Power":
            self.window.ui.label_ability.setText("Solar Power")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Quick Feet":
            self.window.ui.label_ability.setText("Quick Feet")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Normalize":
            self.window.ui.label_ability.setText("Normalize")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sniper":
            self.window.ui.label_ability.setText("Sniper")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Magic Guard":
            self.window.ui.label_ability.setText("Magic Guard")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "No Guard":
            self.window.ui.label_ability.setText("No Guard")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Stall":
            self.window.ui.label_ability.setText("Stall")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Technician":
            self.window.ui.label_ability.setText("Technician")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Leaf Guard":
            self.window.ui.label_ability.setText("Leaf Guard")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Klutz":
            self.window.ui.label_ability.setText("Klutz")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Mold Breaker":
            self.window.ui.label_ability.setText("Mold Breaker")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Super Luck":
            self.window.ui.label_ability.setText("Super Luck")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Aftermath":
            self.window.ui.label_ability.setText("Aftermath")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Anticipation":
            self.window.ui.label_ability.setText("Anticipation")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Forewarn":
            self.window.ui.label_ability.setText("Forewarn")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Unaware":
            self.window.ui.label_ability.setText("Unaware")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Tinted Lens":
            self.window.ui.label_ability.setText("Tinted Lens")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Filter":
            self.window.ui.label_ability.setText("Filter")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Slow Start":
            self.window.ui.label_ability.setText("Slow Start")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Scrappy":
            self.window.ui.label_ability.setText("Scrappy")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Storm Drain":
            self.window.ui.label_ability.setText("Storm Drain")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Ice Body":
            self.window.ui.label_ability.setText("Ice Body")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Solid Rock":
            self.window.ui.label_ability.setText("Solid Rock")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Snow Warning":
            self.window.ui.label_ability.setText("Snow Warning")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Honey Gather":
            self.window.ui.label_ability.setText("Honey Gather")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Frisk":
            self.window.ui.label_ability.setText("Frisk")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Reckless":
            self.window.ui.label_ability.setText("Reckless")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Multitype":
            self.window.ui.label_ability.setText("Multitype")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Flower Gift":
            self.window.ui.label_ability.setText("Flower Gift")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Bad Dreams":
            self.window.ui.label_ability.setText("Bad Dreams")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Pickpocket":
            self.window.ui.label_ability.setText("Pickpocket")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sheer Force":
            self.window.ui.label_ability.setText("Sheer Force")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Contrary":
            self.window.ui.label_ability.setText("Contrary")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Unnerve":
            self.window.ui.label_ability.setText("Unnerve")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Defiant":
            self.window.ui.label_ability.setText("Defiant")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Defeatist":
            self.window.ui.label_ability.setText("Defeatist")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Cursed Body":
            self.window.ui.label_ability.setText("Cursed Body")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Healer":
            self.window.ui.label_ability.setText("Healer")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Friend Guard":
            self.window.ui.label_ability.setText("Friend Guard")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Weak Armor":
            self.window.ui.label_ability.setText("Weak Armor")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Heavy Metal":
            self.window.ui.label_ability.setText("Heavy Metal")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Light Metal":
            self.window.ui.label_ability.setText("Light Metal")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Multiscale":
            self.window.ui.label_ability.setText("Multiscale")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Toxic Boost":
            self.window.ui.label_ability.setText("Toxic Boost")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Flare Boost":
            self.window.ui.label_ability.setText("Flare Boost")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Harvest":
            self.window.ui.label_ability.setText("Harvest")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Telepathy":
            self.window.ui.label_ability.setText("Telepathy")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Moody":
            self.window.ui.label_ability.setText("Moody")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Overcoat":
            self.window.ui.label_ability.setText("Overcoat")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Poison Touch":
            self.window.ui.label_ability.setText("Poison Touch")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Regenerator":
            self.window.ui.label_ability.setText("Regenerator")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Big Pecks":
            self.window.ui.label_ability.setText("Big Pecks")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sand Rush":
            self.window.ui.label_ability.setText("Sand Rush")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Wonder Skin":
            self.window.ui.label_ability.setText("Wonder Skin")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Analytic":
            self.window.ui.label_ability.setText("Analytic")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Illusion":
            self.window.ui.label_ability.setText("Illusion")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Imposter":
            self.window.ui.label_ability.setText("Imposter")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Infiltrator":
            self.window.ui.label_ability.setText("Infiltrator")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Mummy":
            self.window.ui.label_ability.setText("Mummy")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Moxie":
            self.window.ui.label_ability.setText("Moxie")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Justified":
            self.window.ui.label_ability.setText("Justified")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Rattled":
            self.window.ui.label_ability.setText("Rattled")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Magic Bounce":
            self.window.ui.label_ability.setText("Magic Bounce")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sap Sipper":
            self.window.ui.label_ability.setText("Sap Sipper")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Prankster":
            self.window.ui.label_ability.setText("Prankster")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sand Force":
            self.window.ui.label_ability.setText("Sand Force")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Iron Barbs":
            self.window.ui.label_ability.setText("Iron Barbs")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Zen Mode":
            self.window.ui.label_ability.setText("Zen Mode")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Victory Star":
            self.window.ui.label_ability.setText("Victory Star")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Turboblaze":
            self.window.ui.label_ability.setText("Turboblaze")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Teravolt":
            self.window.ui.label_ability.setText("Teravolt")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Aroma Veil":
            self.window.ui.label_ability.setText("Aroma Veil")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Flower Veil":
            self.window.ui.label_ability.setText("Flower Veil")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Cheek Pouch":
            self.window.ui.label_ability.setText("Cheek Pouch")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Protean":
            self.window.ui.label_ability.setText("Protean")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Fur Coat":
            self.window.ui.label_ability.setText("Fur Coat")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Magician":
            self.window.ui.label_ability.setText("Magician")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Bulletproof":
            self.window.ui.label_ability.setText("Bulletproof")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Competitive":
            self.window.ui.label_ability.setText("Competitive")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Strong Jaw":
            self.window.ui.label_ability.setText("Strong Jaw")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Refrigerate":
            self.window.ui.label_ability.setText("Refrigerate")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sweet Veil":
            self.window.ui.label_ability.setText("Sweet Veil")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Stance Change":
            self.window.ui.label_ability.setText("Stance Change")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Gale Wings":
            self.window.ui.label_ability.setText("Gale Wings")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Mega Launcher":
            self.window.ui.label_ability.setText("Mega Launcher")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Grass Pelt":
            self.window.ui.label_ability.setText("Grass Pelt")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Symbiosis":
            self.window.ui.label_ability.setText("Symbiosis")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Tough Claws":
            self.window.ui.label_ability.setText("Tough Claws")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Pixilate":
            self.window.ui.label_ability.setText("Pixilate")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Gooey":
            self.window.ui.label_ability.setText("Gooey")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Aerilate":
            self.window.ui.label_ability.setText("Aerilate")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Parental Bond":
            self.window.ui.label_ability.setText("Parental Bond")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Dark Aura":
            self.window.ui.label_ability.setText("Dark Aura")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Fairy Aura":
            self.window.ui.label_ability.setText("Fairy Aura")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Aura Break":
            self.window.ui.label_ability.setText("Aura Break")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Primordial Sea":
            self.window.ui.label_ability.setText("Primordial Sea")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Desolate Land":
            self.window.ui.label_ability.setText("Desolate Land")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Delta Stream":
            self.window.ui.label_ability.setText("Delta Stream")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Stamina":
            self.window.ui.label_ability.setText("Stamina")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Wimp Out":
            self.window.ui.label_ability.setText("Wimp Out")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Emergency Exit":
            self.window.ui.label_ability.setText("Emergency Exit")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Water Compaction":
            self.window.ui.label_ability.setText("Water Compaction")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Merciless":
            self.window.ui.label_ability.setText("Merciless")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Shields Down":
            self.window.ui.label_ability.setText("Shields Down")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Stakeout":
            self.window.ui.label_ability.setText("Stakeout")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Water Bubble":
            self.window.ui.label_ability.setText("Water Bubble")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Steelworker":
            self.window.ui.label_ability.setText("Steelworker")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Berserk":
            self.window.ui.label_ability.setText("Berserk")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Slush Rush":
            self.window.ui.label_ability.setText("Slush Rush")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Long Reach":
            self.window.ui.label_ability.setText("Long Reach")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Liquid Voice":
            self.window.ui.label_ability.setText("Liquid Voice")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Triage":
            self.window.ui.label_ability.setText("Triage")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Galvanize":
            self.window.ui.label_ability.setText("Galvanize")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Surge Surfer":
            self.window.ui.label_ability.setText("Surge Surfer")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Schooling":
            self.window.ui.label_ability.setText("Schooling")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Disguise":
            self.window.ui.label_ability.setText("Disguise")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Battle Bond":
            self.window.ui.label_ability.setText("Battle Bond")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Power Construct":
            self.window.ui.label_ability.setText("Power Construct")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Corrosion":
            self.window.ui.label_ability.setText("Corrosion")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Comatose":
            self.window.ui.label_ability.setText("Comatose")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Queenly Majesty":
            self.window.ui.label_ability.setText("Queenly Majesty")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Innards Out":
            self.window.ui.label_ability.setText("Innards Out")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Dancer":
            self.window.ui.label_ability.setText("Dancer")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Battery":
            self.window.ui.label_ability.setText("Battery")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Fluffy":
            self.window.ui.label_ability.setText("Fluffy")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Dazzling":
            self.window.ui.label_ability.setText("Dazzling")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Soul Heart":
            self.window.ui.label_ability.setText("Soul Heart")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Tangling Hair":
            self.window.ui.label_ability.setText("Tangling Hair")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Receiver":
            self.window.ui.label_ability.setText("Receiver")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Power Of Alchemy":
            self.window.ui.label_ability.setText("Power Of Alchemy")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Beast Boost":
            self.window.ui.label_ability.setText("Beast Boost")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Rks System":
            self.window.ui.label_ability.setText("Rks System")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Electric Surge":
            self.window.ui.label_ability.setText("Electric Surge")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Psychic Surge":
            self.window.ui.label_ability.setText("Psychic Surge")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Misty Surge":
            self.window.ui.label_ability.setText("Misty Surge")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Grassy Surge":
            self.window.ui.label_ability.setText("Grassy Surge")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Full Metal Body":
            self.window.ui.label_ability.setText("Full Metal Body")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Shadow Shield":
            self.window.ui.label_ability.setText("Shadow Shield")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Prism Armor":
            self.window.ui.label_ability.setText("Prism Armor")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Neuroforce":
            self.window.ui.label_ability.setText("Neuroforce")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Intrepid Sword":
            self.window.ui.label_ability.setText("Intrepid Sword")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Dauntless Shield":
            self.window.ui.label_ability.setText("Dauntless Shield")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Libero":
            self.window.ui.label_ability.setText("Libero")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Ball Fetch":
            self.window.ui.label_ability.setText("Ball Fetch")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Cotton Down":
            self.window.ui.label_ability.setText("Cotton Down")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Propeller Tail":
            self.window.ui.label_ability.setText("Propeller Tail")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Mirror Armor":
            self.window.ui.label_ability.setText("Mirror Armor")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Gulp Missile":
            self.window.ui.label_ability.setText("Gulp Missile")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Stalwart":
            self.window.ui.label_ability.setText("Stalwart")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Steam Engine":
            self.window.ui.label_ability.setText("Steam Engine")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Punk Rock":
            self.window.ui.label_ability.setText("Punk Rock")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sand Spit":
            self.window.ui.label_ability.setText("Sand Spit")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Ice Scales":
            self.window.ui.label_ability.setText("Ice Scales")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Ripen":
            self.window.ui.label_ability.setText("Ripen")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Ice Face":
            self.window.ui.label_ability.setText("Ice Face")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Power Spot":
            self.window.ui.label_ability.setText("Power Spot")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Mimicry":
            self.window.ui.label_ability.setText("Mimicry")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Screen Cleaner":
            self.window.ui.label_ability.setText("Screen Cleaner")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Steely Spirit":
            self.window.ui.label_ability.setText("Steely Spirit")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Perish Body":
            self.window.ui.label_ability.setText("Perish Body")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Wandering Spirit":
            self.window.ui.label_ability.setText("Wandering Spirit")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Gorilla Tactics":
            self.window.ui.label_ability.setText("Gorilla Tactics")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Neutralizing Gas":
            self.window.ui.label_ability.setText("Neutralizing Gas")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Pastel Veil":
            self.window.ui.label_ability.setText("Pastel Veil")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Hunger Switch":
            self.window.ui.label_ability.setText("Hunger Switch")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Quick Draw":
            self.window.ui.label_ability.setText("Quick Draw")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Unseen Fist":
            self.window.ui.label_ability.setText("Unseen Fist")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Curious Medicine":
            self.window.ui.label_ability.setText("Curious Medicine")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Transistor":
            self.window.ui.label_ability.setText("Transistor")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Dragons Maw":
            self.window.ui.label_ability.setText("Dragons Maw")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Chilling Neigh":
            self.window.ui.label_ability.setText("Chilling Neigh")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Grim Neigh":
            self.window.ui.label_ability.setText("Grim Neigh")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "As One Ice Rider":
            self.window.ui.label_ability.setText("As One Ice Rider")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "As One Shadow Rider":
            self.window.ui.label_ability.setText("As One Shadow Rider")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Lingering Aroma":
            self.window.ui.label_ability.setText("Lingering Aroma")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Seed Sower":
            self.window.ui.label_ability.setText("Seed Sower")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Thermal Exchange":
            self.window.ui.label_ability.setText("Thermal Exchange")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Anger Shell":
            self.window.ui.label_ability.setText("Anger Shell")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Purifying Salt":
            self.window.ui.label_ability.setText("Purifying Salt")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Well Baked Body":
            self.window.ui.label_ability.setText("Well Baked Body")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Wind Rider":
            self.window.ui.label_ability.setText("Wind Rider")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Guard Dog":
            self.window.ui.label_ability.setText("Guard Dog")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Rocky Payload":
            self.window.ui.label_ability.setText("Rocky Payload")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Wind Power":
            self.window.ui.label_ability.setText("Wind Power")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Zero To Hero":
            self.window.ui.label_ability.setText("Zero To Hero")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Commander":
            self.window.ui.label_ability.setText("Commander")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Electromorphosis":
            self.window.ui.label_ability.setText("Electromorphosis")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Protosynthesis":
            self.window.ui.label_ability.setText("Protosynthesis")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Quark Drive":
            self.window.ui.label_ability.setText("Quark Drive")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Good As Gold":
            self.window.ui.label_ability.setText("Good As Gold")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Vessel Of Ruin":
            self.window.ui.label_ability.setText("Vessel Of Ruin")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sword Of Ruin":
            self.window.ui.label_ability.setText("Sword Of Ruin")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Tablets Of Ruin":
            self.window.ui.label_ability.setText("Tablets Of Ruin")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Beads Of Ruin":
            self.window.ui.label_ability.setText("Beads Of Ruin")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Orichalcum Pulse":
            self.window.ui.label_ability.setText("Orichalcum Pulse")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Hadron Engine":
            self.window.ui.label_ability.setText("Hadron Engine")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Opportunist":
            self.window.ui.label_ability.setText("Opportunist")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Cud Chew":
            self.window.ui.label_ability.setText("Cud Chew")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Sharpness":
            self.window.ui.label_ability.setText("Sharpness")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Supreme Overlord":
            self.window.ui.label_ability.setText("Supreme Overlord")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Costar":
            self.window.ui.label_ability.setText("Costar")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Toxic Debris":
            self.window.ui.label_ability.setText("Toxic Debris")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Armor Tail":
            self.window.ui.label_ability.setText("Armor Tail")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Earth Eater":
            self.window.ui.label_ability.setText("Earth Eater")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Mycelium Might":
            self.window.ui.label_ability.setText("Mycelium Might")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Hospitality":
            self.window.ui.label_ability.setText("Hospitality")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Minds Eye":
            self.window.ui.label_ability.setText("Minds Eye")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Embody Aspect Teal":
            self.window.ui.label_ability.setText("Embody Aspect Teal")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Embody Aspect Hearthflame":
            self.window.ui.label_ability.setText("Embody Aspect Hearthflame")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Embody Aspect Wellspring":
            self.window.ui.label_ability.setText("Embody Aspect Wellspring")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Embody Aspect Cornerstone":
            self.window.ui.label_ability.setText("Embody Aspect Cornerstone")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Toxic Chain":
            self.window.ui.label_ability.setText("Toxic Chain")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Supersweet Syrup":
            self.window.ui.label_ability.setText("Supersweet Syrup")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Tera Shift":
            self.window.ui.label_ability.setText("Tera Shift")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Tera Shell":
            self.window.ui.label_ability.setText("Tera Shell")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Teraform Zero":
            self.window.ui.label_ability.setText("Teraform Zero")
            self.window.show()
        elif self.ui.comboBox_Ability.currentText()  == "Poison Puppeteer":
            self.window.ui.label_ability.setText("Poison Puppeteer")
            self.window.show()
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Error")
            dialog.setText(f"{self.ui.comboBox_Ability.currentText()} is not a valid Ability")
            dialog.exec()
