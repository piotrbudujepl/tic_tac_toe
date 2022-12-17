import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs
import QtQml

ColumnLayout {

    ToolBar {
        Layout.fillWidth: true

            Button {
                text: "New Game"
                onClicked: {
                    console.log("New game")
                }
            }            

    }
    GridLayout {
        Layout.fillWidth: true
        Layout.fillHeight: true
        rows: 3
        columns: 3
        Button {
            text: ""
            implicitWidth: 100
            implicitHeight: 100
        }
        Button {
            text: ""
            implicitWidth: 100
            implicitHeight: 100
        }
        Button {
            text: ""
            implicitWidth: 100
            implicitHeight: 100
        }
        Button {
            text: ""
            implicitWidth: 100
            implicitHeight: 100
        }
        Button {
            text: ""
            implicitWidth: 100
            implicitHeight: 100
        }
        Button {
            text: ""
            implicitWidth: 100
            implicitHeight: 100
        }
        Button {
            text: ""
            implicitWidth: 100
            implicitHeight: 100
        }
        Button {
            text: ""
            implicitWidth: 100
            implicitHeight: 100
        }
        Button {
            text: ""
            implicitWidth: 100
            implicitHeight: 100
        }

    }    
}
