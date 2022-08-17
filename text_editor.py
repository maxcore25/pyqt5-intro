from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog
import sys


class TextEditorWindow(QMainWindow):
    def __init__(self):
        super(TextEditorWindow, self).__init__()

        self.setWindowTitle('Text Editor')
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.create_menu_bar()

    def create_menu_bar(self):
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.file_menu = QMenu('&File', self)
        self.menu_bar.addMenu(self.file_menu)

        # self.open_file = self.file_menu.addMenu('&Open')
        # self.save_file = self.file_menu.addMenu('&Save')

        self.file_menu.addAction('Open', self.call_action)
        self.file_menu.addAction('Save', self.call_action)

    @QtCore.pyqtSlot()
    def call_action(self):
        action = self.sender()
        if action.text().lower() == 'open':
            file_name = QFileDialog.getOpenFileName(self)[0]

            try:
                with open(file_name, 'r') as f:
                    data = f.read()
                    self.text_edit.setText(data)

            except FileNotFoundError:
                text_edit_content = self.text_edit.toPlainText()
                if not text_edit_content:
                    self.text_edit.setText('')

        elif action.text().lower() == 'save':
            file_name = QFileDialog.getSaveFileName(self)[0]

            try:
                with open(file_name, 'w') as f:
                    text_edit_content = self.text_edit.toPlainText()
                    f.write(text_edit_content)

            except FileNotFoundError:
                text_edit_content = self.text_edit.toPlainText()
                if not text_edit_content:
                    self.text_edit.setText('')


def run_application():
    app = QApplication(sys.argv)
    text_editor_window = TextEditorWindow()

    text_editor_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_application()
