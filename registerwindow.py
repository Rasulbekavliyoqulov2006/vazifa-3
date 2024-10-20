from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QPushButton, QLineEdit, QRadioButton, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
import sys
from loginwindow import LoginWindow

import json

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Names")
        self.setFixedSize(480, 480)

        self.pixmap = QPixmap('rasm.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)

        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())

        self.information = QLabel("         Information", self)
        self.font(self.information, 90, 10)
        self.information.setFixedSize(300, 50)

        self.fullname = QLineEdit(self)
        self.fullname.setPlaceholderText("First Name...")
        self.font(self.fullname, 135, 80)
        self.fullname.setFixedSize(200, 50)

        self.lastname = QLineEdit(self)
        self.lastname.setPlaceholderText("Last Name")
        self.font(self.lastname, 135, 150)
        self.lastname.setFixedSize(200, 50)

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("User Name")
        self.font(self.username, 135, 220)
        self.username.setFixedSize(200, 50)

        self.next_button = QPushButton("Next", self)
        self.next_button.setFixedSize(200, 50)
        self.font(self.next_button, 135, 300)
        self.next_button.clicked.connect(self.goto_info)

        self.setStyleSheet(self.style())

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 12))
        obj.move(x, y)

    def examination(self):
        username = self.username.text()
        fullname = self.fullname.text()
        lastname = self.lastname.text()

        if not username:
            QMessageBox.warning(self, "Warning", "Incorrect username")
            return False

        if not fullname:
            QMessageBox.warning(self, "Warning", "Incorrect fullname")
            return False

        if not lastname:
            QMessageBox.warning(self, "Warning", "Incorrect lastname")
            return False

        if len(username) < 5:
            QMessageBox.warning(self, "Error", "Username must be at least 5 symbols long.")
            return False

        if len(fullname) < 5:
            QMessageBox.warning(self, "Error", "Fullname must be at least 5 symbols long.")
            return False

        if len(lastname) < 5:
            QMessageBox.warning(self, "Error", "Lastname must be at least 5 symbols long.")
            return False

        return True

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
        """

    def goto_info(self):
        if self.examination():
            self.info_window = Info()
            self.info_window.show()
            self.close()

class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Info")
        self.setFixedSize(480, 480)

        self.pixmap = QPixmap('rasm.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)

        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())

        self.information = QLabel("         Information", self)
        self.font(self.information, 90, 10)
        self.information.setFixedSize(300, 50)

        self.month = QComboBox(self)
        self.month.addItems(["Month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.font(self.month, 20, 100)
        self.month.setFixedSize(130, 50)

        self.day = QLineEdit(self)
        self.day.setPlaceholderText("Day")
        self.font(self.day, 170, 100)
        self.day.setFixedSize(130, 50)

        self.year = QLineEdit(self)
        self.year.setPlaceholderText("Year")
        self.font(self.year, 320, 100)
        self.year.setFixedSize(130, 50)

        self.gender_male = QRadioButton("Male", self)
        self.font(self.gender_male, 90, 180)
        self.gender_male.setFixedSize(130, 50)

        self.gender_female = QRadioButton("Female", self)
        self.font(self.gender_female, 240, 180)
        self.gender_female.setFixedSize(130, 50)

        self.next_button = QPushButton("Next", self)
        self.next_button.setFixedSize(200, 50)
        self.font(self.next_button, 135, 250)
        self.next_button.clicked.connect(self.goto_email)

        self.setStyleSheet(self.style())

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 12))
        obj.move(x, y)

    def examination(self):
        month = self.month.currentText()
        day = self.day.text()
        year = self.year.text()

        if month == "Month":
            QMessageBox.warning(self, "Warning", "Incorrect month")
            return False

        if not day:
            QMessageBox.warning(self, "Warning", "Incorrect day")
            return False

        if not year:
            QMessageBox.warning(self, "Warning", "Incorrect year")
            return False

        if not day.isdigit() or int(day) < 1 or int(day) > 31:
            QMessageBox.warning(self, "Error", "Day must be between 1 and 31.")
            return False

        if not year.isdigit() or int(year) < 1900 or int(year) >= 2024:
            QMessageBox.warning(self, "Error", "Year must be between 1900 and 2023.")
            return False
        
        if not self.gender_male.isChecked() and not self.gender_female.isChecked():
            QMessageBox.warning(self, "Error", "Please select your gender!")
            return False
    

        return True

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

    def goto_email(self):
        if self.examination():
            self.email_window = Email()
            self.email_window.show()
            self.close()

class Email(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Email")
        self.setFixedSize(480, 480)

        self.pixmap = QPixmap('rasm.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)

        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())

        self.information = QLabel("         Create Email", self)
        self.font(self.information, 90, 10)
        self.information.setFixedSize(300, 50)

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Email")
        self.font(self.email, 135, 80)
        self.email.setFixedSize(200, 50)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.font(self.password, 135, 150)

        self.register_button = QPushButton("Register", self)
        self.register_button.setFixedSize(200, 50)
        self.font(self.register_button, 135, 220)
        self.register_button.clicked.connect(self.goto_loginwindow)

        self.setStyleSheet(self.style())

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 12))
        obj.move(x, y)

    def goto_loginwindow(self):
        self.loginwindow=LoginWindow()
        self.loginwindow.show()
        self.close()

    def examination(self):
        email = self.email.text()
        password=self.password.text()
        if not email:
            QMessageBox.warning(self, "Warning", "Email is required.")
            return False
        
        if "@" not in email or "." not in email.split("@")[-1]:
            QMessageBox.warning(self, "Error", "Invalid email format.")
            return False
        
        if not password:
            QMessageBox.warning(self, "Warning", "password is required.")
            return False
        
        return True
    


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
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())


