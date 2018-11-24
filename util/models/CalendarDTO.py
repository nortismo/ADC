import random
import string
from datetime import datetime

class CalendarDTO:
    calendarName = "filp"
    appointments = ["AppointmentDTO1"]

    def __init__(self, calendarName = None, appointments = None):
        now = str(datetime.now())
        self.uid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        self.calendarName = calendarName
        self.appointments = appointments

        if calendarName == None:
            self.calendarName = 'no description yet'

        if self.appointments == None:
            self.appointments = 'blö'


    # def toString(self):
    #     print('printing CalendarDTO')