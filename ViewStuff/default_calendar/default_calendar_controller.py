import datetime
import sys
from PyQt5.QtCore import QObject, QUrl, QByteArray
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QMainWindow, QApplication
from ViewStuff.text_input.text_input_controller import TextInputController

from CalendarStuff import Calendar
from ViewStuff.default_calendar.default_calendar_abstract_model import DefaultCalendarAbstractModel
from ViewStuff.default_calendar.default_calendar_entry_model import DefaultCalendarEntryModel


class DefaultCalendarController(QMainWindow):
    def __init__(self, date: datetime = datetime.datetime.now()):
        super().__init__()
        self.date = date
        self.calendar_data = list()

    def add_event(self):
        controller = TextInputController('philipp', self)

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


    def mapAppointmentDTOToDefaultCalendarEntryModel(self):
        self.calendar_data_first_person
        print('****************')
        for googleAppointment in self.calendar_data_first_person.appointments:

            appointment_index = googleAppointment.start.hour

            nativeStart = googleAppointment.start.replace(tzinfo=None)
            nativeEnd = googleAppointment.end.replace(tzinfo=None)



            firstPersString = self.first_persons_column[appointment_index].set_data(
                googleAppointment.uid, nativeStart,nativeEnd, googleAppointment.description
            )

            print(self.calendar_data)
            #self.calendar_data.append({
            #    QByteArray(str.encode("hour")): str(appointment_index) + ":00",
            #    QByteArray(str.encode("firstPerson")): firstPersString,
            #    QByteArray(str.encode("secondPerson")): '-',
            #})

            # self.calendar_data.items[appointment_index] = firstPersString
            print('desc after set_data: ' + self.first_persons_column[appointment_index].description)
            print('****************')

    def prepare_calendar(self):
        schema = [
            QByteArray(str.encode("hour")),
            QByteArray(str.encode("firstPerson")),
            QByteArray(str.encode("secondPerson")),
        ]

        self.calendar_data = DefaultCalendarAbstractModel(schema)

        self.first_persons_column = list()
        self.second_person_column = list()

        # Prepare empty cells
        self.firstPersonList = list()
        self.secondPersonList = list()

        # Prepare data from Google Cal
        calendar = Calendar()
        calendar = calendar.get_calendarEntries("philipp")
        print('getting calendar entries')
        for appointment in calendar.appointments:
            print(appointment.toString())
        self.calendar_data_first_person = calendar

        # Prepare second user data from Google Cal
        calendar = Calendar()
        calendar = calendar.get_calendarEntries("carla")
        print('getting calendar entries')
        for appointment in calendar.appointments:
            print(appointment.toString())
        self.calendar_data_second_person = calendar

        for x in range(0, 24):
            # wenn zu dieser Uhrzeit kein Termin ansteht, das da verwenden:
            # noAppointmentString = DefaultCalendarEntryModel(datetime.datetime(self.date.year, self.date.month, self.date.day, x, 0), datetime.datetime(self.date.year, self.date.month, self.date.day, x, 59))

            # firstPerson aus Google Cal durchloopen und DefaultCalendarEntryModel.set_data abfüllen
            cell = DefaultCalendarEntryModel(datetime.datetime(self.date.year, self.date.month, self.date.day, x, 0),datetime.datetime(self.date.year, self.date.month, self.date.day, x, 59))

            for googleAppointment in self.calendar_data_first_person.appointments:
                appointment_index = googleAppointment.start.hour
                if x is appointment_index:
                    nativeStart = googleAppointment.start.replace(tzinfo=None)
                    nativeEnd = googleAppointment.end.replace(tzinfo=None)

                    defaultCalEntryModel = DefaultCalendarEntryModel(datetime.datetime(self.date.year, self.date.month ,self.date.day, x, 0), datetime.datetime(self.date.year, self.date.month, self.date.day, x, 59))
                    firstPersString = defaultCalEntryModel.set_data(googleAppointment.uid, nativeStart, nativeEnd, googleAppointment.description)

                    # set_data(googleAppointment.uid, nativeStart, nativeEnd, googleAppointment.description)
                    self.firstPersonList.append(firstPersString)
                else:
                    self.firstPersonList.append(cell.full_text)
            for googleAppointment in self.calendar_data_second_person.appointments:
                appt_index = googleAppointment.start.hour
                if x is appt_index:
                    nativeStart = googleAppointment.start.replace(tzinfo=None)
                    nativeEnd = googleAppointment.end.replace(tzinfo=None)

                    defaultCalEntryModel = DefaultCalendarEntryModel(
                        datetime.datetime(self.date.year, self.date.month, self.date.day, x, 0),
                        datetime.datetime(self.date.year, self.date.month, self.date.day, x, 59))
                    secondPersonString = defaultCalEntryModel.set_data(googleAppointment.uid, nativeStart, nativeEnd,
                                                                    googleAppointment.description)

                    # set_data(googleAppointment.uid, nativeStart, nativeEnd, googleAppointment.description)
                    self.secondPersonList.append(secondPersonString)
                else:
                    self.secondPersonList.append(cell.full_text)

            # secondPerson aus Google Cal durchloopen und DefaultCalendarEntryModel.set_data abfüllen
            # self.secondPersonList.append(cell.full_text)

            # Hier dann calendar_data mit QByteArrays füllen
            self.calendar_data.append({
                QByteArray(str.encode("hour")): str(x) + ":00",
                QByteArray(str.encode("firstPerson")): self.firstPersonList[x],
                QByteArray(str.encode("secondPerson")): self.secondPersonList[x],
            })
        print(str(len(self.firstPersonList)))


      # #  for x in range(0, 24):
      #      cell = DefaultCalendarEntryModel(datetime.datetime(self.date.year, self.date.month ,self.date.day, x, 0), datetime.datetime(self.date.year, self.date.month, self.date.day, x, 59))
      #      self.first_persons_column.append(cell)
      #      self.second_person_column.append(cell)

      #      self.calendar_data.append({
      #          QByteArray(str.encode("hour")): str(x) + ":00",
      #          QByteArray(str.encode("firstPerson")): cell.full_text,
      #          QByteArray(str.encode("secondPerson")): cell.full_text,
      #      })
      #  print('prepared calendar')
      #  #



        # #Prepare data from Google Cal
        # calendar = Calendar()
        # calendar = calendar.get_calendarEntries("philipp")
        # print('getting calendar entries')
        # for appointment in calendar.appointments:
        #     print(appointment.toString())
        # self.calendar_data_first_person = calendar
#
        # self.mapAppointmentDTOToDefaultCalendarEntryModel()
        # print('fetched calendar for first Person')



# This main is just for development. The main process should be started somewhere else, out of the GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = DefaultCalendarController()
    engine = controller.start_default_calendar()
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
