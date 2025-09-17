from PySide6.QtWidgets import (
    QWidget, QCalendarWidget, QStackedWidget, QGridLayout, QPushButton)
from PySide6.QtCore import QLocale, Qt
import matplotlib.pyplot as plt
from utils.get_json import get_json_data

class CalendarioWidget(QWidget):
    def __init__(self, stack, parent=None):
        super().__init__(parent)
        self.stack = stack
        self.v_layout = QGridLayout(self)

        # Calendário para navegação
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)  # Mostra a grade do calendário
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setHorizontalHeaderFormat(
            QCalendarWidget.SingleLetterDayNames)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setSelectedDate(self.calendar.selectedDate())
        self.calendar.setStyleSheet(
            "QCalendarWidget { background-color: #f0f0f0; }")
        self.v_layout.addWidget(self.calendar, 0, 0, 1, 1)
        self.calendar.setFocusPolicy(Qt.StrongFocus)
        self.calendar.setFocus()
        self.calendar.installEventFilter(self)

        # Calendário em português
        self.calendar.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))

        # Botão para abrir relatórios mensal
        button_grid = QPushButton("Gráfico Mensal")
        button_grid.clicked.connect(self.open_grid_window)
        self.v_layout.addWidget(button_grid)
        button_grid.setFixedHeight(30)
        
        # Botão para abrir gráfico geral
        button_general_grid = QPushButton("Gráfico Anual")
        button_general_grid.clicked.connect(self.open_grid_window_general)
        self.v_layout.addWidget(button_general_grid)
        button_general_grid.setFixedHeight(30)

        # Abrir nova tela ao clicar em um dia
        self.calendar.clicked.connect(
            lambda date: self.open_habbits_window(date, stack))

    def open_habbits_window(self, date, stack: QStackedWidget):
        habbits_widget = stack.widget(1)
        habbits_widget.set_date(date)
        stack.setCurrentIndex(1)

    def open_grid_window(self):
        grid_window = self.stack.widget(2)  # índice 2 é a GridWindow
        grid_window.refresh()               # chama o método que atualiza o gráfico
        self.stack.setCurrentIndex(2)       # muda para a tela do gráfico

    def open_grid_window_general(self):
        datas, values = get_json_data(360)
        fig, ax1 = plt.subplots(figsize=(8, 4))  # apenas um gráfico

        # Gráfico de linha
        ax1.plot(datas, values, marker='.', linestyle='-', color='blue')
        ax1.set_title("Hábitos ao longo do tempo - Ano")
        ax1.set_xlabel("Data")
        ax1.set_ylabel("Valor")
        ax1.grid(True)
        ax1.legend()
        ax1.tick_params(axis='x', colors='white')  # cor dos ticks + labels do eixo X
        plt.tight_layout()
        plt.show()