from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
import Ui_writer
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    npc = Ui_writer.Ui_MainWindow()
    npc.setupUi(window)
    window.show()
    sys.exit(app.exec())
