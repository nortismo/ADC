import datetime

from CalendarStuff import Calendar
from TextStuff.GoogleCloudVision import GoogleCloudVision


def main():
    #googleCloudVision = GoogleCloudVision()
    #result = googleCloudVision.detectTextInImage("../TestData/kaffee.png")
    #print(result)

    calendar = Calendar()

    start = datetime.datetime.now()
    end = datetime.datetime.now() + datetime.timedelta(hours=1)
    calendar.createAppointment("philipp", start, end, 'Get Coffee because of sleepy')

    calendar = calendar.get_calendarEntries("philipp")
    for appointment in calendar.appointments:
        print(appointment.toString())


if __name__ == '__main__':
    main()
