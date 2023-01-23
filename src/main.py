import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QMessageBox, QLineEdit, QLabel, QPushButton


def set_font(widget):
    font = widget.font()
    font.setPointSize(18)  # set font-size to size "18"
    widget.setFont(font)


def close_gui():
    # same as in main
    app = QApplication(sys.argv)
    sys.exit(app.exec())


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.name = str
        self.email = str
        self.password = str
        self.password_confirm = str
        self.input_name = None
        self.input_email = None
        self.input_password = None
        self.button_okay = None
        self.button_cancel = None
        self.input_password_confirm = None
        self.add_widgets()

    # function to handle content in fields
    def check_fields(self, name, email, password, password_confirm):
        arr = []

        # if everything is typed in correct
        if name != "" and email != "" and password != "" and password == password_confirm:
            self.display_alert(True, arr)  # True = everything is correct - so there's actually no need for the array

        # if something is not typed in correct
        else:
            if name == "":
                arr.append("Name is missing")
            if email == "":
                arr.append("E-Mail is missing")
            if password == "":
                arr.append("Password is missing")
            if password_confirm == "":
                arr.append("Confirmed Password is missing")
            if password != password_confirm:
                arr.append("Passwords are not matching")

            self.display_alert(False, arr)  # False = something is incorrect - arr contains incorrect stuff

    def display_alert(self, check, arr):
        alert = QMessageBox(self)

        # if everything is typed in correct
        if check:
            alert.setIcon(QMessageBox.Icon.Information)
            alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            alert.setWindowTitle("confirm-message")
            alert.setText(f"valid login, congrats")
            
        # if something is typed in incorrect or missing
        else:
            alert.setIcon(QMessageBox.Icon.Warning)
            alert.setStandardButtons(QMessageBox.StandardButton.Retry)
            alert.setWindowTitle("content-missing-message")

            alert.setText(arr[0])  # displays it from top to down - because this doesn't work:
            # for element in arr:
            #     alert.setText(f"{element}")

        alert.exec()

    def show_fields(self):
        name = self.input_name.text()
        email = self.input_email.text()
        password = self.input_password.text()
        password_confirm = self.input_password_confirm.text()

        self.check_fields(name, email, password, password_confirm)

    def add_widgets(self):
        self.setWindowTitle("My login-form")

        layout = QGridLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # padding on all sides
        self.setLayout(layout)

        self.name = QLabel("Name")
        set_font(self.name)  # change font
        layout.addWidget(self.name, 1, 0)  # layout.addWidget(self.name, y-value, x-value)

        self.email = QLabel("E-Mail")
        set_font(self.email)
        layout.addWidget(self.email, 2, 0)

        self.password = QLabel("Password")
        set_font(self.password)
        layout.addWidget(self.password, 3, 0)

        self.password_confirm = QLabel("Password-Confirm")
        set_font(self.password_confirm)
        layout.addWidget(self.password_confirm, 4, 0)

        self.input_name = QLineEdit()
        set_font(self.input_name)
        layout.addWidget(self.input_name, 1, 1)

        self.input_email = QLineEdit()
        set_font(self.input_email)
        layout.addWidget(self.input_email, 2, 1)

        self.input_password = QLineEdit()
        set_font(self.input_password)
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)  # make password hidden
        layout.addWidget(self.input_password, 3, 1)

        self.input_password_confirm = QLineEdit()
        set_font(self.input_password_confirm)
        self.input_password_confirm.setEchoMode(QLineEdit.EchoMode.Password)  # make password-confirm hidden
        layout.addWidget(self.input_password_confirm, 4, 1)

        self.button_okay = QPushButton("okay")
        set_font(self.button_okay)
        self.button_okay.clicked.connect(self.show_fields)  # connect with show_fields (when clicked => show_fields)
        layout.addWidget(self.button_okay, 5, 1)

        self.button_cancel = QPushButton("cancel")
        set_font(self.button_cancel)
        self.button_cancel.clicked.connect(close_gui)  # connect with show_fields (when clicked => close_gui)
        layout.addWidget(self.button_cancel, 6, 1)


def main():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
