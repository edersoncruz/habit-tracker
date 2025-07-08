from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QCalendarWidget, QLineEdit
from PySide6.QtCore import Qt, QLocale
from telas.calendar import CalendarioWidget
from PySide6.QtGui import QKeyEvent

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando layout basico
        self.cw = QWidget()
        self.v_layout = QGridLayout()
        self.v_layout.setVerticalSpacing(0)
        self.v_layout.setHorizontalSpacing(0)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.cw.setLayout(self.v_layout)

        self.setCentralWidget(self.cw)

        # Titulo da janela
        self.setWindowTitle('Habit Tracker')

        # Ajustando o tamanho da janela
        self.resize(300, 300)  # Largura: 400px, Altura: 300px
        self.move(500, 100)    # Posição na tela: X=100px, Y=100p

        # Calendário para navegação chama telas/calendar.py
        self.calendario = CalendarioWidget(self)
        self.v_layout.addWidget(self.calendario, 0, 0, 1, 1)
