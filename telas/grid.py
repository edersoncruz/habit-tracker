from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton
from PySide6.QtWidgets import QPushButton
import matplotlib.pyplot as plt
from utils.get_json import get_json_data
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator

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
        datas, values = get_json_data(30)
        self.plot_graph(datas, values)

        # Adiciona o gráfico à grid (linha 0, coluna 0, ocupando 1 linha e 2 colunas)
        self.grid_layout.addWidget(self.canvas, 0, 0, 1, 2)

        # Botão para voltar ao menu inicial
        button_back = QPushButton("Voltar")
        button_back.clicked.connect(self.back_initial_menu)
        self.grid_layout.addWidget(button_back, 1, 0, 1, 2)  # abaixo do gráfico
        button_back.setFixedHeight(30)
        self.setWindowTitle("Tela em Grade")

    def plot_graph(self, datas, values):
        # Ajusta datas para mostrar só mês-dia
        for d in datas:
            so_dia_mes = "-".join(d.split("-")[1:])
            datas[datas.index(d)] = so_dia_mes

        ax = self.figure.add_subplot(111)

        # Fundo escuro
        self.figure.patch.set_facecolor("#1e1e1e")
        ax.set_facecolor("#1e1e1e")

        # Linha principal
        ax.plot(datas, values, marker='.', linestyle='-', color='white')

        # Grid claro sobre fundo escuro
        ax.grid(True, color="#444444")

        # Títulos e rótulos em branco
        ax.set_title("Hábitos ao longo do tempo - Mês", color="white")
        ax.set_xlabel("Data", color="white")
        ax.set_ylabel("Valor", color="white")

        # Estilo dos ticks
        ax.tick_params(axis='x', rotation=80, colors="white")
        ax.tick_params(axis='y', colors="white")

        # Limites
        ax.set_ylim(bottom=0)
        ax.yaxis.set_major_locator(MultipleLocator(2))

        self.figure.tight_layout()


    def back_initial_menu(self):
        self.stack.setCurrentIndex(0)

    def refresh(self):
        datas, values = get_json_data(30)
        self.figure.clear()  # Limpa o gráfico antigo
        self.plot_graph(datas, values)
        self.canvas.draw()   # Redesenha no canvas


