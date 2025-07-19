#!/data/data/com.termux/files/usr/bin/bash

echo "[+] Installing Sherlock (username OSINT)..."

pkg update -y && pkg install git python -y
pip install --upgrade pip

cd ~
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
pip install -r requirements.txt

echo "[+] Sherlock installed at ~/sherlock/"
echo "[+] Usage Example:"
echo "cd ~/sherlock && python3 sherlock.py username"
