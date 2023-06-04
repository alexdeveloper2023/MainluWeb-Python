#Por la libreria PyQt5, este navegador esta basado en el navegador Google Chrome.

from PyQt5 import Qt, QtCore, QtGui, QtWidgets, QtWebEngineCore, QtWebEngineWidgets, QtWebEngine
import sys

class MainluWeb(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainluWeb, self).__init__()
        #Establecer la ventana principal
        self.setWindowTitle("MainluWeb V3")
        #Icono de la ventana principal
        self.setWindowIcon(QtGui.QIcon("MainluWeb V3/ico.ico"))
        #Establecer la ventana principal en modo maximizado por defecto
        self.showMaximized()
        
        #Crear el objeto QWebEngineView
        self.web = QtWebEngineWidgets.QWebEngineView()
        
        #Establecer el tamaño del objeto QWebEngineView
        self.web.setGeometry(0, 0, self.width(), self.height())
        
        #Cargar la página web por defecto en el objeto QWebEngineView
        self.web.load(QtCore.QUrl("https://www.google.com"))
        
        #Agregar el objeto QWebEngineView al contenedor de la ventana principal
        self.setCentralWidget(self.web)
        
        #Activar el modo full screen
        self.web.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        self.web.page().fullScreenRequested.connect(lambda request: request.accept())
        
        #Crear el menú de navegación
        menubar = QtWidgets.QMenuBar(self)
        
        #Crear una barra de herramientas
        toolbar = QtWidgets.QToolBar(self)
        
        #Crear un campo de texto para la barra de herramientas
        self.url = QtWidgets.QLineEdit(self)
        
        #No poder mover la barra de herramientas y hacerlo invisble
        toolbar.setMovable(False)
        toolbar.toggleViewAction().setVisible(False)
        
        #Establecer en el campo de texto un texto que luego se borra al escribir en el campo de texto
        self.url.setPlaceholderText("Buscar...")
        
        
        #Establecer en el campo de texto la url de la página
        self.url.setText("https://www.google.com")
        
        #Cambiar la url del campo de texto a la url de la página mediante el método urlChanged
        self.web.urlChanged.connect(self.changeUrl)
        
        #Buscar con la palabra puesta en el campo de texto y con Google al presionar la tecla Enter
        self.url.returnPressed.connect(self.setUrlBySearch)
        
        #Agregar el campo de texto a la barra de herramientas
        toolbar.addWidget(self.url)
        
        #addMenu añade al menú de navegación las opciones
        fileMenu = menubar.addMenu("Archivo")
        
        #Esta opcion se utiliza para cerrar la ventana
        fileMenu.addAction("Salir", self.close)

        pluginsMenu = menubar.addMenu("Extensiones")
        
        #Aparecer una mensaje de prueba
        pluginsMenu.addAction("Test Plugin", self.testPlugin)

        #Añadir la barra de navegación y la barra de herramientas al contenedor de la ventana principal
        self.setMenuBar(menubar)
        self.addToolBar(toolbar)
        
    #Función para mostrar un mensaje
    def testPlugin(self):
        QtWidgets.QMessageBox.information(self, "Test Plugin", "Test de Plugin")
    
    #Función para cambiar la url
    def changeUrl(self, q):
        self.url.setText(q.toString())
    
    #Función para buscar con la palabra, lo malo es que al volver a presionar la tecla Enter vuelve a buscar
    def setUrlBySearch(self):
        self.web.load(QtCore.QUrl("https://www.google.com/search?q=" + self.url.text()))
        
#Ejecutar el programa 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainluWeb()
    window.show()
    sys.exit(app.exec_())
        