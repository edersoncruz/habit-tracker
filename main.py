import sys
from PySide6.QtGui import QIcon
from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from variables import WINDOW_ICON_PATH


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o Icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    # Executa Tudo
    window.show()
    app.exec()
