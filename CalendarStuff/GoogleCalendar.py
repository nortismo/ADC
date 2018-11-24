from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def authenticate():
    store = file.Storage('../Configs/token_prod.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('../Configs/credentials_prod.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return build('calendar', 'v3', http=creds.authorize(Http()))

def fetchCalendar(calService, startDate : datetime, endDate : datetime):
    start = startDate.isoformat() + 'Z'  # 'Z' indicates UTC time
    end = endDate.isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = calService.events().list(calendarId='primary', timeMin=start, timeMax=end,
                                        maxResults=100, singleEvents=True,
                                        orderBy='startTime').execute()
    return events_result.get('items', [])

def main():
    calService = authenticate()
    utcNow = datetime.datetime.utcnow()
    todayStart = datetime.datetime(utcNow.year, utcNow.month, utcNow.day, 0, 0, 0)
    todayEnd = datetime.datetime(utcNow.year, utcNow.month, utcNow.day, 23, 59, 59)
    appointments = fetchCalendar(calService, todayStart, todayEnd)


    if not appointments:
        print('No upcoming events found.')
    for event in appointments:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()