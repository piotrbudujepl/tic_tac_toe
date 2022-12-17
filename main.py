import sys
from pathlib import Path

from PySide6.QtCore import QUrl, qInstallMessageHandler
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView

from controller import controller


def qt_message_handler(mode, context, message):
    print(mode, context, message)


qInstallMessageHandler(qt_message_handler)
app = QGuiApplication([])

view = QQuickView()

qml_file = Path(__file__).parent / "view.qml"

if not qml_file.exists():
    print("No qml file")

view.rootContext().setContextProperty("controller", controller)
view.setSource(QUrl.fromLocalFile(qml_file.resolve()))


if view.status() == QQuickView.Error:
    for e in view.errors():
        print("error: " + e.toString())
    sys.exit(-1)

view.setResizeMode(QQuickView.ResizeMode.SizeViewToRootObject)
view.show()

app.exec()

del view
