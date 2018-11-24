from CalendarStuff import GoogleCalendar
from util.models import CalendarDTO, AppointmentDTO
from datetime import datetime, timedelta

class Calendar:
    def get_calendarEntries(self, date=None):
        if date:
            return self.get_calendarEntries(date)
        else:
            return GoogleCalendar.get_calendarEntries(datetime.utcnow())

    def createAppointments(self, start : datetime, end : datetime, description):
        GoogleCalendar.createAppointment(AppointmentDTO(None, start, end, description))