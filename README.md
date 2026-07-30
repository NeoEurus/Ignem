# 🔥 Ignem v0.6

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Stable-success?style=for-the-badge" />
</p>

<p align="center">
  <b>Escáner simple de puertos TCP/UDP desarrollado en Python 3</b>
</p>

<p align="center">
  Rápido · Ligero · Multihilo · Interfaz CLI
</p>

---

## 📌 Descripción

**Ignem** es un escáner de puertos TCP/UDP desarrollado en Python 3, diseñado para realizar análisis rápidos y eficientes sobre equipos autorizados.

Utiliza ejecución multihilo para optimizar el proceso de escaneo, detección de servicios comunes y una interfaz de consola limpia con salida visual mediante colores.

El proyecto busca ofrecer una herramienta ligera, sencilla y educativa para comprender conceptos relacionados con redes, sockets y análisis de servicios.

---

## ✨ Características

- Escaneo de puertos TCP
- Escaneo de puertos UDP
- Escaneo TCP + UDP simultáneo
- Ejecución concurrente mediante múltiples workers
- Resolución automática de hostname
- Detección de servicios comunes
- Barra de progreso en tiempo real
- Resultados ordenados por puerto
- Interfaz de consola con colores
- Manejo de errores
- Código modular y tipado

---

## 📂 Estructura del proyecto

```text
Ignem/
│
├── ignem.py
│
├── core/
│   ├── scanner.py
│   └── __init__.py
│
├── requirements.txt
│
└── README.md
```

## ⚙️ Instalación

### Clonar el repositorio

```bash
git clone https://github.com/eurushanma/ignem.git
```

### Entrar al Directorio

```bash
cd ignem
```

### Instalar dependencias

```bash
chmod +x install.sh
./install.sh
```

O

```
python3 -m pip install -r requirements.txt
```

## 🖥️ Requisitos

- Python 3.10 o superior
- Linux, Windows o macOS
- Permisos suficientes para realizar pruebas sobre el objetivo autorizado

---

## 🚀 Uso

Mostrar ayuda:

```bash
python3 ignem.py --help
```

## 🛠️ Tecnologías utilizadas

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Socket-Networking-00599C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ThreadPoolExecutor-Multithreading-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/argparse-CLI-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/colorama-Terminal-yellow?style=for-the-badge" />
</p>

---

## ⚠️ Aviso

Ignem fue desarrollado con fines educativos y para administración de sistemas.

Utiliza esta herramienta únicamente contra equipos, servidores o redes donde tengas autorización para realizar pruebas.

El uso indebido de herramientas de análisis de red puede tener consecuencias legales.

---

## 📜 Licencia

Este proyecto está distribuido bajo la licencia MIT.

---

## 👤 Autor

<p align="center">
  <img src="https://img.shields.io/badge/Desarrollado%20por-Eurus-orange?style=for-the-badge" />
</p>

<p align="center">
  <b>Eurus</b><br>
  Desarrollador de Ignem<br>
  Python · Redes · Herramientas CLI
</p>

<p align="center">
  <i>
    "Creando herramientas simples para aprender,
    experimentar y entender mejor la tecnología."
  </i>
</p>

---

<p align="center">
  🔥 <b>Ignem Port Scanner · v0.6</b>
</p>
