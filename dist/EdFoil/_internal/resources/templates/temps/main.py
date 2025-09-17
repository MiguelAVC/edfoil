from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
import sys

# The app variable is the wrapper
app = QApplication(sys.argv)

window = ButtonHolder()

window.show()

# Starts the event loop
app.exec()