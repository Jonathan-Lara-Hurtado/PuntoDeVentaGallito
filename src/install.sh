#!/bin/bash
# Generador de carpetas
for d in ./ArchivosUi/*.ui;do
f="$(basename --suffix=.ui $d ).py"
pyuic5 -x "$d"  -o "./VentanasGui/$f"
done
pyrcc5 ./resource.qrc -o ./resource_rc.py
python3 main.py