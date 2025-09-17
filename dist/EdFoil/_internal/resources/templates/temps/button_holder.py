from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget

class ButtonHolder(QMainWindow):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.setWindowTitle('TidEd Blade')
        button = QPushButton('Press Me!')
        
        # Set up the button as our central widget
        self.setCentralWidget(button)