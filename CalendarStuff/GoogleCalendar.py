from __future__ import print_function

import datetime

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pyrfc3339 import parse

from util.models import CalendarDTO
from util.models.AppointmentDTO import AppointmentDTO


class GoogleCalendar:
    # If modifying these scopes, delete the file token.json.
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    googleCalendarAPI = None

    def __init__(self, userName):
        self.googleCalendarAPI = self.__authenticate(userName)

    def createAppointment(self, appointmentDTO: AppointmentDTO):
        self.__insertNewCaledarAppointment(self.__appointmentDTOTogoogleAppointment(appointmentDTO))

    def get_calendarEntries(self, date):
        todayStart = datetime.datetime(date.year, date.month, date.day, 0, 0, 0)
        todayEnd = datetime.datetime(date.year, date.month, date.day, 23, 59, 59)
        googleCalendar = self.__fetchCalendarAppointements(todayStart, todayEnd)

        calendarDTO = CalendarDTO()

        if googleCalendar.get('description'):
            calendarDTO.calendarName = googleCalendar['description']
        else:
            calendarDTO.calendarName = googleCalendar['summary']
            print("please add a description to your calendar")

        appointmentDTOs = None
        googleAppointments = googleCalendar.get('items', [])
        if not googleAppointments:
            print('No upcoming events found.')
        else:
            appointmentDTOs = self.__googleAppointmentsToDTO(googleAppointments)
        calendarDTO.appointments = appointmentDTOs
        return calendarDTO


    def __authenticate(self, userName):
        store = file.Storage('../../Configs/token_' + userName + '_prod.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('Configs/credentials_calapi_prod.json', self.SCOPES)
            creds = tools.run_flow(flow, store)
        return build('calendar', 'v3', http=creds.authorize(Http()))

    def __fetchCalendarAppointements(self, startDate: datetime, endDate: datetime):
        start = startDate.isoformat() + 'Z'  # 'Z' indicates UTC time
        end = endDate.isoformat() + 'Z'  # 'Z' indicates UTC time

        events_result = self.googleCalendarAPI.events().list(calendarId='primary', timeMin=start, timeMax=end,
                                                             maxResults=100, singleEvents=True,
                                                             orderBy='startTime').execute()

        return events_result

    def __insertNewCaledarAppointment(self, appointment):
        event = self.googleCalendarAPI.events().insert(calendarId='primary', body=appointment).execute()

    def __googleAppointmentsToDTO(self, googleAppointments):
        appointmentDTO = []
        for appointment in googleAppointments:
            if appointment['start'].get('dateTime'):
                start = parse(appointment['start'].get('dateTime'))
            else:
                start = datetime.datetime.strptime(appointment['start'].get('date'), "%Y-%m-%d")

            if appointment['end'].get('dateTime'):
                end = parse(appointment['end'].get('dateTime'))
            else:
                end = datetime.datetime.strptime(appointment['end'].get('date'), "%Y-%m-%d")

            appointmentDTO.append(AppointmentDTO(appointment['id'], start, end, appointment['summary']))
        return appointmentDTO

    def __appointmentDTOTogoogleAppointment(self, appointmentDTO: AppointmentDTO):
        json = {
            "summary": appointmentDTO.description,
            "start": {
                'dateTime': appointmentDTO.start.astimezone().isoformat()  # 'Z' indicates UTC time
            },
            "end": {
                'dateTime': appointmentDTO.end.astimezone().isoformat()  # 'Z' indicates UTC time
            }
        }

        return json
