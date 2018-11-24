from CalendarStuff import Calendar
from util.models import AppointmentDTO


def main():

    calendar = Calendar()
    calendarDTO = calendar.get_calendarEntries()
    print('calendar name: ' + calendarDTO.calendarName + ', calendarUID: ' + calendarDTO.uid)

    appDTOTest = AppointmentDTO()
    print('appointment - start: ' + appDTOTest.start + ' end: ' + appDTOTest.end + ' description: ' + appDTOTest.description)


if __name__ == '__main__':
    main()