import QtQuick 2.9
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Window 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.3


ApplicationWindow  {
    id: window
    visible: true
    width: Screen.width
    height: Screen.height
    minimumHeight: 600
    minimumWidth: 800
    flags: Qt.WindowMaximized | Qt.WindowActive
    Material.theme: Material.Dark

    readonly property FontLoader materialFontIcons: FontLoader {
        source: "resource/materialdesignicons-webfont.ttf"
    }

    property alias seed: seedTf.text

    header: ColumnLayout {
        TextField {
            id: seedTf
            Layout.fillWidth: true
            placeholderText: qsTr("Seed")
            echoMode: TextField.Password
            validator: RegExpValidator { regExp: /[0-9A-Fa-f]+/ }
        }

        TextArea {
            id: result
        }
    }

    Pane {

        Material.theme: Material.Light
        Material.elevation: 2
        id: app_header
        padding: 0

        ToolButton {
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 2
            implicitHeight: 48
            implicitWidth: 48
            padding:0
            font.pointSize: 28
            font.family: materialFontIcons.name
            text: MdiFont.Icon.menu
            onClicked: drawer.open()
        }

        width: parent.width
        height: 50
    }

    SwipeView {
        id: view

    ToolGenesis {

    }


    }

    footer: PageIndicator {
        id: indicator

        count: view.count
        currentIndex: view.currentIndex

        anchors.horizontalCenter: parent.horizontalCenter
    }

    Drawer {
        id: drawer
        height: window.height
        visible: false
        interactive: true

//        ButtonGroup{
//            buttons: column.children
//            onClicked: {
//                for(var i=0; i<buttons.length; i++){
//                    buttons[i].background.color = "white"
//                }
//                button.background.color = "lightgray"
//            }
//        }

        ColumnLayout{
            id: column
            anchors.fill: parent

        }
    }
}
