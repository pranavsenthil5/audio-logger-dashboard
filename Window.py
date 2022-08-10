from PyQt5.QtWidgets import QMainWindow, QToolBar, QStatusBar


class Window(QMainWindow):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)

        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _addCentralWidget(self, widget):
        self.setCentralWidget(widget)

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)
