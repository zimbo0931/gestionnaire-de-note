import sys
from PySide2.QtWidgets import (QLabel, QApplication,
    QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy, QMainWindow)
import numpy as np
import matplotlib.pyplot as plt

filename = "gestionnaire.data"

class gestionnaire(QMainWindow):
    def __init__(,gestionnaire,self): #constructeur
        super(gestionnaire, self).__init__(parent)
        self.gestiondoc= {}
        # définir les QWidgets

        self.gestiondoc= self.lireJSON(filename)


        # définition Layout

if __name__ == '__main__': # on fait ici les fonctions, on apelle aussi les fonctions
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    gestio=gestionnaire
    gestio.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
