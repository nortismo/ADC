import datetime

from CalendarStuff import Calendar
from TextStuff.GoogleCloudVision import GoogleCloudVision


def main():
    googleCloudVision = GoogleCloudVision()
    result = googleCloudVision.detectTextInImage("../TestData/kaffee.png")
    print(result)

    calendar = Calendar()

    start = datetime.datetime.now()
    end = datetime.datetime.now() + datetime.timedelta(hours=1)
    calendar.createAppointment(start, end, 'Get Coffee because of sleepy')

    calendarEntries = calendar.get_calendarEntries()
    for appointment in calendarEntries:
        print(appointment.toString())


if __name__ == '__main__':
    main()
