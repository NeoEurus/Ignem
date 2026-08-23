#!/usr/bin/env python3

"""
Proyecto Maqueta - Ignem v0.6
Este proyecto es un escáner de puertos TCP/UDP simple desarrollado en Python 3.
Hecho por Eurus (@eurushanma) y distribuido bajo la licencia MIT.
"""

import argparse
import os
import sys
from typing import Callable

from colorama import Fore, Style, init

from core.scanner import Scanner, print_results, print_summary

init(autoreset=True)

VERSION = "1.0"

BANNER = f"""
{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}
    ██╗ ██████╗ ███╗   ██╗███████╗███╗   ███╗
    ██║██╔════╝ ████╗  ██║██╔════╝████╗ ████║
    ██║██║  ███╗██╔██╗ ██║█████╗  ██╔████╔██║
    ██║██║   ██║██║╚██╗██║██╔══╝  ██║╚██╔╝██║
    ██║╚██████╔╝██║ ╚████║███████╗██║ ╚═╝ ██║
    ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝
{Style.RESET_ALL}{Fore.LIGHTCYAN_EX}           Port Scanner  ·  v{VERSION}
{Style.RESET_ALL}
"""

clear: Callable[[], None] = lambda: os.system(
    "cls" if os.name == "nt" else "clear"
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ignem",
        description=BANNER + f"""
{Fore.LIGHTWHITE_EX}{Style.BRIGHT}
USO{Style.RESET_ALL}
  ignem <TARGET> [OPCIONES]

{Fore.LIGHTWHITE_EX}{Style.BRIGHT}
OPCIONES{Style.RESET_ALL}
  --tcp              Escanea únicamente puertos TCP.
  --udp              Escanea únicamente puertos UDP.
  --version          Muestra la versión del programa.
  -h, --help         Muestra esta ayuda.

{Fore.LIGHTWHITE_EX}{Style.BRIGHT}
PROTOCOLO POR DEFECTO{Style.RESET_ALL}
  Si no se especifica --tcp ni --udp,
  Ignem escanea TCP y UDP automáticamente.

{Fore.LIGHTWHITE_EX}{Style.BRIGHT}
EJEMPLOS{Style.RESET_ALL}
  ignem scanme.nmap.org
  ignem localhost --tcp
  ignem 192.168.1.1 --udp
  ignem 192.168.1.1 --tcp --udp
""",
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False,
    )

    parser.add_argument(
        "target",
        metavar="TARGET",
        nargs="?",
        help="IP o hostname a escanear",
    )

    parser.add_argument(
        "--tcp",
        action="store_true",
        help="Escanea únicamente puertos TCP",
    )

    parser.add_argument(
        "--udp",
        action="store_true",
        help="Escanea únicamente puertos UDP",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"Ignem v{VERSION}",
    )

    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="Muestra esta ayuda y sale",
    )

    args = parser.parse_args()

    if args.target is None:
        parser.print_help()
        sys.exit(0)

    return args


def main() -> None:
    args = parse_arguments()

    clear()
    print(BANNER)

    if args.tcp:
        modes = [False]
    elif args.udp:
        modes = [True]
    else:
        modes = [False, True]

    results = []

    for udp in modes:
        scanner = Scanner(
            args.target,
            udp,
        )

        results.extend(
            scanner.scan()
        )

    print_results(results)
    print_summary(results)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print(
            f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}"
            "Escaneo interrumpido por el usuario."
            f"{Style.RESET_ALL}\n"
        )
        sys.exit(130)

    except Exception as error:
        print(
            f"\n{Fore.LIGHTRED_EX}{Style.BRIGHT}"
            f"Error: {error}"
            f"{Style.RESET_ALL}\n"
        )
        sys.exit(1)
