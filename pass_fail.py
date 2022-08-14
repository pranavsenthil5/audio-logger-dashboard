import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class PassFail(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Pass Fail')

        self.layout = QVBoxLayout()
        self.btn_pass = QPushButton('Pass')
        self.btn_fail = QPushButton('Fail')
        self.layout.addWidget(self.btn_pass)
        self.layout.addWidget(self.btn_fail)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PassFail()
    ex.show()
    sys.exit(app.exec())
