ports = {
    80: "HTTP - web traffic",
    433: "HTTPS - secure web traffic",
    22: "SSH - remote access",
    21: "FTP - file transfer",
    3389: "RDP - remote desktop WARNING!",
    53: "DNS - domain name service"
}

while True:
    port= int(input("\nEnter port number to check (0 to quit)"))
    if port== 0:
        print("Goodbye!")
        break
    if port in ports:
        print(f"port{port} - {ports[port]}")
    else:
        print(f"port{port} - Unknown port")