import datetime
import sys
from PyQt5.QtCore import QObject, QUrl, QByteArray
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QMainWindow, QApplication
from ViewStuff.text_input.text_input_controller import TextInputController
from ViewStuff.default_calendar.default_calendar_abstract_model import DefaultCalendarAbstractModel
from ViewStuff.default_calendar.default_calendar_entry_model import DefaultCalendarEntryModel


class DefaultCalendarController(QMainWindow):
    def __init__(self, date: datetime = datetime.datetime.now()):
        super().__init__()
        self.date = date
        self.calendar_data = list()

    def add_event(self):
        controller = TextInputController('michi', self)

    def start_default_calendar(self):
        self.prepare_calendar()
        engine = QQmlApplicationEngine()
        ctx = engine.rootContext()
        ctx.setContextProperty("controller", self)
        ctx.setContextProperty("calendarData", self.calendar_data)
        engine.load(QUrl('ViewStuff/default_calendar/default_calendar.qml'))
        win = engine.rootObjects()[0]
        btn = win.findChild(QObject, 'createEvent')
        btn.clicked.connect(self.add_event)  # works too
        return engine

    def prepare_calendar(self):
        schema = [
            QByteArray(str.encode("hour")),
            QByteArray(str.encode("firstPerson")),
            QByteArray(str.encode("secondPerson")),
        ]

        self.calendar_data = DefaultCalendarAbstractModel(schema)

        first_persons_column = list()
        second_person_column = list()

        # Prepare empty cells
        for x in range(0, 24):
            cell = DefaultCalendarEntryModel(datetime.datetime(self.date.year, self.date.month ,self.date.day, x, 0), datetime.datetime(self.date.year, self.date.month, self.date.day, x, 59))
            first_persons_column.append(cell)
            second_person_column.append(cell)

            self.calendar_data.append({
                QByteArray(str.encode("hour")): str(x) + ":00",
                QByteArray(str.encode("firstPerson")): cell.full_text,
                QByteArray(str.encode("secondPerson")): cell.full_text,
            })


# This main is just for development. The main process should be started somewhere else, out of the GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = DefaultCalendarController()
    engine = controller.start_default_calendar()
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
