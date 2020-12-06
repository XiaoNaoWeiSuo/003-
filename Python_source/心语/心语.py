import Ui_心语UI
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    npc = Ui_心语UI.Ui_MainWindow()
    npc.setupUi(window)
    window.show()
    sys.exit(app.exec_())
