from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.AbilityWindow import AbilityWindow
from src.MoveWindow import MoveWindow
from src.PokemonWindow import PokemonWindow
from ui.ui_mainwindow import Ui_MainWindow


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
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ivysaur":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Venusaur":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Charmander":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Charmeleon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Charizard":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Squirtle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wartortle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Blastoise":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Caterpie":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Metapod":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Butterfree":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Weedle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kakuna":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Beedrill":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pidgey":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pidgeotto":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pidgeot":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rattata":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Raticate":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spearow":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Fearow":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ekans":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Arbok":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pikachu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Raichu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sandshrew":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sandslash":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nidoran Female":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nidorina":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nidoqueen":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nidoran Male":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nidorino":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nidoking":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Clefairy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Clefable":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vulpix":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ninetales":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Jigglypuff":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wigglytuff":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zubat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Golbat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Oddish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gloom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vileplume":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Paras":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Parasect":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Venonat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Venomoth":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Diglett":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dugtrio":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Meowth":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Persian":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Psyduck":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Golduck":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mankey":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Primeape":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Growlithe":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Arcanine":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Poliwag":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Poliwhirl":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Poliwrath":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Abra":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kadabra":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Alakazam":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Machop":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Machoke":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Machamp":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bellsprout":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Weepinbell":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Victreebel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tentacool":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tentacruel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Geodude":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Graveler":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Golem":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ponyta":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rapidash":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Slowpoke":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Slowbro":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Magnemite":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Magneton":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Farfetch'd":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Doduo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dodrio":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Seel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dewgong":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Grimer":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Muk":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shellder":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cloyster":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gastly":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Haunter":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gengar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Onix":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Drowzee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hypno":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Krabby":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kingler":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Voltorb":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Electrode":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Exeggcute":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Exeggutor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cubone":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Marowak":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hitmonlee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hitmonchan":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lickitung":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Koffing":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Weezing":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rhyhorn":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rhydon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chansey":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tangela":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kangaskhan":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Horsea":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Seadra":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Goldeen":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Seaking":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Staryu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Starmie":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mr. Mime":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Scyther":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Jynx":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Electabuzz":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Magmar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pinsir":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tauros":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Magikarp":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gyarados":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lapras":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ditto":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Eevee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vaporeon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Jolteon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Flareon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Porygon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Omanyte":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Omastar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kabuto":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kabutops":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Aerodactyl":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Snorlax":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Articuno":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zapdos":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Moltres":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dratini":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dragonair":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dragonite":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mewtwo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mew":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chikorita":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bayleef":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Meganium":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cyndaquil":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Quilava":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Typhlosion":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Totodile":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Croconaw":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Feraligatr":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sentret":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Furret":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hoothoot":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Noctowl":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ledyba":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ledian":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spinarak":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ariados":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Crobat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chinchou":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lanturn":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pichu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cleffa":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Igglybuff":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Togepi":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Togetic":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Natu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Xatu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mareep":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Flaaffy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ampharos":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bellossom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Marill":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Azumarill":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sudowoodo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Politoed":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hoppip":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Skiploom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Jumpluff":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Aipom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sunkern":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sunflora":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Yanma":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wooper":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Quagsire":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Espeon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Umbreon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Murkrow":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Slowking":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Misdreavus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Unown":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wobbuffet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Girafarig":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pineco":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Forretress":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dunsparce":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gligar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Steelix":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Snubbull":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Granbull":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Qwilfish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Scizor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shuckle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Heracross":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sneasel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Teddiursa":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ursaring":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Slugma":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Magcargo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Swinub":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Piloswine":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Corsola":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Remoraid":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Octillery":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Delibird":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mantine":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Skarmory":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Houndour":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Houndoom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kingdra":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Phanpy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Donphan":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Porygon2":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Stantler":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Smeargle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tyrogue":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hitmontop":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Smoochum":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Elekid":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Magby":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Miltank":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Blissey":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Raikou":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Entei":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Suicune":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Larvitar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pupitar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tyranitar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lugia":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ho-oh":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Celebi":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Treecko":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Grovyle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sceptile":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Torchic":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Combusken":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Blaziken":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mudkip":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Marshtomp":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Swampert":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Poochyena":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mightyena":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zigzagoon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Linoone":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wurmple":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Silcoon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Beautifly":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cascoon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dustox":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lotad":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lombre":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ludicolo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Seedot":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nuzleaf":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shiftry":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Taillow":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Swellow":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wingull":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pelipper":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ralts":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kirlia":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gardevoir":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Surskit":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Masquerain":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shroomish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Breloom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Slakoth":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vigoroth":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Slaking":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nincada":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ninjask":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shedinja":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Whismur":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Loudred":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Exploud":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Makuhita":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hariyama":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Azurill":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nosepass":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Skitty":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Delcatty":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sableye":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mawile":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Aron":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lairon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Aggron":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Meditite":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Medicham":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Electrike":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Manectric":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Plusle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Minun":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Volbeat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Illumise":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Roselia":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gulpin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Swalot":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Carvanha":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sharpedo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wailmer":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wailord":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Numel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Camerupt":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Torkoal":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spoink":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Grumpig":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spinda":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Trapinch":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vibrava":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Flygon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cacnea":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cacturne":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Swablu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Altaria":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zangoose":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Seviper":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lunatone":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Solrock":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Barboach":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Whiscash":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Corphish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Crawdaunt":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Baltoy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Claydol":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lileep":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cradily":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Anorith":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Armaldo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Feebas":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Milotic":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Castform":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kecleon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shuppet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Banette":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Duskull":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dusclops":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tropius":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chimecho":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Absol":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wynaut":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Snorunt":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Glalie":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spheal":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sealeo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Walrein":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Clamperl":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Huntail":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gorebyss":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Relicanth":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Luvdisc":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bagon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shelgon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Salamence":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Beldum":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Metang":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Metagross":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Regirock":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Regice":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Registeel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Latias":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Latios":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kyogre":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Groudon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rayquaza":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Jirachi":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Deoxys":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Turtwig":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Grotle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Torterra":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chimchar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Monferno":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Infernape":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Piplup":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Prinplup":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Empoleon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Starly":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Staravia":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Staraptor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bidoof":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bibarel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kricketot":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kricketune":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shinx":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Luxio":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Luxray":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Budew":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Roserade":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cranidos":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rampardos":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shieldon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bastiodon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Burmy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wormadam":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mothim":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Combee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vespiquen":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pachirisu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Buizel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Floatzel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cherubi":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cherrim":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shellos":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gastrodon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ambipom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Drifloon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Drifblim":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Buneary":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lopunny":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mismagius":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Honchkrow":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Glameow":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Purugly":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chingling":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Stunky":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Skuntank":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bronzor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bronzong":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bonsly":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mime Jr.":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Happiny":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chatot":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spiritomb":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gible":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gabite":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Garchomp":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Munchlax":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Riolu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lucario":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hippopotas":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hippowdon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Skorupi":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Drapion":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Croagunk":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Toxicroak":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Carnivine":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Finneon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lumineon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mantyke":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Snover":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Abomasnow":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Weavile":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Magnezone":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lickilicky":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rhyperior":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tangrowth":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Electivire":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Magmortar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Togekiss":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Yanmega":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Leafeon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Glaceon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gliscor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mamoswine":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Porygon-Z":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gallade":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Probopass":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dusknoir":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Froslass":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rotom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Uxie":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mesprit":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Azelf":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dialga":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Palkia":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Heatran":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Regigigas":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Giratina":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cresselia":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Phione":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Manaphy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Darkrai":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shaymin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Arceus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Victini":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Snivy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Servine":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Serperior":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tepig":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pignite":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Emboar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Oshawott":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dewott":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Samurott":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Patrat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Watchog":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lillipup":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Herdier":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Stoutland":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Purrloin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Liepard":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pansage":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Simisage":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pansear":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Simisear":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Panpour":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Simipour":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Munna":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Musharna":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pidove":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tranquill":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Unfezant":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Blitzle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zebstrika":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Roggenrola":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Boldore":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gigalith":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Woobat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Swoobat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Drilbur":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Excadrill":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Audino":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Timburr":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gurdurr":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Conkeldurr":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tympole":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Palpitoad":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Seismitoad":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Throh":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sawk":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sewaddle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Swadloon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Leavanny":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Venipede":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Whirlipede":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Scolipede":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cottonee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Whimsicott":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Petilil":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lilligant":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Basculin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sandile":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Krokorok":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Krookodile":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Darumaka":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Darmanitan":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Maractus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dwebble":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Crustle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Scraggy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Scrafty":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sigilyph":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Yamask":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cofagrigus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tirtouga":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Carracosta":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Archen":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Archeops":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Trubbish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Garbodor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zorua":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zoroark":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Minccino":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cinccino":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gothita":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gothorita":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gothitelle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Solosis":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Duosion":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Reuniclus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ducklett":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Swanna":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vanillite":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vanillish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vanilluxe":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Deerling":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sawsbuck":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Emolga":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Karrablast":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Escavalier":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Foongus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Amoonguss":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Frillish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Jellicent":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Alomomola":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Joltik":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Galvantula":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ferroseed":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ferrothorn":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Klink":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Klang":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Klinklang":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tynamo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Eelektrik":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Eelektross":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Elgyem":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Beheeyem":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Litwick":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lampent":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chandelure":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Axew":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Fraxure":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Haxorus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cubchoo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Beartic":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cryogonal":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shelmet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Accelgor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Stunfisk":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mienfoo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mienshao":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Druddigon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Golett":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Golurk":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pawniard":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bisharp":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bouffalant":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rufflet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Braviary":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vullaby":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mandibuzz":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Heatmor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Durant":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Deino":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zweilous":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hydreigon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Larvesta":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Volcarona":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cobalion":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Terrakion":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Virizion":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tornadus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Thundurus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Reshiram":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zekrom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Landorus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kyurem":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Keldeo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Meloetta":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Genesect":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chespin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Quilladin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chesnaught":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Fennekin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Braixen":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Delphox":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Froakie":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Frogadier":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Greninja":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bunnelby":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Diggersby":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Fletchling":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Fletchinder":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Talonflame":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Scatterbug":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spewpa":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vivillon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Litleo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pyroar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Flabébé":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Floette":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Florges":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Skiddo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gogoat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pancham":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pangoro":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Furfrou":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Espurr":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Meowstic":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Honedge":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Doublade":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Aegislash":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spritzee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Aromatisse":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Swirlix":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Slurpuff":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Inkay":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Malamar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Binacle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Barbaracle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Skrelp":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dragalge":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Clauncher":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Clawitzer":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Helioptile":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Heliolisk":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tyrunt":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tyrantrum":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Amaura":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Aurorus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sylveon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hawlucha":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dedenne":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Carbink":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Goomy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sliggoo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Goodra":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Klefki":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Phantump":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Trevenant":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pumpkaboo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gourgeist":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bergmite":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Avalugg":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Noibat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Noivern":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Xerneas":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Yveltal":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zygarde":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Diancie":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hoopa":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Volcanion":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rowlet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dartrix":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Decidueye":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Litten":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Torracat":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Incineroar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Popplio":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Brionne":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Primarina":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pikipek":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Trumbeak":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Toucannon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Yungoos":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gumshoos":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Grubbin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Charjabug":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Vikavolt":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Crabrawler":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Crabominable":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Oricorio":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cutiefly":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ribombee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rockruff":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lycanroc":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wishiwashi":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mareanie":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Toxapex":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mudbray":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mudsdale":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dewpider":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Araquanid":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Fomantis":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lurantis":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Morelull":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shiinotic":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Salandit":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Salazzle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Stufful":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bewear":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bounsweet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Steenee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tsareena":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Comfey":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Oranguru":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Passimian":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wimpod":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Golisopod":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sandygast":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Palossand":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pyukumuku":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Type: Null":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Silvally":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Minior":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Komala":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Turtonator":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Togedemaru":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mimikyu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bruxish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Drampa":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dhelmise":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Jangmo-o":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hakamo-o":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kommo-o":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tapu Koko":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tapu Lele":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tapu Bulu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tapu Fini":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cosmog":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cosmoem":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Solgaleo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lunala":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nihilego":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Buzzwole":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pheromosa":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Xurkitree":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Celesteela":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kartana":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Guzzlord":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Necrozma":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Magearna":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Marshadow":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Poipole":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Naganadel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Stakataka":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Blacephalon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zeraora":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Meltan":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Melmetal":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Grookey":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Thwackey":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rillaboom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Scorbunny":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Raboot":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cinderace":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sobble":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Drizzile":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Inteleon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Skwovet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Greedent":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rookidee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Corvisquire":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Corviknight":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Blipbug":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dottler":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Orbeetle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nickit":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Thievul":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gossifleur":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Eldegoss":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wooloo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dubwool":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chewtle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Drednaw":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Yamper":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Boltund":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rolycoly":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Carkol":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Coalossal":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Applin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Flapple":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Appletun":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Silicobra":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sandaconda":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cramorant":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Arrokuda":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Barraskewda":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Toxel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Toxtricity":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sizzlipede":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Centiskorch":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Clobbopus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Grapploct":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sinistea":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Polteageist":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hatenna":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hattrem":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hatterene":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Impidimp":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Morgrem":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Grimmsnarl":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Obstagoon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Perrserker":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cursola":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sirfetch'd":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mr. Rime":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Runerigus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Milcery":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Alcremie":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Falinks":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pincurchin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Snom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Frosmoth":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Stonjourner":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Eiscue":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Indeedee":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Morpeko":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cufant":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Copperajah":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dracozolt":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Arctozolt":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dracovish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Arctovish":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Duraludon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dreepy":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Drakloak":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dragapult":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zacian":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zamazenta":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Eternatus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kubfu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Urshifu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Zarude":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Regieleki":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Regidrago":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Glastrier":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spectrier":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Calyrex":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wyrdeer":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kleavor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ursaluna":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Basculegion":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sneasler":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Overqwil":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Enamorus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sprigatito":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Floragato":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Meowscarada":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Fuecoco":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Crocalor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Skeledirge":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Quaxly":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Quaxwell":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Quaquaval":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lechonk":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Oinkologne":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tarountula":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Spidops":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nymble":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Lokix":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pawmi":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pawmo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pawmot":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tandemaus":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Maushold":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Fidough":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dachsbun":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Smoliv":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dolliv":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Arboliva":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Squawkabilly":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Nacli":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Naclstack":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Garganacl":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Charcadet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Armarouge":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ceruledge":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tadbulb":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bellibolt":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wattrel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kilowattrel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Maschiff":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Mabosstiff":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Shroodle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Grafaiai":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bramblin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Brambleghast":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Toedscool":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Toedscruel":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Klawf":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Capsakid":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Scovillain":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rellor":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Rabsca":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Flittle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Espathra":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tinkatink":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tinkatuff":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tinkaton":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wiglett":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wugtrio":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Bombirdier":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Finizen":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Palafin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Varoom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Revavroom":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cyclizar":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Orthworm":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Glimmet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Glimmora":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Greavard":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Houndstone":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Flamigo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cetoddle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Cetitan":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Veluza":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dondozo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Tatsugiri":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Annihilape":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Clodsire":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Farigiraf":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dudunsparce":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Kingambit":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Great Tusk":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Scream Tail":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Brute Bonnet":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Flutter Mane":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Slither Wing":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sandy Shocks":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Treads":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Bundle":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Hands":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Jugulis":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Moth":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Thorns":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Frigibax":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Arctibax":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Baxcalibur":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gimmighoul":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gholdengo":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Wo-Chien":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chien-Pao":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ting-Lu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Chi-Yu":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Roaring Moon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Valiant":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Koraidon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Miraidon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Walking Wake":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Leaves":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Dipplin":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Poltchageist":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Sinistcha":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Okidogi":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Munkidori":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Fezandipiti":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Ogerpon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Archaludon":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Hydrapple":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Gouging Fire":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Raging Bolt":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Boulder":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Iron Crown":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Terapagos":
            self.window.show()
        elif self.ui.comboBox_Pokemon.currentText() == "Pecharunt":
            self.window.show()
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Error")
            dialog.setText(f"{self.ui.comboBox_Pokemon.currentText()} is not a valid Pokemon")
            dialog.exec()

    def open_move_window(self):
        self.window = MoveWindow()
        self.window.setWindowTitle(self.ui.comboBox_Move.currentText())
        if self.ui.comboBox_Move.currentText() == "Pound":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Karate Chop":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Double Slap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Comet Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mega Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pay Day":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fire Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ice Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thunder Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Scratch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Vise Grip":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Guillotine":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Razor Wind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Swords Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Cut":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Gust":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wing Attack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Whirlwind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fly":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Slam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Vine Whip":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stomp":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Double Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mega Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Jump Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rolling Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sand Attack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Headbutt":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Horn Attack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fury Attack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Horn Drill":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tackle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Body Slam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wrap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Take Down":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thrash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Double Edge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tail Whip":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Poison Sting":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Twineedle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pin Missile":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Leer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bite":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Growl":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Roar":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sing":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Supersonic":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sonic Boom":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Disable":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Acid":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ember":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flamethrower":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mist":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Water Gun":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hydro Pump":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Surf":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ice Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Blizzard":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psybeam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bubble Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aurora Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hyper Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Peck":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Drill Peck":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Submission":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Low Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Counter":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Seismic Toss":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Strength":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Absorb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mega Drain":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Leech Seed":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Growth":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Razor Leaf":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Solar Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Poison Powder":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stun Spore":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sleep Powder":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Petal Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "String Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Rage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fire Spin":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thunder Shock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thunderbolt":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thunder Wave":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thunder":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rock Throw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Earthquake":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fissure":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dig":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Toxic":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Confusion":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psychic":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hypnosis":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Meditate":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Agility":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Quick Attack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Teleport":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Night Shade":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mimic":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Screech":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Double Team":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Recover":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Harden":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Minimize":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Smokescreen":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Confuse Ray":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Withdraw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Defense Curl":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Barrier":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Light Screen":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Haze":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Reflect":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Focus Energy":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bide":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Metronome":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mirror Move":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Self Destruct":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Egg Bomb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Smog":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sludge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bone Club":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fire Blast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Waterfall":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Clamp":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Swift":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Skull Bash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spike Cannon":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Constrict":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Amnesia":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Kinesis":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Soft Boiled":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "High Jump Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Glare":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dream Eater":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Poison Gas":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Barrage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Leech Life":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lovely Kiss":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sky Attack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Transform":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bubble":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dizzy Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spore":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psywave":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Splash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Acid Armor":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Crabhammer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Explosion":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fury Swipes":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bonemerang":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rest":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rock Slide":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hyper Fang":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sharpen":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Conversion":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tri Attack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Super Fang":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Slash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Substitute":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Struggle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sketch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Triple Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thief":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spider Web":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mind Reader":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Nightmare":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flame Wheel":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Snore":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Curse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flail":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Conversion ":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aeroblast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Cotton Spore":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Reversal":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spite":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Powder Snow":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Protect":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mach Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Scary Face":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Feint Attack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sweet Kiss":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Belly Drum":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sludge Bomb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mud Slap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Octazooka":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spikes":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Zap Cannon":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Foresight":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Destiny Bond":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Perish Song":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Icy Wind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Detect":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bone Rush":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lock On":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Outrage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sandstorm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Giga Drain":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Endure":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Charm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rollout":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "False Swipe":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Swagger":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Milk Drink":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spark":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fury Cutter":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Steel Wing":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mean Look":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Attract":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sleep Talk":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Heal Bell":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Return":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Present":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Frustration":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Safeguard":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pain Split":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sacred Fire":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magnitude":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dynamic Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Megahorn":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Breath":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Baton Pass":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Encore":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pursuit":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rapid Spin":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sweet Scent":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Iron Tail":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Metal Claw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Vital Throw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Morning Sun":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Synthesis":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Moonlight":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hidden Power":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Cross Chop":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Twister":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rain Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sunny Day":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Crunch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mirror Coat":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psych Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Extreme Speed":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ancient Power":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shadow Ball":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Future Sight":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rock Smash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Whirlpool":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Beat Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fake Out":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Uproar":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stockpile":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spit Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Swallow":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Heat Wave":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hail":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Torment":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flatter":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Will O Wisp":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Memento":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Facade":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Focus Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Smelling Salts":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Follow Me":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Nature Power":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Charge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Taunt":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Helping Hand":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Trick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Role Play":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wish":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Assist":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ingrain":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Superpower":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magic Coat":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Recycle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Revenge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Brick Break":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Yawn":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Knock Off":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Endeavor":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Eruption":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Skill Swap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Imprison":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Refresh":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Grudge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Snatch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Secret Power":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dive":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Arm Thrust":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Camouflage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tail Glow":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Luster Purge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mist Ball":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Feather Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Teeter Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Blaze Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mud Sport":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ice Ball":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Needle Arm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Slack Off":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hyper Voice":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Poison Fang":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Crush Claw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Blast Burn":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hydro Cannon":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Meteor Mash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Astonish":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Weather Ball":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aromatherapy":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fake Tears":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Air Cutter":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Overheat":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Odor Sleuth":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rock Tomb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Silver Wind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Metal Sound":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Grass Whistle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tickle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Cosmic Power":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Water Spout":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Signal Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shadow Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Extrasensory":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sky Uppercut":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sand Tomb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sheer Cold":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Muddy Water":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bullet Seed":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aerial Ace":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Icicle Spear":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Iron Defense":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Block":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Howl":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Claw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Frenzy Plant":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bulk Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bounce":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mud Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Poison Tail":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Covet":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Volt Tackle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magical Leaf":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Water Sport":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Calm Mind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Leaf Blade":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rock Blast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shock Wave":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Water Pulse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Doom Desire":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psycho Boost":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Roost":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Gravity":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Miracle Eye":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wake Up Slap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hammer Arm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Gyro Ball":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Healing Wish":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Brine":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Natural Gift":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Feint":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pluck":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tailwind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Acupressure":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Metal Burst":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "U Turn":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Close Combat":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Payback":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Assurance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Embargo":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fling":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psycho Shift":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Trump Card":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Heal Block":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wring Out":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Power Trick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Gastro Acid":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lucky Chant":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Me First":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Copycat":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Power Swap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Guard Swap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Punishment":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Last Resort":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Worry Seed":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sucker Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Toxic Spikes":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Heart Swap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aqua Ring":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magnet Rise":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flare Blitz":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Force Palm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aura Sphere":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rock Polish":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Poison Jab":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dark Pulse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Night Slash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aqua Tail":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Seed Bomb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Air Slash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "X Scissor":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bug Buzz":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Pulse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Rush":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Power Gem":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Drain Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Vacuum Wave":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Focus Blast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Energy Ball":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Brave Bird":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Earth Power":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Switcheroo":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Giga Impact":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Nasty Plot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bullet Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Avalanche":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ice Shard":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shadow Claw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thunder Fang":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ice Fang":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fire Fang":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shadow Sneak":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mud Bomb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psycho Cut":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Zen Headbutt":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mirror Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flash Cannon":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rock Climb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Defog":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Trick Room":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Draco Meteor":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Discharge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lava Plume":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Leaf Storm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Power Whip":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rock Wrecker":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Cross Poison":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Gunk Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Iron Head":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magnet Bomb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stone Edge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Captivate":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stealth Rock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Grass Knot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Chatter":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Judgment":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bug Bite":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Charge Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wood Hammer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aqua Jet":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Attack Order":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Defend Order":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Heal Order":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Head Smash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Double Hit":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Roar Of Time":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spacial Rend":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lunar Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Crush Grip":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magma Storm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dark Void":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Seed Flare":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ominous Wind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shadow Force":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hone Claws":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wide Guard":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Guard Split":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Power Split":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wonder Room":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psyshock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Venoshock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Autotomize":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rage Powder":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Telekinesis":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magic Room":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Smack Down":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Storm Throw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flame Burst":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sludge Wave":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Quiver Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Heavy Slam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Synchronoise":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Electro Ball":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Soak":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flame Charge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Coil":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Low Sweep":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Acid Spray":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Foul Play":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Simple Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Entrainment":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "After You":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Round":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Echoed Voice":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Chip Away":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Clear Smog":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stored Power":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Quick Guard":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ally Switch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Scald":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shell Smash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Heal Pulse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hex":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sky Drop":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shift Gear":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Circle Throw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Incinerate":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Quash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Acrobatics":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Reflect Type":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Retaliate":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Final Gambit":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bestow":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Inferno":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Water Pledge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fire Pledge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Grass Pledge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Volt Switch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Struggle Bug":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bulldoze":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Frost Breath":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Tail":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Work Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Electroweb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wild Charge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Drill Run":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dual Chop":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Heart Stamp":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Horn Leech":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sacred Sword":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Razor Shell":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Heat Crash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Leaf Tornado":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Steamroller":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Cotton Guard":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Night Daze":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psystrike":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tail Slap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hurricane":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Head Charge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Gear Grind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Searing Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Techno Blast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Relic Song":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Secret Sword":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Glaciate":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bolt Strike":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Blue Flare":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fiery Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Freeze Shock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ice Burn":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Snarl":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Icicle Crash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "V Create":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fusion Flare":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fusion Bolt":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flying Press":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mat Block":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Belch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rototiller":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sticky Web":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fell Stinger":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Phantom Force":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Trick Or Treat":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Noble Roar":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ion Deluge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Parabolic Charge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Forests Curse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Petal Blizzard":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Freeze Dry":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Disarming Voice":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Parting Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Topsy Turvy":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Draining Kiss":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Crafty Shield":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flower Shield":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Grassy Terrain":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Misty Terrain":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Electrify":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Play Rough":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fairy Wind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Moonblast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Boomburst":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fairy Lock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Kings Shield":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Play Nice":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Confide":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Diamond Storm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Steam Eruption":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hyperspace Hole":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Water Shuriken":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mystical Fire":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spiky Shield":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aromatic Mist":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Eerie Impulse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Venom Drench":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Powder":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Geomancy":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magnetic Flux":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Happy Hour":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Electric Terrain":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dazzling Gleam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Celebrate":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hold Hands":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Baby Doll Eyes":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Nuzzle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hold Back":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Infestation":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Power Up Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Oblivion Wing":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thousand Arrows":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thousand Waves":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lands Wrath":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Light Of Ruin":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Origin Pulse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Precipice Blades":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Ascent":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hyperspace Fury":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shore Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "First Impression":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Baneful Bunker":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spirit Shackle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Darkest Lariat":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sparkling Aria":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ice Hammer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Floral Healing":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "High Horsepower":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Strength Sap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Solar Blade":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Leafage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spotlight":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Toxic Thread":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Laser Focus":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Gear Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Throat Chop":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pollen Puff":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Anchor Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psychic Terrain":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lunge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fire Lash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Power Trip":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Burn Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Speed Swap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Smart Strike":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Purify":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Revelation Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Core Enforcer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Trop Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Instruct":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Beak Blast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Clanging Scales":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Hammer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Brutal Swing":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aurora Veil":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shell Trap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fleur Cannon":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psychic Fangs":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stomping Tantrum":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shadow Bone":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Accelerock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Liquidation":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Prismatic Laser":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spectral Thief":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sunsteel Strike":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Moongeist Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tearful Look":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Zing Zap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Natures Madness":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Multi Attack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mind Blown":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Plasma Fists":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Photon Geyser":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Zippy Zap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Splishy Splash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Floaty Fall":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pika Papow":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bouncy Bubble":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Buzzy Buzz":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sizzly Slide":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Glitzy Glow":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Baddy Bad":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sappy Seed":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Freezy Frost":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sparkly Swirl":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Veevee Volley":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Double Iron Bash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Breakneck Blitz":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "All Out Pummeling":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Supersonic Skystrike":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Acid Downpour":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tectonic Rage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Continental Crush":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Savage Spin Out":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Never Ending Nightmare":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Corkscrew Crash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Inferno Overdrive":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hydro Vortex":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bloom Doom":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Gigavolt Havoc":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shattered Psyche":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Subzero Slammer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Devastating Drake":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Black Hole Eclipse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Twinkle Tackle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Catastropika":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Move 10000000 Volt Thunderbolt":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stoked Sparksurfer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Extreme Evoboost":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pulverizing Pancake":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Genesis Supernova":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sinister Arrow Raid":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Malicious Moonsault":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Oceanic Operetta":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Splintered Stormshards":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lets Snuggle Forever":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Clangorous Soulblaze":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Guardian Of Alola":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Searing Sunraze Smash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Menacing Moonraze Maelstrom":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Light That Burns The Sky":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Soul Stealing  Star Strike":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dynamax Cannon":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Snipe Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Jaw Lock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stuff Cheeks":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "No Retreat":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tar Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magic Powder":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Darts":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Teatime":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Octolock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bolt Beak":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fishious Rend":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Court Change":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Clangorous Soul":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Body Press":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Decorate":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Drum Beating":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Snap Trap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pyro Ball":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Behemoth Blade":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Behemoth Bash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aura Wheel":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Breaking Swipe":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Branch Poke":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Overdrive":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Apple Acid":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Grav Apple":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spirit Break":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Strange Steam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Life Dew":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Obstruct":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "False Surrender":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Meteor Assault":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Eternabeam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Steel Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Expanding Force":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Steel Roller":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Scale Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Meteor Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shell Side Arm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Misty Explosion":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Grassy Glide":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rising Voltage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Terrain Pulse":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Skitter Smack":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Burning Jealousy":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lash Out":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Poltergeist":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Corrosive Gas":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Coaching":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flip Turn":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Triple Axel":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dual Wingbeat":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Scorching Sands":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Jungle Healing":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wicked Blow":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Surging Strikes":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thunder Cage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Energy":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Freezing Glare":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fiery Wrath":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thunderous Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Glacial Lance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Astral Barrage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Eerie Spell":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dire Claw":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psyshield Bash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Power Shift":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Stone Axe":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Springtide Storm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mystical Power":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Raging Fury":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wave Crash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Chloroblast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mountain Gale":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Victory Dance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Headlong Rush":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Barb Barrage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Esper Wing":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bitter Malice":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shelter":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Triple Arrows":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Infernal Parade":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ceaseless Edge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bleakwind Storm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wildbolt Storm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Sandsear Storm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lunar Blessing":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Take Heart":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Guard":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Strike":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Knuckle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Airstream":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Ooze":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Quake":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Rockfall":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Flutterby":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Phantasm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Steelspike":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Flare":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Geyser":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Overgrowth":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Lightning":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Mindstorm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Hailstorm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Wyrmwind":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Darkness":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Max Starfall":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Vine Lash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Wildfire":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Cannonade":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Befuddle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Volt Crash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Gold Rush":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Chi Strike":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Terror":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Foam Burst":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Resonance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Cuddle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Replenish":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Malodor":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Meltdown":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Drum Solo":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Fireball":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Hydrosnipe":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Wind Rage":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Gravitas":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Stonesurge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Volcalith":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Tartness":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Sweetness":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Sandblast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Stun Shock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Centiferno":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Smite":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Snooze":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Finale":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Steelsurge":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Depletion":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max One Blow":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "G Max Rapid Flow":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tera Blast":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Silk Trap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Axe Kick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Last Respects":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Lumina Crash":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Order Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Jet Punch":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spicy Extract":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Spin Out":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Population Bomb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ice Spinner":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Glaive Rush":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Revival Blessing":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Salt Cure":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Triple Dive":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mortal Spin":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Doodle":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fillet Away":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Kowtow Cleave":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Flower Trick":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Torch Song":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aqua Step":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Raging Bull":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Make It Rain":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ruination":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Collision Course":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Electro Drift":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Shed Tail":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Chilly Reception":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tidy Up":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Snowscape":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Pounce":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Trailblaze":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Chilling Water":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hyper Drill":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Twin Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Rage Fist":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Armor Cannon":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Bitter Blade":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Double Shock":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Gigaton Hammer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Comeuppance":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Aqua Cutter":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Blazing Torque":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Wicked Torque":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Noxious Torque":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Combat Torque":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Magical Torque":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psyblade":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hydro Steam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Blood Moon":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Matcha Gotcha":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Syrup Bomb":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Ivy Cudgel":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Electro Shot":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tera Starstorm":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Fickle Beam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Burning Bulwark":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Thunderclap":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Mighty Cleave":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Tachyon Cutter":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Hard Press":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Dragon Cheer":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Alluring Voice":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Temper Flare":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Supercell Slam":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Psychic Noise":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Upper Hand":
            self.window.show()
        elif self.ui.comboBox_Move.currentText() == "Malignant Chain":
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
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Drizzle":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Speed Boost":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Battle Armor":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sturdy":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Damp":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Limber":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sand Veil":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Static":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Volt Absorb":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Water Absorb":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Oblivious":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Cloud Nine":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Compound Eyes":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Insomnia":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Color Change":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Immunity":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Flash Fire":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Shield Dust":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Own Tempo":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Suction Cups":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Intimidate":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Shadow Tag":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Rough Skin":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Wonder Guard":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Levitate":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Effect Spore":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Synchronize":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Clear Body":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Natural Cure":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Lightning Rod":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Serene Grace":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Swift Swim":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Chlorophyll":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Illuminate":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Trace":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Huge Power":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Poison Point":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Inner Focus":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Magma Armor":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Water Veil":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Magnet Pull":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Soundproof":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Rain Dish":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sand Stream":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Pressure":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Thick Fat":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Early Bird":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Flame Body":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Run Away":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Keen Eye":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Hyper Cutter":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Pickup":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Truant":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Hustle":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Cute Charm":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Plus":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Minus":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Forecast":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sticky Hold":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Shed Skin":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Guts":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Marvel Scale":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Liquid Ooze":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Overgrow":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Blaze":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Torrent":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Swarm":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Rock Head":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Drought":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Arena Trap":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Vital Spirit":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "White Smoke":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Pure Power":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Shell Armor":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Air Lock":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Tangled Feet":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Motor Drive":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Rivalry":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Steadfast":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Snow Cloak":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Gluttony":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Anger Point":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Unburden":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Heatproof":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Simple":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Dry Skin":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Download":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Iron Fist":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Poison Heal":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Adaptability":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Skill Link":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Hydration":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Solar Power":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Quick Feet":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Normalize":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sniper":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Magic Guard":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "No Guard":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Stall":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Technician":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Leaf Guard":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Klutz":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Mold Breaker":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Super Luck":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Aftermath":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Anticipation":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Forewarn":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Unaware":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Tinted Lens":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Filter":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Slow Start":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Scrappy":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Storm Drain":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Ice Body":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Solid Rock":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Snow Warning":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Honey Gather":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Frisk":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Reckless":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Multitype":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Flower Gift":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Bad Dreams":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Pickpocket":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sheer Force":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Contrary":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Unnerve":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Defiant":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Defeatist":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Cursed Body":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Healer":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Friend Guard":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Weak Armor":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Heavy Metal":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Light Metal":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Multiscale":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Toxic Boost":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Flare Boost":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Harvest":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Telepathy":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Moody":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Overcoat":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Poison Touch":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Regenerator":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Big Pecks":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sand Rush":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Wonder Skin":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Analytic":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Illusion":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Imposter":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Infiltrator":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Mummy":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Moxie":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Justified":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Rattled":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Magic Bounce":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sap Sipper":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Prankster":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sand Force":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Iron Barbs":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Zen Mode":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Victory Star":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Turboblaze":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Teravolt":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Aroma Veil":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Flower Veil":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Cheek Pouch":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Protean":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Fur Coat":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Magician":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Bulletproof":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Competitive":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Strong Jaw":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Refrigerate":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sweet Veil":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Stance Change":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Gale Wings":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Mega Launcher":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Grass Pelt":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Symbiosis":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Tough Claws":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Pixilate":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Gooey":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Aerilate":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Parental Bond":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Dark Aura":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Fairy Aura":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Aura Break":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Primordial Sea":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Desolate Land":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Delta Stream":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Stamina":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Wimp Out":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Emergency Exit":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Water Compaction":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Merciless":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Shields Down":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Stakeout":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Water Bubble":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Steelworker":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Berserk":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Slush Rush":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Long Reach":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Liquid Voice":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Triage":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Galvanize":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Surge Surfer":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Schooling":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Disguise":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Battle Bond":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Power Construct":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Corrosion":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Comatose":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Queenly Majesty":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Innards Out":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Dancer":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Battery":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Fluffy":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Dazzling":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Soul Heart":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Tangling Hair":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Receiver":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Power Of Alchemy":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Beast Boost":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Rks System":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Electric Surge":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Psychic Surge":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Misty Surge":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Grassy Surge":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Full Metal Body":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Shadow Shield":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Prism Armor":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Neuroforce":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Intrepid Sword":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Dauntless Shield":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Libero":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Ball Fetch":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Cotton Down":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Propeller Tail":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Mirror Armor":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Gulp Missile":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Stalwart":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Steam Engine":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Punk Rock":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sand Spit":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Ice Scales":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Ripen":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Ice Face":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Power Spot":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Mimicry":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Screen Cleaner":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Steely Spirit":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Perish Body":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Wandering Spirit":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Gorilla Tactics":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Neutralizing Gas":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Pastel Veil":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Hunger Switch":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Quick Draw":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Unseen Fist":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Curious Medicine":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Transistor":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Dragons Maw":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Chilling Neigh":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Grim Neigh":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "As One Ice Rider":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "As One Shadow Rider":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Lingering Aroma":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Seed Sower":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Thermal Exchange":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Anger Shell":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Purifying Salt":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Well Baked Body":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Wind Rider":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Guard Dog":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Rocky Payload":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Wind Power":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Zero To Hero":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Commander":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Electromorphosis":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Protosynthesis":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Quark Drive":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Good As Gold":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Vessel Of Ruin":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sword Of Ruin":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Tablets Of Ruin":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Beads Of Ruin":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Orichalcum Pulse":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Hadron Engine":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Opportunist":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Cud Chew":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Sharpness":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Supreme Overlord":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Costar":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Toxic Debris":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Armor Tail":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Earth Eater":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Mycelium Might":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Hospitality":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Minds Eye":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Embody Aspect Teal":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Embody Aspect Hearthflame":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Embody Aspect Wellspring":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Embody Aspect Cornerstone":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Toxic Chain":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Supersweet Syrup":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Tera Shift":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Tera Shell":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Teraform Zero":
            self.window.show()
        elif self.ui.comboBox_Ability.currentText() == "Poison Puppeteer":
            self.window.show()
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Error")
            dialog.setText(f"{self.ui.comboBox_Ability.currentText()} is not a valid Ability")
            dialog.exec()
