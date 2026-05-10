#!/bin/bash
echo " Configurando entorno para Raspberry Pi..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo " Instalación completada. Activa el entorno con: source venv/bin/activate"