from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        self.setWindowTitle('Hello World')
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('This is default text')
        self.main_text.adjustSize()

        self.button = QtWidgets.QPushButton(self)
        self.button.setText('Click me')
        self.button.move(50, 50)
        self.button.setFixedWidth(200)
        self.button.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText('Button has clicked')


def run_application():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()

    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_application()
