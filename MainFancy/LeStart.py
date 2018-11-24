from CalendarStuff import Calendar

def main():

    calendar = Calendar()
    calendarDTO = calendar.get_calendarEntries()
    print('calendar name: ' + calendarDTO.calendarName + ', calendarUID: ' + calendarDTO.uid)


if __name__ == '__main__':
    main()