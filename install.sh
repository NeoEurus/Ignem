#!/bin/bash

echo "🔥 Instalando Ignem v0.6"
echo "========================"

if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 no está instalado."
    exit 1
fi

echo "✓ Python encontrado"

echo "Actualizando pip..."
python3 -m pip install --upgrade pip

echo "Instalando dependencias..."
python3 -m pip install -r requirements.txt
sudo cp ignem /usr/local/bin/
sudio cp core /usr/local/bin/

echo ""
echo "✅ Instalación completada."
echo ""
echo "Ejecuta Ignem con:"
echo "python3 ignem.py --help"
echo "O"
echo "ignem --help"
