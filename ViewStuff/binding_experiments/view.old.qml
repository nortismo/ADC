import QtQuick 2.7
import QtQuick.Controls 2.3

ApplicationWindow {
    id: root
    width: 384
    height: 640
    x:0
    y:0

    visible: true

    Text{
        x: 61
        y: 4
        text: "PersonA"
        font.pixelSize: 14
    }
    Text{
        x: 184
        y: 4
        text: "PersonB"
        font.pixelSize: 14
    }
    Rectangle {
        id: lineBeforePersonA
        x: 50
        y: 0
        width: 3
        height: parent.height
        color: "#101313"
    }
    Rectangle {
        id: lineBeforePersonB
        x: 171
        y: 0
        width: 3
        height: parent.height
        color: "#0b0e0f"
    }
    Grid {
        id: grid
        width: 400
        height: 400
        Row {
            id: row8Uhr
            width: grid.width
            height: 20
            y: horizontalRectangle.x + horizontalRectangle.height
            Column{
                id: row8UhrColZeit
                height: parent.height
                width: lineBeforePersonA.x
                y: row8Uhr.y
                Text{
                    text: qsTr("08:00")
                    horizontalAlignment: Text.AlignHCenter
                    font.pixelSize: 12
                }
            }
            Column{
                id: row8UhrColPersA
                height: parent.height
                width: lineBeforePersonB - (lineBeforePersonA.x + lineBeforePersonA.width)
                y: lineBeforePersonA.x + lineBeforePersonA.width
                Text{
                    text: qsTr("Termintext Pers. A")
                    horizontalAlignment: Text.AlignLeft
                    font.pixelSize: 12
                }
            }
            /*
            Column{
                id: row8UhrColPersA
                height: row8Uhr.height
                width: 79
                x: 90
                y: row8Uhr.y
                Text{
                    x: 79
                    text: qsTr("Eintrag für Person A")
                    horizontalAlignment: Text.AlignLeft
                    font.pixelSize: 12
                }
            }*/
        }
    }
    Rectangle {
        id: horizontalRectangle
        x: 0
        y: 25
        width: 384
        height: 3
        color: "#000000"
    }
}