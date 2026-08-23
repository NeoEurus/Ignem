# Ignem v1.0

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Termux-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Stable-success?style=for-the-badge" />
</p>

<p align="center">
  <b>Escáner de puertos TCP/UDP desarrollado en Python 3</b>
</p>

<p align="center">
  Rápido · Ligero · Multihilo · CLI
</p>

---

## Descripción

**Ignem** es un escáner de puertos TCP/UDP desarrollado en Python 3, diseñado para realizar análisis de red de forma sencilla y eficiente sobre equipos autorizados.

El proyecto utiliza ejecución concurrente mediante múltiples workers para acelerar el proceso de escaneo, resolución automática de hostnames y detección de servicios comunes.

Ignem está pensado como una herramienta ligera y educativa para aprender sobre redes, sockets, protocolos TCP/UDP y desarrollo de herramientas de línea de comandos.

---

## Características

- Escaneo de puertos TCP.
- Escaneo de puertos UDP.
- Escaneo TCP + UDP por defecto.
- Selección individual de protocolo mediante `--tcp` o `--udp`.
- Ejecución concurrente mediante `ThreadPoolExecutor`.
- Resolución automática de IP y hostname.
- Detección de servicios comunes.
- Más de 50 puertos TCP y UDP incluidos.
- Barra de progreso en tiempo real.
- Resultados ordenados por número de puerto.
- Una única tabla para resultados TCP y UDP.
- Interfaz de consola con colores.
- Compatibilidad opcional con Colorama.
- Manejo de errores.
- Código modular y tipado.
- Instalación mediante script.
- Compatibilidad con Termux.

---

## Estructura del proyecto

```text
Ignem/
│
├── ignem.py
├── install.sh
│
├── core/
│   ├── scanner.py
│   └── __init__.py
│
├── requirements.txt
│
└── README.md
```

---

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/eurushanma/ignem.git
```

### Entrar al directorio

```bash
cd ignem
```

### Instalar Ignem

```bash
chmod +x install.sh
./install.sh
```

Durante la instalación se podrá elegir si se desea instalar `colorama`.

Si se decide no instalarlo, Ignem utilizará colores ANSI como alternativa.

### Instalación manual

También es posible instalar las dependencias directamente:

```bash
python3 -m pip install -r requirements.txt
```

Y ejecutar Ignem con:

```bash
python3 ignem.py
```

---

## Termux

Ignem también puede instalarse en Termux.

Primero instala Python:

```bash
pkg install python
```

Después clona el repositorio:

```bash
git clone https://github.com/eurushanma/ignem.git
```

Entra al directorio:

```bash
cd ignem
```

Ejecuta el instalador:

```bash
chmod +x install.sh
./install.sh
```

El instalador detectará automáticamente Termux y utilizará su directorio de binarios correspondiente.

---

## Requisitos

- Python 3.10 o superior.
- Linux, Windows, macOS o Termux.
- Permisos suficientes para realizar pruebas sobre el objetivo autorizado.
- Colorama es opcional.

---

## Uso

Una vez instalado, Ignem puede ejecutarse directamente:

```bash
ignem
```

También puede utilizarse indicando un objetivo:

```bash
ignem <TARGET>
```

Si no se especifica ningún protocolo, Ignem realizará automáticamente un escaneo TCP y UDP.

### Escaneo TCP

```bash
ignem <TARGET> --tcp
```

### Escaneo UDP

```bash
ignem <TARGET> --udp
```

### Escaneo TCP + UDP

```bash
ignem <TARGET> --tcp --udp
```

### Mostrar ayuda

```bash
ignem --help
```

### Mostrar versión

```bash
ignem --version
```

---

## Opciones

| Opción | Descripción |
|---|---|
| `--tcp` | Escanea únicamente TCP. |
| `--udp` | Escanea únicamente UDP. |
| `--version` | Muestra la versión de Ignem. |
| `-h`, `--help` | Muestra la ayuda. |

Si no se especifica `--tcp` ni `--udp`, se ejecutan ambos protocolos automáticamente.

---

## Tecnologías utilizadas

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Socket-Redes-00599C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ThreadPoolExecutor-Concurrencia-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/argparse-CLI-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Colorama-Terminal-yellow?style=for-the-badge" />
</p>

---

## Próximas mejoras

Algunas características que podrían incorporarse en futuras versiones:

- Escaneo de rangos de puertos personalizados.
- Escaneo de todos los puertos.
- Configuración del número de workers.
- Configuración del tiempo de espera.
- Detección más avanzada de servicios.
- Exportación de resultados a JSON.
- Exportación de resultados a TXT.
- Soporte para IPv6.
- Mejor detección de puertos UDP.
- Argumentos de configuración adicionales.
- Mayor cantidad de servicios conocidos.

---

## Aviso

Ignem fue desarrollado con fines educativos y de administración de sistemas.

Utiliza esta herramienta únicamente contra equipos, servidores o redes sobre los que tengas autorización para realizar pruebas.

El uso indebido de herramientas de análisis de red puede tener consecuencias legales.

---

## Licencia

Este proyecto se distribuye bajo la licencia MIT.

Consulta el archivo `LICENSE` para obtener los términos completos de la licencia.

---

## Autor

<p align="center">
  <img src="https://img.shields.io/badge/Desarrollado%20por-Eurus-orange?style=for-the-badge" />
</p>

<p align="center">
  <b>Eurus</b><br>
  Creador y desarrollador de Ignem
</p>

<p align="center">
  Python · Redes · Linux · Herramientas CLI
</p>

<p align="center">
  <i>
    Herramientas simples para aprender,
    experimentar y comprender mejor la tecnología.
  </i>
</p>

---

<p align="center">
  <b>Ignem Port Scanner · v1.0</b>
</p>
