#!/bin/bash

echo "[+] Updating package lists..."
sudo apt update

echo "[+] Installing aircrack-ng..."
sudo apt install -y aircrack-ng

echo "[+] Installing pip (if needed)..."
sudo apt install -y python3-pip

echo "[+] Installing pyfiglet..."
pip3 install pyfiglet

echo "[+] Done!"

echo "[+] Checking installations..."

if command -v aircrack-ng >/dev/null 2>&1; then
    echo "✓ aircrack-ng installed"
else
    echo "✗ aircrack-ng not found"
fi

python3 -c "import pyfiglet; print('✓ pyfiglet installed')" 2>/dev/null || echo "✗ pyfiglet not found"