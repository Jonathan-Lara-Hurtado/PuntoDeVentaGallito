# Punto de Venta Gallito Negro



**Comandos de Conversion de archivos:**

- Para convertir archivo ui a py usar el siguiente comando
    ~~~
    pyuic5 -x <nombre>.ui -o <nombre>.py      
    ~~~

- Para convertir un archivo recurso .qrc a py usar el siguiente comando
    ~~~
    pyrcc5 <nombre>.qrc -o <nombre>.py
    ~~~

    ejemplo:  
    ~~~
    pyrcc5 resource.qrc -o ./Recursos/resource_rc.py
    ~~~
---
## Instalacion de matplotlib(libreria para graficar).

- Linux 
    - pip3 install matplotlib

- Windows
    - python -m pip install numpy
    - python -m pip install scipy
    - python -m pip install matplotlib

##

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
