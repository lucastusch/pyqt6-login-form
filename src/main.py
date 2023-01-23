import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt6-title")
        self.resize(400, 200)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
