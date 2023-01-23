import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt6.QtGui import QPalette, QColor


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.name = None
        self.email = None
        self.password = str
        self.password_confirm = str
        self.input_name = None
        self.input_email = None
        self.input_password = None
        self.button_okay = None
        self.button_cancel = None
        self.input_password_confirm = None
        self.test()

    def test(self):
        self.setWindowTitle("My App")

        layout = QGridLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)

        # acutal form
        self.name = QLabel("Name")
        layout.addWidget(self.name, 1, 0)

        self.email = QLabel("E-Mail")
        layout.addWidget(self.email, 2, 0)

        self.password = QLabel("Password")
        layout.addWidget(self.password, 3, 0)

        self.password_confirm = QLabel("Password-Confirm")
        layout.addWidget(self.password_confirm, 4, 0)

        self.input_name = QLineEdit()
        layout.addWidget(self.input_name, 1, 1)

        self.input_email = QLineEdit()
        layout.addWidget(self.input_email, 2, 1)

        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_password, 3, 1)

        self.input_password_confirm = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_password_confirm, 4, 1)

        self.button_okay = QPushButton("okay")
        self.button_okay.clicked.connect(self.show_fields)
        layout.addWidget(self.button_okay, 5, 1)

        self.button_cancel = QPushButton("cancel")
        layout.addWidget(self.button_cancel, 6, 1)

    def password_check(self, password, password_confirm):
        if password == password_confirm:
            print(f"Password is valid")
            return True
        else:
            print(f"Password is invalid")
            return False

    def show_fields(self):
        arr = []
        name = self.input_name.text()
        email = self.input_email.text()
        password = self.input_password.text()
        password_confirm = self.input_password_confirm.text()

        check = self.password_check(password, password_confirm)
        if check:
            arr.append((name, email, password))
            print(f"{arr}")
        else:
            print(f"todo: reload window")


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


def main():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
