import datetime

from CalendarStuff import Calendar
from TextStuff.googleCloudVision import detectTextInImage
from util.models import AppointmentDTO


def main():

    #result = detectTextInImage("../TestData/kaffee.png")
    #print(result)

    calendar = Calendar()

    start = datetime.datetime.now() #astimezone = to utc
    end = datetime.datetime.now() + datetime.timedelta(hours=1)
    calendar.createAppointments(start, end, 'Get Coffee because of sleepy')

    calendarEntries = calendar.get_calendarEntries()
    for appointment in calendarEntries:
        print(appointment.toString())

if __name__ == '__main__':
    main()