open_ports =[80, 443, 22, 3389, 21, 53]

print("Open ports found:")
for port in open_ports:
    print(f"Port{port} is open")

print(f"\nTotal open ports: {len(open_ports)}")

if 3389 in open_ports:
    print("WARNING - RDP port 3389 is open!")
