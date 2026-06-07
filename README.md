# Airstop v1.0.1

Airstop is a Python-based wireless security testing utility that provides a simple command-line interface for working with Aircrack-ng tools.

> This tool is intended for authorized security testing, lab environments, and educational purposes only.

## Features

### Version 1.0.1

* Automatic Aircrack-ng installation check
* Automatic Aircrack-ng installation (APT-based systems)
* ASCII startup banner using PyFiglet
* Deauthentication attack interface
* Simple interactive command-line menu

### Planned Features

* Handshake capture
* WPA/WPA2 password cracking
* Graphical user interface (GUI)
* Additional wireless auditing modules

## Requirements

* Python 3.8+
* Linux (Debian/Ubuntu/Kali recommended)
* sudo privileges
* Wireless adapter capable of monitor mode
* Aircrack-ng suite

Run:

```bash
python3 airstop.py
```

## Usage

Start the program:

```bash
python3 airstop.py
```

Select an attack option:

```text
1 - Deauthentication Attack
2 - Handshake Capture (Coming Soon)
3 - Password Cracking (Coming Soon)
```

For the deauthentication module, provide:

* Target Access Point MAC Address (BSSID)
* Number of deauthentication packets
* Wireless interface in monitor mode

Example:

```text
Target MAC: AA:BB:CC:DD:EE:FF
Packets: 100
Interface: wlan0mon
```

## Disclaimer

This software is provided for educational and authorized security testing purposes only.

The user is solely responsible for complying with all applicable laws and regulations. Unauthorized attacks against networks, devices, or systems that you do not own or have explicit permission to test may be illegal.

The author assumes no responsibility for misuse or damage caused by this software.

## Version

Current Release: **v1.0.1**

## Author

Vijayvinayak

