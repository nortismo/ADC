import QtQuick 2.0
import QtQuick.Controls 2.3

ApplicationWindow {
    id: root
    width: 384
    height: 600
    color: "#8C8A91"

    visible: true

    Rectangle {
        id: rectangle
        color: "#00000000"
        anchors.fill: parent
        clip: false

        Text {
            color: "#ffffff"
            anchors.centerIn: parent
            id: myLabel
            text: "Test not done yet"
        }


        Button {
            id: button
            anchors.topMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: myLabel.bottom
            objectName: "myButton"
            text: qsTr("Change text below")

            //Call from QML to python
            onClicked: {
                // call the slot to process the text
                controller.textLabel("Button was clicked, yo!")
            }
        }

        Text {
            color: "#e30505"
            id: textResult
            anchors.top: button.bottom
            text: "This text should change on click."
            anchors.topMargin: 10
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter
        }


        ListView {
            clip: true

            model: pyModel

            anchors.top: textResult.bottom
            anchors.bottom: parent.bottom

            width: parent.width
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

    //Callback from python to QML
    Connections {
        target: controller

        // Signal Handler
        onTextResult: {
            // textLabel - was given through arguments=['textLabel']
            textResult.text = textLabel
        }
    }
}