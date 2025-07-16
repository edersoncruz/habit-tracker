from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton
from PySide6.QtWidgets import QPushButton
import matplotlib.pyplot as plt
from utils.get_json import datas, values
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GridWindow(QWidget):
    def __init__(self, stack, parent=None):
        super().__init__(parent)
        self.stack = stack

        # Layout em grade
        self.grid_layout = QGridLayout(self)
        self.setLayout(self.grid_layout)

        # Criação da figura do Matplotlib embutida
        self.figure = Figure(figsize=(7, 2.5))
        self.canvas = FigureCanvas(self.figure)
        self.plot_graph(datas, values)

        # Adiciona o gráfico à grid (linha 0, coluna 0, ocupando 1 linha e 2 colunas)
        self.grid_layout.addWidget(self.canvas, 0, 0, 1, 2)

        # Botão para voltar ao menu inicial
        button_back = QPushButton("Voltar ao menu Inicial")
        button_back.clicked.connect(self.back_initial_menu)
        self.grid_layout.addWidget(button_back, 1, 0, 1, 2)  # abaixo do gráfico

        self.setWindowTitle("Tela em Grade")

    def plot_graph(self, datas, values):
        ax = self.figure.add_subplot(111)
        ax.plot(datas, values, marker='o', linestyle='-', color='blue')
        ax.axhline(y=11, color='red', linestyle='--', label='Meta (11)')
        ax.set_title("Hábitos ao longo do tempo")
        ax.set_xlabel("Data")
        ax.set_ylabel("Valor")
        ax.grid(True)
        self.figure.tight_layout()

    def back_initial_menu(self):
        self.stack.setCurrentIndex(0)

