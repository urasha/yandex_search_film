import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5 import uic
import sqlite3


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('films.ui', self)

        con = sqlite3.connect('films_db.sqlite')
        self.cur = con.cursor()

        self.comboBox.addItems(('Продолжительность', 'Название', 'Год выпуска'))
        self.pushButton.clicked.connect(self.show_result)

    def show_result(self):
        if self.comboBox.currentText() == 'Продолжительность':
            self.REQ = """SELECT * FROM Films WHERE duration=?"""
        elif self.comboBox.currentText() == 'Название':
            self.REQ = """SELECT * FROM Films WHERE title=?"""
        elif self.comboBox.currentText() == 'Год выпуска':
            self.REQ = """SELECT * FROM Films WHERE year=?"""

        try:
            self.result = self.cur.execute(self.REQ, (self.lineEdit.text(),)).fetchall()[0]
            self.lineEdit_2.setText(str(self.result[0]))
            self.lineEdit_3.setText(self.result[1])
            self.lineEdit_4.setText(str(self.result[2]))
            self.lineEdit_5.setText(str(self.result[3]))
            self.lineEdit_6.setText(str(self.result[4]))

        except Exception:
            self.label_6.setText('Ошибка!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
