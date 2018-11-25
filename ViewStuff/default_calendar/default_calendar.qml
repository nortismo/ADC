import QtQuick 2.0
import QtQuick.Controls 2.3

ApplicationWindow {
    id: root
    width: 384
    height: 600
    color: "#8C8A91"
    visible: true


    ListView {
        clip: true

        model: calendarData  //TODO: CHANGE!
        anchors.fill: parent

        width: parent.width
        //TODO: Change layout
        height: 10
        delegate: Row {
            Column {
                Text{
                    width: 44
                    text: hour
                }
            }
            Column {
                Text{
                    width: 170
                    text: firstPerson
                }
            }
            Column {
                Text{
                    width: 170
                    text: secondPerson
                }
            }
            spacing: 10
        }
    }
}