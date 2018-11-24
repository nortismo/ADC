from CalendarStuff import Calendar
from util.models import AppointmentDTO


def main():

    calendar = Calendar()
    calendarDTO = calendar.get_calendarEntries()
    calendarDTO.toString()

    # appDTO = AppointmentDTO()
    # appDTO.toString()


if __name__ == '__main__':
    main()