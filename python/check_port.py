
def check_port(port):
    if port==80:
        print(f'port{port}- HTTP web traffic')
    elif port ==443:
        print(f'port {port}- HTTPS secure web traffic')
    elif port ==22:
        print(f'port {port} - SSH remote access')
    elif port==3389:
        print(f'port {port} - RDp remote desktop WARNING')
    elif port==53:
        print(f'port{port} -domain name service(DNS)')
    elif port==21:
        print(f'port {port} - file transfer protocol')
    else:
        print(f'port {port} - Unkown port')
check_port(80)
check_port(443)
check_port(22)
check_port(8080)
check_port(3389)
check_port(53)
check_port(21)
while True:
    user_port = int(input("\nEnter a port number to check (0 to quit): "))
    if user_port ==0:
        print("Goodbye!")
        break
    check_port(user_port)
