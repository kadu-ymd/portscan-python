import sys
import socket
import datetime

#TODO: finalizar execucao direta via linha de comando e arrumar o range para o IP


socket.setdefaulttimeout(.01)

def scanner(hostname: str, protocol: str, start_port: int, end_port: int ):
    target = socket.gethostbyname(hostname)

    print(f"Nome e endereco do host: {hostname} | {target}")
    print("----------------------------------")
    
    try:
        start_time = datetime.datetime.now()
        ports_open = 0
        service = ""

        for port in range(start_port, end_port):
            s = socket.socket()

            addr = (target, port)

            errno_code = s.connect_ex(addr)

            try:
                service = socket.getservbyport(port, protocol)
                if not errno_code:
                    print(f"Porta {port} - {service} - open")
                    ports_open += 1
                elif errno_code in [111, 10061]:
                    print(f"Porta {port} - {service} - closed")
                else:
                    print(f"Porta {port} - {service} - filtered")
            except OSError:
                service = "unknown port"

            s.close()

        runtime = datetime.datetime.now() - start_time

        print(f"Total de portas abertas encontradas: {ports_open}\n"
              f"Tempo de execucao: {runtime.seconds:.2f} segundos\n")

    except KeyboardInterrupt:
        raise KeyboardInterrupt("\nOperacao cancelada pelo usuario")


def scanNetwork(network: str, protocol: str, start_port: int = 1, end_port: int = 1000):
    print(f"Rede a ser escaneada: {network}")

    for ip in range(1, 256):
        hostname = network + "." + str(ip)
        
        scanner(hostname, protocol, start_port, end_port)
    

def main():
    if len(sys.argv) == 4: # main.py -n/-h network/host
        protocol = ""

        if sys.argv[1] in ["-u", "-U"]:
            protocol = "udp"
        elif sys.argv[1] in ["-t", "-T"]:
            protocol = "tcp"
        else:
            raise Exception("Sintaxe incorreta: primeiro argumento deve ser -t ou -u (protocolo)")
        
        if sys.argv[2] in ["-n", "-N"]:
            network = sys.argv[3]
            
            scanNetwork(network, protocol)

        elif sys.argv[2] in ["-h", "-H"]:
            hostname = sys.argv[3]

            scanner(hostname, protocol)

    elif len(sys.argv) == 5:
        if sys.argv[4].startswith("port_range="):
            port_range = sys.argv[4][11:].split(",")

            try:
                start_port = int(port_range[0])
                end_port = int(port_range[1])
            except:
                raise Exception("Sintaxe invalida: verifique se os valores do port_range sao inteiros")


            if sys.argv[2] in ["-n", "-N"]:
                network = sys.argv[3]
                
                scanNetwork(network, protocol, start_port, end_port)

            elif sys.argv[2] in ["-h", "-H"]:
                hostname = sys.argv[3]

                scanner(hostname, protocol, start_port, end_port)
        
        elif sys.argv[4].startswith("ip_range=") and sys.argv[2] in ["-n", "-N"]:
            ip_range = sys.argv[4][9:].split(",")

            try:
                start_port = int(ip_range[0])
                end_port = int(ip_range[1])
            except:
                raise Exception("Sintaxe invalida: verifique se os valores do ip_range sao inteiros")

            network = sys.argv[3]
                
            scanNetwork(network, protocol, start_port, end_port)

        else:
            raise Exception("Sintaxe invalida")
        
    elif len(sys.argv) == 6 and sys.argv[2] in ["-n", "-N"]:
        if sys.argv[4].startswith("port_range="):
            port_range = sys.argv[4][11:].split(",")

            try:
                start_port = int(port_range[0])
                end_port = int(port_range[1])
            except:
                raise Exception("Sintaxe invalida: verifique se os valores do port_range sao inteiros")
            
            if sys.argv[4].startswith("port_range="):
        print(port_range)


    return 0


if __name__ == "__main__":
    main()
    # print(socket.getservbyport(53))
