#lecialem z 10 poradnikow na necie i sie udalo wiec ez win widzowie
#robcie co chcecie z tym
#ps hindusi sa najlepsi i elo



import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *



x = 10.0
x = "adfasf"
input = int()
# main window widzowie kazdy wie o co chodzi jest 1300x700 bo nie umiem inaczej
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Rocket Browser')
        self.setWindowIcon(QIcon("icons/browser.png"))
        self.resize(1300, 700)
        self.show()
        #karty kurwa ten zjebane to
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)
        self.setCentralWidget(self.tabWidget)

        self.webview = WebEngineView(self)
        #reklame gorących mamusiek tu wkleic chopaki
        self.webview.load(QUrl("http://www.google.pl"))
        self.create_tab(self.webview)



        navigation_bar = QToolBar('Pasek nawigacji')
        navigation_bar.setIconSize(QSize(30, 30))
        self.addToolBar(navigation_bar)

        back_button = QAction(QIcon('icons/left-arrow.png'), 'Wstecz', self)
        next_button = QAction(QIcon('icons/right-arrow.png'), 'Dalej', self)
        reload_button = QAction(QIcon('icons/refresh.png'), 'Odśwież', self)


                 # Normalnie lacze se jak klocki lego przyciski z funkcjami z engine
        back_button.triggered.connect(self.webview.back)
        next_button.triggered.connect(self.webview.forward)
        reload_button.triggered.connect(self.webview.reload)

                 # Tu przyciski dodajesz frajerze denty
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(reload_button)


                 # Pasek ten co wklejania linkow do teletubisow
        self.urlbar = QLineEdit()
                 # Maly update
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)

                 # to kazali wkleic i chyba cos tam zmienia
        self.webview.urlChanged.connect(self.renew_urlbar)

         # POka poka sowe
    def homeBtn(self):
        self.webEngineView.load(QUrl('https://google.com'))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.webview.setUrl(q)

         # jak klikasz enter kurwa ten to normalnie dziala
    def renew_urlbar(self, q):
                 # a tu bug fixed jak wejdzesz na strone to ci normalnie zmienia url na gorze i elo
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

         # nowa karta funckja ten
    def create_tab(self, webview):
        self.tab = QWidget()
        self.tabWidget.addTab(self.tab, "Karta")
        self.tabWidget.setCurrentWidget(self.tab)

                 # a tutaj wystawielanie ale wolne bo pyengine ssie przy chrome
        self.Layout = QHBoxLayout(self.tab)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addWidget(webview)

         # zamknij karte bo stary wchodzi
    def close_Tab(self, index):
        if self.tabWidget.count() > 1:
            self.tabWidget.removeTab(index)
        else:
            self.close()

class WebEngineView(QWebEngineView):

    def __init__(self, mainwindow, parent=None):
        super(WebEngineView, self).__init__(parent)
        self.mainwindow = mainwindow

    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView(self.mainwindow)
        self.mainwindow.create_tab(new_webview)
        return new_webview

#no tutaj wyswietlamy aplikacje okej
if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = MainWindow()
    browser.show()
    sys.exit(app.exec_())
