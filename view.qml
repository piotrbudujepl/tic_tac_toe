import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs
import QtQml

ColumnLayout {
    Popup {
        property alias text: messageText.text
        id: messageDialog
        modal: true
        focus: true
        anchors.centerIn: Overlay.overlay
        ColumnLayout {
            anchors.fill: parent
            Text {
                id: messageText
                Layout.fillWidth: true
            }
            Button {
                Layout.alignment: Qt.AlignHCenter
                text: "Ok"
                onClicked: {
                    messageDialog.close()
                }
            }
        }
    }
    Connections {
        target: controller
        function onGame_ended(message) {
            console.log(message)
            messageDialog.text = message
            messageDialog.open()
        }
    }

    ToolBar {
        Layout.fillWidth: true

        Button {
            text: "New Game"
            onClicked: {
                controller.start_new_game()
            }
        }
    }
    Text {
        text: "Current player: " + model.current_player
    }
    GridLayout {
        Layout.fillWidth: true
        Layout.fillHeight: true
        rows: 3
        columns: 3
        Button {
            text: model.field_0_0
            implicitWidth: 100
            implicitHeight: 100
            onClicked: function () {
                controller.move(0, 0)
            }
        }
        Button {
            text: model.field_0_1
            implicitWidth: 100
            implicitHeight: 100
            onClicked: function () {
                controller.move(0, 1)
            }
        }
        Button {
            text: model.field_0_2
            implicitWidth: 100
            implicitHeight: 100
            onClicked: function () {
                controller.move(0, 2)
            }
        }
        Button {
            text: model.field_1_0
            implicitWidth: 100
            implicitHeight: 100
            onClicked: function () {
                controller.move(1, 0)
            }
        }
        Button {
            text: model.field_1_1
            implicitWidth: 100
            implicitHeight: 100
            onClicked: function () {
                controller.move(1, 1)
            }
        }
        Button {
            text: model.field_1_2
            implicitWidth: 100
            implicitHeight: 100
            onClicked: function () {
                controller.move(1, 2)
            }
        }
        Button {
            text: model.field_2_0
            implicitWidth: 100
            implicitHeight: 100
            onClicked: function () {
                controller.move(2, 0)
            }
        }
        Button {
            text: model.field_2_1
            implicitWidth: 100
            implicitHeight: 100
            onClicked: function () {
                controller.move(2, 1)
            }
        }
        Button {
            text: model.field_2_2
            implicitWidth: 100
            implicitHeight: 100
            onClicked: function () {
                controller.move(2, 2)
            }
        }
    }
}
