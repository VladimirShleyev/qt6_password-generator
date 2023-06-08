import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from random import choices


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)
        self.clean.clicked.connect(self.reset)
        self.generate.clicked.connect(self.gen)

    def gen(self):
        digit = '1234567890'
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        alphabet_upper = alphabet.upper()
        symbol = '!@#$%^&*()_<>?/|§'
        line = ''
        if self.digits.isChecked():
            line += digit
        if self.alphabet.isChecked():
            line += alphabet + alphabet_upper
        if self.symbols.isChecked():
            line += symbol
        data = []
        for elem in range(self.count_pwd.value()):
            data.append(''.join(choices(line, k=self.count_symbols.value())))
        fname = QFileDialog.getSaveFileName(self, 'сохранить', '/passwords.txt')[0]
        with open(fname, 'w') as f:
            for elem in data:
                f.write(elem)
                f.write('\n')


    def reset(self):
        self.count_pwd.setValue(0)
        self.count_symbols.setValue(0)
        self.digits.setChecked(False)
        self.alphabet.setChecked(False)
        self.symbols.setChecked(False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
