import QtQuick 2.0
import QtQuick.Controls 1.0

ApplicationWindow {
    id: root
    width: 384
    height: 600
    visible: true

    Rectangle {
        width: 384
        height: 600


        Rectangle {
            id: title_rectangle
            anchors.top: parent.top
            anchors.topMargin: 10
            width: parent.width
            height: 35
            color: "#00000000"
            border.width: 0
            Text {
                id: date_title
                width: parent.width
                height: 20
                text: "Today"
                horizontalAlignment: Text.AlignHCenter
                font.pointSize: 12
                font.bold: true
            }
            Button {
                id: createEvent
                objectName: "createEvent"
                text: "Create Event"
                anchors.top: date_title.top
                anchors.right: title_rectangle.right
                anchors.rightMargin: 20
                transformOrigin: Item.Top
            }
        }

        Rectangle {
            id: header_rectangle
            anchors.top: title_rectangle.bottom
            width: parent.width
            height: 15
            color: "#00000000"
            border.width: 0
            Text {
                id: header_time
                width: 50
                text: ""
                font.pointSize: 10
                font.bold: true
            }
            Text {
                id: header_first
                anchors.left: header_time.right
                width: 167
                text: "Michi's Kalender"
                font.pointSize: 10
                font.bold: true
            }
            Text {
                id: header_second
                anchors.left: header_first.right
                width: 167
                text: "Philipp's Kalender"
                font.pointSize: 10
                font.bold: true
            }
            Rectangle {
                anchors.top: header_time.bottom
                height: 1
                color: "#000000"
                width: parent.width
            }
        }

        ListView {
            clip: true

            model: calendarData  //TODO: CHANGE!
            anchors.top: header_rectangle.bottom
            anchors.bottom: parent.bottom
            anchors.topMargin: 10
            width: parent.width
            delegate: Row {
                        height: 21
                        Column {
                            Text {
                                id: column_hour
                                width: 50
                                text: hour
                                anchors.right: parent.right
                                horizontalAlignment: Text.AlignRight
                                anchors.rightMargin: 5
                            }
                        }
                        Column {
                            id: column_first
                            Text {
                                width: 167
                                text: firstPerson
                                wrapMode: Text.WordWrap
                            }
                        }
                        Column {
                            Text {
                                width: 167
                                text: secondPerson
                                wrapMode: Text.WordWrap
                            }
                        }
            }
        }
    }
}