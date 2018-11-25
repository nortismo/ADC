import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

ApplicationWindow {
    id: root
    width: 384
    height: 600
    color: "#FFFFFF"

    visible: true

    property int xpos
    property int ypos

    ColumnLayout {
        spacing: 2

        Rectangle {
            height: 550
            width: 384
            Canvas {
                id: textInput
                objectName: "textCanvas"
                anchors.fill: parent

                onPaint: {
                    var ctx = getContext('2d')
                    ctx.lineWidth = 2
                    ctx.strokeStyle = color.black

                    ctx.beginPath()
                    ctx.moveTo(xpos, ypos)

                    xpos = mouseInput.mouseX
                    ypos = mouseInput.mouseY

                    ctx.lineTo(xpos, ypos)
                    ctx.stroke()
                }

                MouseArea{
                    id: mouseInput
                    anchors.fill: parent
                    onPressed: {
                        xpos = mouseX
                        ypos = mouseY
                        textInput.requestPaint()
                    }

                    onPositionChanged: {
                        textInput.requestPaint()
                    }
                }

            }
        }

        Button {
            id: finishButton
            objectName: "finishButton"
            Layout.fillWidth: true
            text: "Ok"
        }
    }
}