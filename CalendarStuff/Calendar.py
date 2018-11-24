import time

from util.models import CalendarDTO, AppointmentDTO
from datetime import datetime


class Calendar:
    def __init__(self):
        self.calendarDTO = CalendarDTO('calendarNameFromConstructor', self.createAppointments())

    def get_calendarEntries(self, date):
        pass

    def get_calendarEntries(self):
        return self.calendarDTO

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
