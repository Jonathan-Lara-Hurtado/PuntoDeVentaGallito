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

- Linux digitar el siguiente comando:
    
    ~~~
    pip3 install matplotlib
    ~~~
- Windows digitar el siguientes comandos:
    ~~~
    python -m pip install numpy
    python -m pip install scipy
    python -m pip install matplotlib
    ~~~

---

## Instalacion plugin web Pyqt5

- **Windows**
     ~~~
     pip install PyQtWebEngine     
     ~~~
- **Linux**
    ~~~
    sudo apt-get install python3-pyqt5.qtwebkit
    ~~~
---
## Generar el ejecutable con pyinstaller

Ejecutar el siguiente comando en la carpteta src sin importar el S.O
~~~
pyinstaller main.spec
~~~
---

## Notas
- Como generar un main.spec
    ~~~
    pyinstaller --add-data 'Recursos:Recursos' --add-data 'Documentacion:Documentacion' main.py 
    ~~~
