from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import sys

class One(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Question 1")
        self.setFixedSize(480, 480)

        self.pixmap = QPixmap('quiz.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())


        self.question_one = QLabel("question 1", self)
        self.font(self.question_one, 100, 10)
        self.question_one.setFixedSize(220, 50)


        self.label_question = QLabel("Who created Python?", self)
        self.font(self.label_question, 35, 100)
        self.label_question.setFixedSize(400, 50)

        self.a_answer = QRadioButton("Brendan Eich", self)
        self.font(self.a_answer, 10, 200)

        self.b_answer = QRadioButton("Dennis Ritchie", self)
        self.font(self.b_answer, 10, 280)

        self.c_answer = QRadioButton("Guido van Rossum", self)
        self.font(self.c_answer, 10, 360)

        self.next_button = QPushButton("Next", self)
        self.font(self.next_button, 360, 420)

        self.next_button.clicked.connect(self.goto_question_2)
        self.setStyleSheet(self.style())
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 20))
        obj.move(x, y)

    def examination(self):
        if not self.a_answer.isChecked() and not self.b_answer.isChecked() and not self.c_answer.isChecked():
            QMessageBox.warning(self, "Error", "Please select an answer!")
            return False
        return True

    def goto_question_2(self):
        if self.examination():
            self.quiz_window = Two()
            self.quiz_window.show()
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
            QRadioButton {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """



class Two(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Question 2")
        self.setFixedSize(480, 480)

        self.pixmap = QPixmap('quiz.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())

        self.label_question = QLabel("Question 2", self)
        self.font(self.label_question, 100, 10)
        self.label_question.setFixedSize(220, 50)

        self.question_two = QLabel("Who created C?", self)
        self.font(self.question_two, 35, 100)

        self.a_answer = QRadioButton("Guido van Rossum", self)
        self.font(self.a_answer, 10, 200)

        self.b_answer = QRadioButton("Brendan Eich", self)
        self.font(self.b_answer, 10, 280)

        self.c_answer = QRadioButton("Dennis Ritchie", self)
        self.font(self.c_answer, 10, 360)

        self.next_button = QPushButton("Next", self)
        self.font(self.next_button, 360, 420)

        self.next_button.clicked.connect(self.goto_question_3)
        self.setStyleSheet(self.style())
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 20))
        obj.move(x, y)

    def examination(self):
        if not self.a_answer.isChecked() and not self.b_answer.isChecked() and not self.c_answer.isChecked():
            QMessageBox.warning(self, "Error", "Please select an answer!")
            return False
        return True

    def goto_question_3(self):
        if self.examination():
            self.quiz_window = Three()
            self.quiz_window.show()
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
            QRadioButton {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """


class Three(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Question 3")
        self.setFixedSize(480, 480)

        
        self.pixmap = QPixmap('quiz.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())

        
        self.label_question = QLabel("Question 3", self)
        self.font(self.label_question, 100, 10)
        self.label_question.setFixedSize(220, 50)

        
        self.question_three = QLabel("Who created C++?", self)
        self.font(self.question_three, 35, 100)

        
        self.a_answer = QRadioButton("James Gosling", self)
        self.font(self.a_answer, 10, 200)

        self.b_answer = QRadioButton("Bjarne Stroustrup", self)
        self.font(self.b_answer, 10, 280)

        self.c_answer = QRadioButton("Yukihiro Matsumoto", self)
        self.font(self.c_answer, 10, 360)

        
        self.next_button = QPushButton("Next", self)
        self.font(self.next_button, 360, 420)

        self.next_button.clicked.connect(self.goto_question_4)  
        self.setStyleSheet(self.style())
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 20))
        obj.move(x, y)

    def examination(self):
        if not self.a_answer.isChecked() and not self.b_answer.isChecked() and not self.c_answer.isChecked():
            QMessageBox.warning(self, "Error", "Please select an answer!")
            return False
        return True

    def goto_question_4(self):
        if self.examination():  
            self.quiz_window = Four() 
            self.quiz_window.show()
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
            QRadioButton {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """

    


class Four(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Question 4")
        self.setFixedSize(480, 480)

        # Background image
        self.pixmap = QPixmap('quiz.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())

        # Title of the question
        self.label_question = QLabel("Question 4", self)
        self.font(self.label_question, 100, 10)
        self.label_question.setFixedSize(220, 50)

        
        self.question_four = QLabel("Who created Java?", self)
        self.font(self.question_four, 35, 100)

        
        self.a_answer = QRadioButton("Bjarne Stroustrup", self)
        self.font(self.a_answer, 10, 200)

        self.b_answer = QRadioButton("Dennis Ritchie", self)
        self.font(self.b_answer, 10, 280)

        self.c_answer = QRadioButton("James Gosling", self)
        self.font(self.c_answer, 10, 360)

        
        self.next_button = QPushButton("Next", self)
        self.font(self.next_button, 360, 420)

        self.next_button.clicked.connect(self.goto_five)  
        self.setStyleSheet(self.style())
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 20))
        obj.move(x, y)

    def examination(self):
        if not self.a_answer.isChecked() and not self.b_answer.isChecked() and not self.c_answer.isChecked():
            QMessageBox.warning(self, "Error", "Please select an answer!")
            return False
        return True

    def goto_five(self):
        if self.examination():  
            self.result_window = Five()
            self.result_window.show()
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
            QRadioButton {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """

class Five(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Question 5")
        self.setFixedSize(480, 480)
        self.pixmap = QPixmap('quiz.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())

        self.label_question = QLabel("Question 5", self)
        self.font(self.label_question, 100, 10)
        self.label_question.setFixedSize(220, 50)

        self.question_five = QLabel("Which one do you like?", self)
        self.font(self.question_five, 35, 100)

        self.a_answer = QRadioButton("BackEnd", self)
        self.font(self.a_answer, 10, 200)

        self.b_answer = QRadioButton("FrontEnd", self)
        self.font(self.b_answer, 10, 280)

        self.c_answer = QRadioButton("FullStack", self)
        self.font(self.c_answer, 10, 360)

        self.next_button = QPushButton("Next", self)
        self.font(self.next_button, 360, 420)
        self.next_button.clicked.connect(self.goto_theend)

        self.setStyleSheet(self.style())
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 20))
        obj.move(x, y)
    
    def examination(self):
        if not self.a_answer.isChecked() and not self.b_answer.isChecked() and not self.c_answer.isChecked():
            QMessageBox.warning(self, "Error", "Please select an answer!")
            return False
        return True

    def goto_theend(self):
        if self.examination():
            self.quiz_window = THeEnd()
            self.quiz_window.show()
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
            QRadioButton {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """


class THeEnd(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The End!")
        self.setFixedSize(480, 480)
        self.pixmap = QPixmap('quiz.jpg')
        self.scaled_pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)
        self.label_image = QLabel(self)
        self.label_image.setPixmap(self.scaled_pixmap)
        self.label_image.setGeometry(0, 0, self.width(), self.height())




        self.question_one = QLabel("THe End!!!", self)
        self.font(self.question_one, 100, 10)
        self.question_one.setFixedSize(220, 50)


        self.question_one = QLabel("thankyou participating 😁", self)
        self.font(self.question_one, 5, 100)
        


      

        self.notworth = QPushButton("Not Worth it!", self)
        self.font(self.notworth, 100, 420)
        self.notworth.clicked.connect(self.stop)
        


        
        self.setStyleSheet(self.style())
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 20))
        obj.move(x, y)
    
    def stop(self):
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
            QRadioButton {
                background-color: white;
                color: #213D44;
                border: 4px solid black;
                border-radius: 10px;
            }
        """

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = One()
    sys.exit(app.exec_())

