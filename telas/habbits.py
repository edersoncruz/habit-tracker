from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox

class HabitsWindow(QWidget):
    def __init__(self, main_window, stack, parent=None):
        super().__init__()
        self.main_window = main_window

        self.habbits = QVBoxLayout()
        self.habbits.addWidget(QLabel("Aqui você pode adicionar seus hábitos."))
        self.habbits.addWidget(QCheckBox("Estudar"))
        self.habbits.addWidget(QCheckBox("Exercitar-se"))
        self.habbits.addWidget(QCheckBox("Ler um livro"))
        self.habbits.addWidget(QCheckBox("Ler as escrituras"))

        self.resize(300, 300)  # Largura: 400px, Altura: 300px
        self.move(500, 100)    # Posição na tela: X=100px, Y=100p

        # set layout
        # self.setLayout(self.habbits)
