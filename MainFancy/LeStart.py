from CalendarStuff import CalendarImpl

def main():

    calendar = CalendarImpl()
    calendarDTO = calendar.get_calendarEntries()
    print('calendar name: ' + calendarDTO.calendarName + ', calendarUID: ' + calendarDTO.uid)


if __name__ == '__main__':
    main()