from PySide6.QtWidgets import QApplication, QWidget
import sys

# The app variable is the wrapper
app = QApplication(sys.argv)

window = QWidget()
window.show()

# Starts the event loop
app.exec()