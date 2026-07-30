import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Dict

from colorama import Fore, Style


COMMON_TCP: Dict[int, str] = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    111: "RPCbind",
    135: "MSRPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Proxy",
    8443: "HTTPS-Alt",
    27017: "MongoDB",
}


COMMON_UDP: Dict[int, str] = {
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    123: "NTP",
    137: "NetBIOS-NS",
    138: "NetBIOS-DGM",
    161: "SNMP",
    162: "SNMP-Trap",
    500: "ISAKMP",
    514: "Syslog",
    520: "RIP",
    1900: "SSDP",
    4500: "IPSec-NAT",
    5353: "mDNS",
}


TIMEOUT = 1.0
MAX_WORKERS = 100
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class Scanner:
    def __init__(self, target: str, udp: bool = False) -> None:
        self.hostname = target
        self.target = socket.gethostbyname(target)
        self.udp = udp
        self.ports = COMMON_UDP if udp else COMMON_TCP

        self.open_ports: list[tuple[int, str]] = []
        self.lock = threading.Lock()

        self.completed = 0
        self.total = len(self.ports)

    def _progress(self) -> None:
        with self.lock:
            self.completed += 1

            percent = int(
                (self.completed / self.total) * 100
            )

            bar_length = 30
            filled = int(
                (bar_length * self.completed) / self.total
            )

            bar = "█" * filled + "░" * (bar_length - filled)

            print(
                f"\r  Progreso: {bar} {percent:3d}%",
                end="",
                flush=True,
            )

    def _check_tcp(
        self,
        port: int,
        service: str,
    ) -> None:

        try:
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM,
            ) as sock:

                sock.settimeout(TIMEOUT)

                if sock.connect_ex(
                    (self.target, port)
                ) == 0:

                    with self.lock:
                        self.open_ports.append(
                            (port, service)
                        )

        except OSError:
            pass

        finally:
            self._progress()

    def _check_udp(
        self,
        port: int,
        service: str,
    ) -> None:

        try:
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM,
            ) as sock:

                sock.settimeout(TIMEOUT)

                sock.sendto(
                    b"\x00",
                    (self.target, port),
                )

                try:
                    sock.recvfrom(1024)

                    with self.lock:
                        self.open_ports.append(
                            (port, service)
                        )

                except socket.timeout:
                    pass

        except OSError:
            pass

        finally:
            self._progress()

    def _print_results(self) -> None:

        print("\n")

        print(
            f"{Fore.LIGHTWHITE_EX}"
            f"  {'PUERTO':<8} │ {'ESTADO':<10} │ SERVICIO"
            f"{Style.RESET_ALL}"
        )

        print(
            f"  {'─'*8}─┼─{'─'*10}─┼─{'─'*20}"
        )

        self.open_ports.sort(
            key=lambda item: item[0]
        )

        for port, service in self.open_ports:

            print(
                f"  {Fore.LIGHTGREEN_EX}"
                f"{port:<8}"
                f"{Style.RESET_ALL}"
                f" │ "
                f"{Fore.LIGHTGREEN_EX}"
                f"{'ABIERTO':<10}"
                f"{Style.RESET_ALL}"
                f" │ {service}"
            )

    def scan(self) -> None:

        protocol = "UDP" if self.udp else "TCP"

        start = time.time()

        print(
            f"{Fore.LIGHTCYAN_EX}"
            f"  Protocolo : {protocol}"
        )

        print(
            f"  Objetivo  : {self.hostname}"
            f" ({self.target})"
        )

        print(
            f"  Puertos   : {self.total}"
        )

        print(
            f"  Workers   : {MAX_WORKERS}"
            f"{Style.RESET_ALL}\n"
        )

        with ThreadPoolExecutor(
            max_workers=MAX_WORKERS
        ) as executor:

            checker = (
                self._check_udp
                if self.udp
                else self._check_tcp
            )

            futures = [
                executor.submit(
                    checker,
                    port,
                    service,
                )
                for port, service
                in self.ports.items()
            ]

            for _ in as_completed(futures):
                pass

        elapsed = time.time() - start

        self._print_results()

        print(
            f"\n{Fore.LIGHTCYAN_EX}"
            f"  ─────────────────────────────────────"
        )

        if self.open_ports:
            print(
                f"  Encontrados "
                f"{Fore.LIGHTGREEN_EX}"
                f"{len(self.open_ports)}"
                f"{Fore.LIGHTCYAN_EX}"
                f" puerto(s) abierto(s)."
            )
        else:
            print(
                "  No se encontraron puertos abiertos."
            )

        print(
            f"  Tiempo: {elapsed:.2f}s"
        )

        print(
            f"  Finalizado: "
            f"{datetime.now().strftime(DATE_FORMAT)}"
        )

        print(
            f"{Fore.LIGHTCYAN_EX}"
            f"  ─────────────────────────────────────"
            f"{Style.RESET_ALL}\n"
        )