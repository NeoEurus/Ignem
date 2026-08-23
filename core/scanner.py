import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Dict

try:
    from colorama import Fore, Style
except ImportError:
    class Fore:
        LIGHTGREEN_EX = "\033[92m"
        LIGHTYELLOW_EX = "\033[93m"
        LIGHTCYAN_EX = "\033[96m"
        LIGHTRED_EX = "\033[91m"
        LIGHTWHITE_EX = "\033[97m"

    class Style:
        BRIGHT = "\033[1m"
        RESET_ALL = "\033[0m"

COMMON_TCP: Dict[int, str] = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    26: "SMTP-Alt",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    111: "RPCbind",
    119: "NNTP",
    135: "MSRPC",
    139: "NetBIOS",
    143: "IMAP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    587: "SMTP-Submission",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    2049: "NFS",
    2375: "Docker",
    2376: "Docker-TLS",
    3000: "Grafana/Node",
    3306: "MySQL",
    3389: "RDP",
    4000: "Web-Alt",
    5000: "HTTP-Alt",
    5432: "PostgreSQL",
    5672: "AMQP",
    5900: "VNC",
    5985: "WinRM",
    5986: "WinRM-HTTPS",
    6379: "Redis",
    6443: "Kubernetes-API",
    8000: "HTTP-Alt",
    8008: "HTTP-Alt",
    8080: "HTTP-Proxy",
    8081: "HTTP-Alt",
    8088: "HTTP-Alt",
    8443: "HTTPS-Alt",
    8888: "HTTP-Alt",
    9000: "PHP-FPM/Dev",
    9090: "Prometheus",
    9200: "Elasticsearch",
    9300: "Elasticsearch",
    10000: "Webmin",
    11211: "Memcached",
    15672: "RabbitMQ",
    27017: "MongoDB",
    27018: "MongoDB",
    50000: "SAP",
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
    623: "IPMI",
    1194: "OpenVPN",
    1434: "MSSQL-Browser",
    1701: "L2TP",
    1900: "SSDP",
    4500: "IPSec-NAT",
    5060: "SIP",
    5061: "SIP-TLS",
    5353: "mDNS",
    5355: "LLMNR",
    5683: "CoAP",
    10000: "Webmin",
    11211: "Memcached",
    16100: "SNMP-Alt",
}

TIMEOUT = 1.0
MAX_WORKERS = 100
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class Scanner:
    def __init__(
        self,
        target: str,
        udp: bool = False,
    ) -> None:
        self.hostname = target
        self.target = socket.gethostbyname(target)
        self.udp = udp

        self.protocol = "UDP" if udp else "TCP"
        self.ports = COMMON_UDP if udp else COMMON_TCP

        self.open_ports: list[
            tuple[int, str, str]
        ] = []

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
                (bar_length * self.completed)
                / self.total
            )

            bar = (
                "█" * filled
                + "░" * (bar_length - filled)
            )

            print(
                f"\r  {Fore.LIGHTCYAN_EX}"
                f"Progreso: "
                f"{bar} "
                f"{percent:3d}%"
                f"{Style.RESET_ALL}",
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
                            (
                                port,
                                self.protocol,
                                service,
                            )
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
                            (
                                port,
                                self.protocol,
                                service,
                            )
                        )

                except socket.timeout:
                    pass

        except OSError:
            pass

        finally:
            self._progress()

    def scan(
        self,
    ) -> list[tuple[int, str, str]]:
        self.completed = 0
        self.open_ports.clear()

        start = time.time()

        print(
            f"{Fore.LIGHTCYAN_EX}"
            f"  Protocolo : {self.protocol}"
            f"{Style.RESET_ALL}"
        )

        print(
            f"  Objetivo  : "
            f"{self.hostname} ({self.target})"
        )

        print(
            f"  Puertos   : {self.total}"
        )

        print(
            f"  Workers   : {MAX_WORKERS}"
        )

        print()

        checker = (
            self._check_udp
            if self.udp
            else self._check_tcp
        )

        with ThreadPoolExecutor(
            max_workers=MAX_WORKERS
        ) as executor:

            futures = [
                executor.submit(
                    checker,
                    port,
                    service,
                )
                for port, service
                in self.ports.items()
            ]

            for future in as_completed(futures):
                future.result()

        elapsed = time.time() - start

        print(
            f"\n\n  "
            f"{Fore.LIGHTGREEN_EX}"
            f"✓ Escaneo {self.protocol} finalizado"
            f"{Style.RESET_ALL}"
        )

        print(
            f"  Tiempo: {elapsed:.2f}s"
        )

        return self.open_ports


def print_results(
    results: list[tuple[int, str, str]],
) -> None:
    results.sort(
        key=lambda item: (
            item[0],
            item[1],
        )
    )

    print()

    print(
        f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}"
        f"  {'PUERTO':<9}│ "
        f"{'PROTOCOLO':<11}│ "
        f"{'ESTADO':<10}│ "
        f"SERVICIO"
        f"{Style.RESET_ALL}"
    )

    print(
        f"  {'─' * 9}"
        f"┼"
        f"{'─' * 12}"
        f"┼"
        f"{'─' * 11}"
        f"┼"
        f"{'─' * 20}"
    )

    if not results:
        print(
            f"  {Fore.LIGHTYELLOW_EX}"
            "No se encontraron puertos abiertos."
            f"{Style.RESET_ALL}"
        )
        return

    for port, protocol, service in results:
        print(
            f"  {Fore.LIGHTCYAN_EX}"
            f"{port:<9}"
            f"{Style.RESET_ALL}"
            f"│ "
            f"{Fore.LIGHTYELLOW_EX}"
            f"{protocol:<11}"
            f"{Style.RESET_ALL}"
            f"│ "
            f"{Fore.LIGHTGREEN_EX}"
            f"{'ABIERTO':<10}"
            f"{Style.RESET_ALL}"
            f"│ {service}"
        )


def print_summary(
    results: list[tuple[int, str, str]],
) -> None:
    print()

    print(
        f"{Fore.LIGHTCYAN_EX}"
        "  ─────────────────────────────────────────────"
        f"{Style.RESET_ALL}"
    )

    if results:
        print(
            f"  Encontrados "
            f"{Fore.LIGHTGREEN_EX}"
            f"{len(results)}"
            f"{Style.RESET_ALL}"
            f" puerto(s) abierto(s)."
        )
    else:
        print(
            f"  {Fore.LIGHTYELLOW_EX}"
            "No se encontraron puertos abiertos."
            f"{Style.RESET_ALL}"
        )

    print(
        f"  Finalizado: "
        f"{datetime.now().strftime(DATE_FORMAT)}"
    )

    print(
        f"{Fore.LIGHTCYAN_EX}"
        "  ─────────────────────────────────────────────"
        f"{Style.RESET_ALL}\n"
    )
