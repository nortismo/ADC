from __future__ import print_function
import datetime

from pyrfc3339 import generate, parse

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
from util.models import AppointmentDTO

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def authenticate():
    store = file.Storage('../Configs/token_prod.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('../Configs/credentials_prod.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return build('calendar', 'v3', http=creds.authorize(Http()))

def fetchCalendarAppointements(calService, startDate : datetime, endDate : datetime):
    start = startDate.isoformat() + 'Z'  # 'Z' indicates UTC time
    end = endDate.isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = calService.events().list(calendarId='primary', timeMin=start, timeMax=end,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()

    return events_result.get('items', [])


def googleAppointmentsToDTO(googleAppointments):
    appointmentDTO = []
    for appointment in googleAppointments:
        if appointment['start'].get('dateTime'):
            start = parse(appointment['start'].get('dateTime'))
        else:
            start = datetime.datetime.strptime(appointment['start'].get('date'), "%Y-%m-%d")

        if appointment['end'].get('dateTime'):
            end = parse(appointment['start'].get('dateTime'))
        else:
            end = datetime.datetime.strptime(appointment['end'].get('date'), "%Y-%m-%d")

        appointmentDTO.append(AppointmentDTO(appointment['id'],start , end, appointment['summary']))
    return appointmentDTO

def main():
    calService = authenticate()
    utcNow = datetime.datetime.utcnow()
    todayStart = datetime.datetime(utcNow.year, utcNow.month, utcNow.day, 0, 0, 0)
    todayEnd = datetime.datetime(utcNow.year, utcNow.month, utcNow.day, 23, 59, 59)
    googleAppointments = fetchCalendarAppointements(calService, todayStart, todayEnd)

    if not googleAppointments:
        print('No upcoming events found.')
    else:
        appointmentDTOs = googleAppointmentsToDTO(googleAppointments)
        print(appointmentDTOs)

if __name__ == '__main__':
        main()