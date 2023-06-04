from PyQt5 import Qt, QtCore, QtGui, QtWidgets, QtWebEngineCore, QtWebEngineWidgets, QtWebEngine
import sys

class MainluWeb(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainluWeb, self).__init__()
        self.setWindowTitle("MainluWeb V3")
        self.setWindowIcon(QtGui.QIcon("mainlu.ico"))
        
        self.web = QtWebEngineWidgets.QWebEngineView()
        self.web.setGeometry(0, 0, self.width(), self.height())
        self.web.load(QtCore.QUrl("https://www.google.com"))
        self.setCentralWidget(self.web)
        self.web.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        self.web.page().fullScreenRequested.connect(lambda request: request.accept())

    def toggleFullScreen(self, request):
        if request.toggleOn():
            self.setWindowState(Qt.WindowFullScreen)
            request.accept()
        else:
            self.setWindowState(Qt.WindowNoState)
            request.accept()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainluWeb()
    window.show()
    sys.exit(app.exec_())
        