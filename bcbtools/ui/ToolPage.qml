import QtQuick 2.9
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Window 2.3
import QtQuick.Controls.Styles 1.4
import QtQuick.Controls.Material 2.3

Page {

    property string seed
    property string prvk
    property string pubk
    property string addr

    Button {
        text: "Generate"
        onClicked: {
//            result = proxy.create_genesis(prvk);
        }
    }

}
