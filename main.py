import sys
from PySide6.QtGui import QIcon, QPalette, QColor
from main_window import MainWindow
from PySide6.QtWidgets import QApplication

from utils.variables import WINDOW_ICON_PATH


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Paleta escura personalizada
    palette = QPalette()

    # Fundo principal grafite escuro
    palette.setColor(QPalette.Window, QColor(18, 18, 28))
    palette.setColor(QPalette.WindowText, QColor(220, 220, 230))

    # Campos de entrada e áreas de texto
    palette.setColor(QPalette.Base, QColor(25, 25, 40))
    palette.setColor(QPalette.AlternateBase, QColor(30, 30, 50))

    palette.setColor(QPalette.Text, QColor(220, 220, 230))

    # Tooltips
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
    palette.setColor(QPalette.ToolTipText, QColor(10, 10, 10))

    # Botões
    palette.setColor(QPalette.Button, QColor(40, 40, 70))
    palette.setColor(QPalette.ButtonText, QColor(100, 220, 255))

    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))

    # Seleções (ex: texto selecionado)
    palette.setColor(QPalette.Highlight, QColor(0, 170, 255))
    palette.setColor(QPalette.HighlightedText, QColor(10, 10, 10))

    # Placeholders
    palette.setColor(QPalette.PlaceholderText, QColor(150, 150, 150))

    # Aplica a paleta no app
    app.setPalette(palette)
    window = MainWindow()

    # Define o Icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    # Executa Tudo
    window.show()
    app.exec()
