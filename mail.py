# from kamene.all import sniff, TCP, IP

# def packet_callback(packet):
#     if packet[TCP].payload:
#         mail_packet = bytes(packet[TCP].payload)
#         if b'user' in mail_packet.lower() or b'pass' in mail_packet.lower():
#             print("[*] Server: %s" % packet[IP].dst)
#             print("[*] %s" % packet[TCP].payload)

# # Fire up our sniffer
# sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",
#       prn=packet_callback,
#       store=0)


# from kamene.all import sniff, TCP, IP

# def packet_callback(packet):
#     if packet[TCP].payload:
#         http_packet = bytes(packet[TCP].payload)
#         if b'GET' in http_packet:
#             print("[*] Server: %s" % packet[IP].dst)
#             print("[*] %s" % packet[TCP].payload)

# # Fire up our sniffer
# sniff(filter="tcp port 80",
#       prn=packet_callback,
#       store=0)



# from kamene.all import sniff, TCP, IP

# def packet_callback(packet):
#     if packet.haslayer(TCP) and packet.haslayer(IP):
#         print(f"[*] Packet: {packet.summary()}")

# # Fire up our sniffer
# sniff(prn=packet_callback, store=0)


# from kamene.all import sniff, TCP, IP

# def packet_callback(packet):
#     if packet.haslayer(TCP) and packet.haslayer(IP):
#         if packet[TCP].dport == 80 or packet[TCP].sport == 80:  # HTTP traffic
#             http_packet = bytes(packet[TCP].payload)
#             if b'GET' in http_packet:
#                 try:
#                     http_info = http_packet.decode('utf-8')
#                     lines = http_info.split('\r\n')
#                     for line in lines:
#                         if line.startswith('GET'):
#                             print(f"[*] HTTP GET Request: {line}")
#                             print(f"[*] Server: {packet[IP].dst}")
#                             break
#                 except UnicodeDecodeError:
#                     pass

# # Fire up our sniffer
# sniff(filter="tcp port 80", prn=packet_callback, store=0)



# from kamene.all import sniff, TCP, IP

# def packet_callback(packet):
#     if packet.haslayer(TCP) and packet.haslayer(IP):
#         if packet[TCP].dport == 80 or packet[TCP].sport == 80:  # HTTP traffic
#             http_packet = bytes(packet[TCP].payload)
#             if b'GET' in http_packet:
#                 try:
#                     http_info = http_packet.decode('utf-8')
#                     lines = http_info.split('\r\n')
#                     for line in lines:
#                         if line.startswith('GET'):
#                             print(f"[*] HTTP GET Request: {line}")
#                             print(f"[*] Server: {packet[IP].dst}")
#                             break
#                 except UnicodeDecodeError:
#                     pass

# # Fire up our sniffer
# sniff(filter="tcp port 80", prn=packet_callback, store=0)



# from kamene.all import sniff, TCP, IP

# def packet_callback(packet):
#     if packet.haslayer(TCP) and packet.haslayer(IP):
#         if packet[TCP].dport == 80 or packet[TCP].sport == 80:  # HTTP traffic
#             http_packet = bytes(packet[TCP].payload)
#             if b'GET' in http_packet:
#                 try:
#                     http_info = http_packet.decode('utf-8')
#                     lines = http_info.split('\r\n')
#                     for line in lines:
#                         if line.startswith('GET'):
#                             print(f"[*] HTTP GET Request: {line}")
#                             print(f"[*] Server: {packet[IP].dst}")
#                             break
#                 except UnicodeDecodeError:
#                     pass
#         elif packet[TCP].dport == 443 or packet[TCP].sport == 443:  # HTTPS traffic
#             print(f"[*] HTTPS Request to: {packet[IP].dst}")

# # Fire up our sniffer
# sniff(filter="tcp port 80 or tcp port 443", prn=packet_callback, store=0)



# from kamene.all import sniff, TCP, IP
# import socket

# def packet_callback(packet):
#     if packet.haslayer(TCP) and packet.haslayer(IP):
#         if packet[TCP].dport == 80 or packet[TCP].sport == 80:  # HTTP traffic
#             http_packet = bytes(packet[TCP].payload)
#             if b'GET' in http_packet:
#                 try:
#                     http_info = http_packet.decode('utf-8')
#                     lines = http_info.split('\r\n')
#                     for line in lines:
#                         if line.startswith('GET'):
#                             print(f"[*] HTTP GET Request: {line}")
#                             print(f"[*] Server: {packet[IP].dst}")
#                             break
#                 except UnicodeDecodeError:
#                     pass
#         elif packet[TCP].dport == 443 or packet[TCP].sport == 443:  # HTTPS traffic
#             try:
#                 domain_name = socket.gethostbyaddr(packet[IP].dst)[0]
#             except socket.herror:
#                 domain_name = packet[IP].dst
#             print(f"[*] HTTPS Request to: {domain_name}")

# # Fire up our sniffer
# sniff(filter="tcp port 80 or tcp port 443", prn=packet_callback, store=0)



from kamene.all import sniff, TCP, IP
import socket

# Cache for storing IP to domain name mappings
dns_cache = {}

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        ip_address = packet[IP].dst
        if ip_address in dns_cache:
            domain_name = dns_cache[ip_address]
        else:
            try:
                domain_name = socket.gethostbyaddr(ip_address)[0]
            except socket.herror:
                domain_name = ip_address
            dns_cache[ip_address] = domain_name

        if packet[TCP].dport == 80 or packet[TCP].sport == 80:  # HTTP traffic
            http_packet = bytes(packet[TCP].payload)
            if b'GET' in http_packet:
                try:
                    http_info = http_packet.decode('utf-8')
                    lines = http_info.split('\r\n')
                    for line in lines:
                        if line.startswith('GET'):
                            print(f"[*] HTTP GET Request: {line}")
                            print(f"[*] Server: {domain_name}")
                            break
                except UnicodeDecodeError:
                    pass
        else:  # Other TCP traffic
            print(f"[*] TCP Request to: {domain_name}")

# Fire up our sniffer
sniff(prn=packet_callback, store=0)