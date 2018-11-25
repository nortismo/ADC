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

        model: pyModel  //TODO: CHANGE!
        anchors.fill: parent

        width: parent.width
        //TODO: Change layout
        height: 40
        delegate: Row {
            Column {
                Text{
                    width: 40
                    height: 40
                    text: index
                }
            }
            Column {
                Text{
                    width: 40
                    height: 40
                    text: dog
                }
            }
            Column {
                Text{
                    width: 40
                    height: 40
                    text: thirdValue
                }
            }
            spacing: 10
        }
    }
}