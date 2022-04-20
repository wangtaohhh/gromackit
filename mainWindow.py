import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import protein_protein_docking_ui

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.initUI()
        self.setWindowTitle('chuizhi')

        self.resize(600, 400)
        self.layout = QVBoxLayout()
        
        self.button_1 = QPushButton('protein-protein docking')
        self.button_2 = QPushButton('protein-ligand docking')
        self.button_3 = QPushButton('protein in solvent')


        self.layout.addWidget(self.button_1)
        # self.layout.addStretch(0) #增加伸缩量
        self.layout.addWidget(self.button_2)
        # self.layout.addStretch(0) #增加伸缩量
        self.layout.addWidget(self.button_3)
        # self.layout.addStretch(10) #增加伸缩量

        # self.layout.setSpacing(1)
        self.setLayout(self.layout)
        self.button_1.clicked.connect(protein_protein_docking_ui.ProteinProteinDockingWindow().show)

 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()

   
    sys.exit(app.exec_())
















