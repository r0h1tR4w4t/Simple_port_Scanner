import socket
from IPy import IP

# Function to convert Domain to IP
def convert_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

# Function to get banner information
def get_banner(s):
    return s.recv(1024).decode('utf-8').strip()

# Function to get protocol name for well-known ports
def get_protocol_name(port):
    well_known_ports = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        443: 'HTTPS',
        3389: 'RDP',
    }
    return well_known_ports.get(port, 'TCP')

# Function to scan the ports
def scan_port(ip_addr, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)  # Increased timeout for banner grabbing
        sock.connect((ip_addr, port))
        try:
            banner = get_banner(sock)
            protocol = get_protocol_name(port)
            print(f"\r[+] Open Port : {port} {protocol} : {banner}\n")
        except Exception as e:
            protocol = get_protocol_name(port)
            print(f"\r[+] Open Port : {port} {protocol} (No banner available)\n")
        finally:
            sock.close()
    except:
        pass

print('''
$$$$$$$\                       $$\                                                                      
$$  __$$\                      $$ |                                                                     
$$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\ 
$$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$  _____|$$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  ____/ $$ /  $$ |$$ |  \__| $$ |          \$$$$$$\  $$ /      $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$ |  $$ |$$ |       $$ |$$\        \____$$\ $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |       
$$ |      \$$$$$$  |$$ |       \$$$$  |      $$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|       \______/ \__|        \____/       \_______/  \_______|\_______|\__|  \__| \_______|\__|
|                                                                                                |
|--------------------------------------------Coded by Rohit--------------------------------------|''')

# Variables Declaration
ip_address = input("[+] Enter the Address: ")
starting_port = int(input("[+] Enter Starting port: "))
last_port = int(input("[+] Enter Last port: "))

target_ip = convert_ip(ip_address)

print("\n[*] Scanning Target : " + ip_address)
print("[*] Target Address: " + str(target_ip) + "\n")

# Function Call
for port in range(starting_port, last_port):
    scan_port(target_ip, port)

print("\nDone!!")

