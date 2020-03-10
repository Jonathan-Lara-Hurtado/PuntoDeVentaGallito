#################################################
Generar .ui a .py
################################################
pyuic5 -x <nombre>.ui -o <nombre>.py
pyrcc5 resource.qrc -o ./Recursos/resource_rc.py


#################################################
Windows
#################################################
pip install PyQtWebEngine
para que funcione el web
#####from PyQt5 import QtWebKitWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings


#################################################
Linux
#################################################
sudo apt-get install python3-pyqt5.qtwebkit




#################################################
Mac
#################################################



################################################
pyinstaller
#############################################
pyinstaller --add-data 'Recursos:Recursos' --add-data 'Documentacion:Documentacion' main.py 
pyinstaller main.spec