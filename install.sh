#!/bin/bash

VERSION="1.0"

echo "Instalando Ignem v${VERSION}"
echo "=========================="
echo ""

if ! command -v python3 &> /dev/null
then
    echo "Python3 no está instalado."

    if [ -n "$TERMUX_VERSION" ]; then
        echo "Puedes instalarlo con:"
        echo "pkg install python"
    fi

    exit 1
fi

echo "Python3 encontrado: $(python3 --version)"
echo ""

if [ -n "$TERMUX_VERSION" ]; then
    TERMUX=true
    INSTALL_DIR="$PREFIX/bin"

    echo "Entorno detectado: Termux"
    echo "Directorio de instalación: $INSTALL_DIR"
else
    TERMUX=false
    INSTALL_DIR="/usr/local/bin"

    echo "Entorno detectado: Linux"
    echo "Directorio de instalación: $INSTALL_DIR"
fi

echo ""

echo "¿Quieres instalar colorama?"
echo ""
echo "1) Sí"
echo "2) No"
echo ""

read -p "Selecciona una opción [1/2]: " COLORAMA_OPTION

case "$COLORAMA_OPTION" in
    1)
        echo ""
        echo "Instalando colorama..."

        if python3 -m pip install colorama
        then
            echo "Colorama instalado correctamente."
        else
            echo "No se pudo instalar colorama."
            echo "Ignem utilizará los colores ANSI incorporados."
        fi
        ;;

    2)
        echo ""
        echo "Se omitirá la instalación de colorama."
        echo "Ignem utilizará los colores ANSI incorporados."
        ;;

    *)
        echo ""
        echo "Opción no válida."
        echo "Se omitirá la instalación de colorama."
        ;;
esac

echo ""

if [ ! -f "ignem.py" ]; then
    echo "No se encontró ignem.py."
    exit 1
fi

chmod +x ignem.py

cat > ignem << EOF
#!/bin/sh
exec python3 "$(pwd)/ignem.py" "\$@"
EOF

chmod +x ignem

echo "Lanzador creado."
echo ""

if [ "$TERMUX" = true ]; then

    cp ignem "$INSTALL_DIR/ignem"

    if [ $? -ne 0 ]; then
        echo "No se pudo instalar Ignem en $INSTALL_DIR."
        exit 1
    fi

else

    if [ ! -w "$INSTALL_DIR" ]; then
        sudo cp ignem "$INSTALL_DIR/ignem"
    else
        cp ignem "$INSTALL_DIR/ignem"
    fi

    if [ $? -ne 0 ]; then
        echo "No se pudo instalar Ignem."
        exit 1
    fi

fi

echo ""
echo "=========================="
echo "Ignem v${VERSION} instalado."
echo "=========================="
echo ""
echo "Ejecuta:"
echo ""
echo "  ignem"
echo ""
echo "Ayuda:"
echo ""
echo "  ignem --help"
echo ""
echo "Versión:"
echo ""
echo "  ignem --version"
echo ""
