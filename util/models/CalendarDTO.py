import random
import string
from datetime import datetime

from util.models import AppointmentDTO


class CalendarDTO:
    calendarName = None
    appointments = None

    def __init__(self, calendarName=None, appointments=None):
        now = str(datetime.now())
        self.uid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        self.calendarName = calendarName
        self.appointments = appointments

        if calendarName == None:
            self.calendarName = 'no description yet'

        if self.appointments == None:
            self.appointments = AppointmentDTO()

    def toString(self):
        print('---- printing CalendarDTO ----')
        print('uid: ' + self.uid)
        print('calendarName: ' + self.calendarName)

        for appointment in self.appointments:
            appointment.toString()

        # print('appointments: ' + self.appointments)
        print('-------------------------------')
