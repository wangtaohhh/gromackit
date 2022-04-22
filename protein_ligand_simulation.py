from PyQt5 import QtWidgets,QtCore,QtGui

import sys

class ProteinLigandSimulation(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('protein ligand simulation')
        self.resize(700,400)
        
        self.layout = QtWidgets.QVBoxLayout()

        self.button_simulation = QtWidgets.QPushButton('Run...')
        self.button_simulation.clicked.connect(self.run_simulation)


    def run_simulation(self):
        return command_run_simulation













