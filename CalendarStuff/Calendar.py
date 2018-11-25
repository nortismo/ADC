from CalendarStuff.GoogleCalendar import GoogleCalendar
from util.models import AppointmentDTO
from datetime import datetime


class Calendar:
    def get_calendarEntries(self, userName, date=None):
        if date:
            googleCalendar = GoogleCalendar(userName)
            return googleCalendar.get_calendarEntries(date)
        else:
            return self.get_calendarEntries(userName, datetime.utcnow())

    def createAppointment(self, userName, start: datetime, end: datetime, description):
        googleCalendar = GoogleCalendar(userName)
        googleCalendar.createAppointment(AppointmentDTO(None, start, end, description))

    def createAppointmentFromDTO(self, userName, appointmentDTO: AppointmentDTO):
        googleCalendar = GoogleCalendar(userName)
        googleCalendar.createAppointment(appointmentDTO)
