from PySide6.QtWidgets import QWidget, QCalendarWidget, QLabel, QPushButton
from PySide6.QtCore import QLocale, Qt
from telas.habbits import HabitsWindow  # ajuste o nome conforme seu projeto

class CalendarioWidget(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        # Exemplo de layout, ajuste conforme necessário
        from PySide6.QtWidgets import QGridLayout
        self.v_layout = QGridLayout(self)
        
        # Calendário para navegação
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)  # Mostra a grade do calendário
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setSelectedDate(self.calendar.selectedDate())
        self.calendar.setStyleSheet("QCalendarWidget { background-color: #f0f0f0; }")
        self.v_layout.addWidget(self.calendar, 0, 0, 1, 1)
        self.calendar.setFocusPolicy(Qt.StrongFocus)
        self.calendar.setFocus()
        self.calendar.installEventFilter(self)

        # Calendário em português
        self.calendar.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.calendar.setFirstDayOfWeek(Qt.Monday)

        # Abrir nova tela ao clicar em um dia
        self.calendar.clicked.connect(self.open_new_window)

    def open_new_window(self, date):
        self.habits_widget = HabitsWindow(self.main_window)
        self.habits_widget.show()
