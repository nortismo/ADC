from CalendarStuff.GoogleCalendar import GoogleCalendar
from util.models import AppointmentDTO
from datetime import datetime


class Calendar:
    def get_calendarEntries(self, date=None):
        if date:
            return self.get_calendarEntries(date)
        else:
            googleCalendar = GoogleCalendar()
            return googleCalendar.get_calendarEntries(datetime.utcnow())

    def createAppointment(self, start: datetime, end: datetime, description):
        googleCalendar = GoogleCalendar()
        googleCalendar.createAppointment(AppointmentDTO(None, start, end, description))
