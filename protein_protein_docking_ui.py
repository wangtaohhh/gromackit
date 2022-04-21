import sys
from tkinter import W
from turtle import pu
import PyQt5.QtWidgets
import subprocess


class ProteinProteinDockingWindow(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()
        self.setWindowTitle('protein and protein')
        self.resize(700, 400)
        
        self.layout = PyQt5.QtWidgets.QHBoxLayout()
        
        self.water_model = PyQt5.QtWidgets.QComboBox()
        self.water_model.addItem('spce')
        self.water_model.addItem('spc')
        # self.water_model.currentIndexChanged.connect(self.water_model_user_choose)
        self.button_all_in_one = PyQt5.QtWidgets.QPushButton("run simulation")
        
        self.layout.addWidget(self.water_model)
        self.layout.addWidget(self.button_all_in_one)


        self.setLayout(self.layout)
        self.button_all_in_one.clicked.connect(self.run_all_in_one)

    def run_all_in_one(self, protein):
        water_model = self.water_model.currentText()
        print(water_model)
        subprocess.call(
            [
            'gmx', 'pdb2gmx'
            ,'-f', '1aki.pdb'
            ,'-o', 'protein.gro'
            ,'-p', 'protein.top'
            ,'-water', water_model
            ,'-ff', 'amber03'
            ])



    def water_model_user_choose(self, water_model_from_combobox):        
        return water_model_from_combobox


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main = ProteinProteinDockingWindow()
    main.show()
    sys.exit(app.exec_())















