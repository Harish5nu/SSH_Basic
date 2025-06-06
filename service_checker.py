import socket

target = input("Enter target IP address: ")

# Check Telnet (Port 23)
sock_telnet = socket.socket()
sock_telnet.settimeout(2)
if sock_telnet.connect_ex((target, 23)) == 0:
    print("[+] Telnet (port 23) is OPEN")
else:
    print("[-] Telnet (port 23) is CLOSED")
sock_telnet.close()

# Check SSH (Port 22)
sock_ssh = socket.socket()
sock_ssh.settimeout(2)
if sock_ssh.connect_ex((target, 22)) == 0:
    print("[+] SSH (port 22) is OPEN")
else:
    print("[-] SSH (port 22) is CLOSED")
sock_ssh.close()
