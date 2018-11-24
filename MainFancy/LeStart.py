from CalendarStuff import Calendar
from util.models import AppointmentDTO


def main():

    calendar = Calendar()
    calendarEntries = calendar.get_calendarEntries()

    for appointment in calendarEntries:
        print(appointment.toString())



if __name__ == '__main__':
    main()