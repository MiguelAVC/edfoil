import sys
from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QIcon
from resources.uis.mainwindow import MainWindow
from edfoil.utils.dev import resource_path
# os.environ["QT_FONT_DPI"] = "96"


# Set application ID for Windows to enable taskbar grouping and icon display
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('resources/icons/icon.ico')))
    # app.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow(app)
    window.show()

    sys.exit(app.exec())