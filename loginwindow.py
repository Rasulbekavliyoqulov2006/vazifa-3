from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox,QApplication
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import json
import sys
from quiz import One

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setFixedSize(480, 480)

        self.pixmap = QPixmap('rasm.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)

        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())

        self.username_text = QLabel("USERNAME", self)
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("     username...")
        self.font(self.username, 83, 75)
        self.font(self.username_text, 149, 10)
        self.username.setFixedSize(350, 55)

        self.password_text = QLabel("PASSWORD", self)
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("     password...") 
        self.password.setEchoMode(QLineEdit.Password)  
        self.font(self.password, 83, 225)
        self.font(self.password_text, 149, 160)
        self.password.setFixedSize(350, 55)

        self.login_button = QPushButton("LOGIN", self)
        self.font(self.login_button, 83, 400)
        self.login_button.setFixedSize(350, 55)
        self.login_button.clicked.connect(self.goto_one)
        

        self.setStyleSheet(self.style())

        self.show()

    

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 20))
        obj.move(x, y)
    

    def goto_one(self):
        self.window_one=One()
        self.window_one.show()
        self.close()

    def style(self):
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
            QLineEdit {
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
            QComboBox {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
            QRadioButton {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """

    def inspection(self):
        username = self.username.text()
        password = self.password.text()

        if not username:
            QMessageBox.warning(self, "Input Error", "Username is required.")
            return False
        
        if not password:
            QMessageBox.warning(self, "Input Error", "Password is required.")
            return False
        
        if len(username) < 5:
            QMessageBox.warning(self, "Error", "Username must be at least 5 symbols long.")
            return False

        if len(password) < 8:
            QMessageBox.warning(self, "Error", "Password must be at least 8 symbols long.")
            return False
        
        return True
    

if __name__=="__main__":
    app=QApplication(sys.argv)
    log_win=LoginWindow()
    sys.exit(app.exec_())
