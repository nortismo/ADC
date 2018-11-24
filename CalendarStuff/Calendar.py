import time

from CalendarStuff import GoogleCalendar
from util.models import CalendarDTO, AppointmentDTO
from datetime import datetime


class Calendar:
    def __init__(self):
        self.calendarDTO = CalendarDTO('calendarNameFromConstructor', self.createAppointments())

    def get_calendarEntries(self, date=None):
        if date:
            return self.get_calendarEntries(date)
        else:
            return GoogleCalendar.get_calendarEntries(datetime.utcnow())


    def createAppointments(self):
        datetime
        start = datetime.now()
        end = datetime.now()
        print(start)
        print(end)
        appointmentMonday = AppointmentDTO(start, end, 'Get Coffee because of sleepy')
        appointmentTuesday = AppointmentDTO(start, end, 'Get more Coffee because of supersleepy')
        appointmentFriday = AppointmentDTO(start, end, 'Get even more Coffee because of nearly dead')

        list = [appointmentMonday, appointmentTuesday, appointmentFriday]
        return list