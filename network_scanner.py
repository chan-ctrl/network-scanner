import socket

target = input("Enter IP Address: ")

for port in [3389, 3306, 110, 80, 443]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: Open")
    else:
        print(f"Port {port}: Closed")

    sock.close()