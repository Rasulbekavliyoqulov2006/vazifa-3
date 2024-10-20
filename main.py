from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import sys
from loginwindow import LoginWindow 
from registerwindow import RegisterWindow



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main window")
        self.setFixedSize(480, 480)

        self.pixmap = QPixmap('rasm.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)

        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())

        self.welcome = QLabel("Welcome guys", self)
        self.font(self.welcome, 100, 50)
        self.welcome.setFixedSize(280, 60)

        self.login_button = QPushButton("Login", self)
        self.font(self.login_button, 100, 200)
        self.login_button.setFixedSize(280, 60)
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Register", self)
        self.font(self.register_button, 100, 280)
        self.register_button.setFixedSize(280, 60)
        self.register_button.clicked.connect(self.register)  
        self.setStyleSheet(self.stile())

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 20))
        obj.move(x, y)

    def stile(self):
        return """
            QWidget {
                background-color: white;
                color: #213D44;
            }
            QPushButton {
                background-color: white;  
                color: #213D44;               
                border: 4px solid black;  
                border-radius: 10px;      
            }
            QLabel {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """

    def login(self):
        if self.check_login_condition():
            self.login_connect = LoginWindow()
            self.login_connect.show()
            self.close()
        else:
            self.show_message("Login failed. Please try again.")

    def register(self):
        if self.check_register_condition():
            self.register_connect = RegisterWindow()
            self.register_connect.show()
            self.close()
        else:
            self.show_message("Registration failed. Please try again.")

    def check_login_condition(self):
        return True

    def check_register_condition(self):
        return True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
