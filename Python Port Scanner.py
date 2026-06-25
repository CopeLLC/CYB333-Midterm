import socket

class Scanner:
    def __init__(self,host):
        self.host = host

    def __repr__(self):
        return f"Scanner: {self.host}"

def main():
    host = 'scanme.nmap.org'
    ports = [80, 443, 22, 21]

    scanner = Scanner(host)
    print(scanner)

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed (error {result})")

        sock.close()

if __name__ == '__main__':
    main()