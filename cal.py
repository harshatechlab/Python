import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basic PyQt5 Calculator')
        self.setFixedSize(320, 400)

        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet('font-size: 24px;')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['(', ')', '⌫', '=']
        ]

        grid = QGridLayout()
        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                btn = QPushButton(label)
                btn.setFixedSize(70, 60)
                btn.setStyleSheet('font-size: 18px;')
                btn.clicked.connect(lambda _, text=label: self.on_click(text))
                grid.addWidget(btn, r, c)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    def on_click(self, label):
        if label == 'C':
            self.display.setText('0')
            return
        if label == '⌫':
            current = self.display.text()
            if len(current) <= 1:
                self.display.setText('0')
            else:
                self.display.setText(current[:-1])
            return
        if label == '=':
            expression = self.display.text().replace('x', '*').replace('÷', '/')
            try:
                result = str(eval(expression, {}, {}))
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
            return
        if self.display.text() == '0' and label not in ['.', '+', '-', '*', '/', ')']:
            self.display.setText(label)
        else:
            self.display.setText(self.display.text() + label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())