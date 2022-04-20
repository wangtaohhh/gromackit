import sys
import PyQt5.QtWidgets

class ProteinProteinDockingWindow(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # self.initUI()
        self.setWindowTitle('protein and protein')
        print(123)
        self.resize(700, 400)
	


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main = ProteinProteinDockingWindow()
    main.show()
    sys.exit(app.exec_())















