from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox

class HabitsWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Aqui você pode adicionar seus hábitos."))
        layout.addWidget(QCheckBox("Estudar"))
        layout.addWidget(QCheckBox("Exercitar-se"))
        layout.addWidget(QCheckBox("Ler um livro"))
        layout.addWidget(QCheckBox("Ler as escrituras"))

        self.resize(300, 300)  # Largura: 400px, Altura: 300px
        self.move(500, 100)    # Posição na tela: X=100px, Y=100p
        

        self.setLayout(layout)
