import datetime

from CalendarStuff import Calendar
from TextStuff.GoogleCloudVision import GoogleCloudVision
from util import ConfigManager


def main():
    confmanager = ConfigManager()
    configuration = confmanager.loadConfig('Configs/config.json')

    #googleCloudVision = GoogleCloudVision()
    #result = googleCloudVision.detectTextInImage("../TestData/kaffee.png")
    #print(result)

    calendar = Calendar()

    start = datetime.datetime.now()
    #end = datetime.datetime.now() + datetime.timedelta(hours=1)
    #calendar.createAppointment(configuration.USERS[0], start, end, 'Get Coffee because of sleepy')

    calendar = calendar.get_calendarEntries(configuration.USERS[0])
    for appointment in calendar.appointments:
        print(appointment.toString())

        calendar = calendar.get_calendarEntries("carla")
        for appointment in calendar.appointments:
            print(appointment.toString())


if __name__ == '__main__':
    main()
