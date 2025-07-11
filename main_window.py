from PySide6.QtWidgets import QStackedWidget, QMainWindow, QWidget, QGridLayout
from telas.calendar import CalendarioWidget
from telas.habbits import HabitsWindow


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

        # Titulo da janela e tamanho
        self.setWindowTitle('Habit Tracker')
        self.resize(400, 300)  
        self.move(500, 100)    

        # Stack para alternar entre telas
        self.stack = QStackedWidget()

        # criando as telas
        self.calendario = CalendarioWidget(self.stack)
        self.habbits = HabitsWindow(self.stack)

        # Adiciona as páginas no stack
        self.stack.addWidget(self.calendario)   # indice 0
        self.stack.addWidget(self.habbits)      # indice 1

        # Inicia com o calendário
        self.stack.setCurrentIndex(0)

        # Adiciona o stack no layout principal
        self.v_layout.addWidget(self.stack, 0, 0, 1, 1)

    def closeEvent(self, event):
        # Salva os hábitos do dia atual antes de fechar
        self.habbits.save_habits_for_date()
        super().closeEvent(event)
