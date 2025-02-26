import sys
import socket
import datetime

#TODO: finalizar execucao direta via linha de comando e arrumar o range para o IP

OUTPUT = "./output/scan_results.txt"


socket.setdefaulttimeout(.01)

def scanner(ip: str, 
            protocol: str, 
            ip_proto: int, 
            start_port: int = 1, 
            end_port: int = 1000
    ):

    target = socket.getaddrinfo(ip, None, ip_proto)[0][4][0]

    print("----------------------------------")

    try:
        start_time = datetime.datetime.now()
        ports_open = 0
        service = ""

        for port in range(start_port, end_port):
            with socket.socket(family=ip_proto, type=socket.SOCK_STREAM, proto=0) as s:
                addr = (target, port)

                if ip_proto == socket.AF_INET6:
                    addr = (target, port, 0, 0)

                errno_code = s.connect_ex(addr)

                try:
                    service = socket.getservbyport(port, protocol)

                    result = ""

                    if not errno_code:
                        result = f"Porta {port} - {service} - open"
                        ports_open += 1
                    elif errno_code in [111, 10061]:
                        result = f"Porta {port} - {service} - closed"
                    else:
                        result = f"Porta {port} - {service} - filtered"

                    print(result)
                except OSError:
                    service = "unknown port"

        runtime = datetime.datetime.now() - start_time

        print(f"Total de portas abertas encontradas: {ports_open}\n"
              f"Tempo de execucao: {runtime.seconds:.2f} segundos\n")

    except KeyboardInterrupt:
        raise KeyboardInterrupt("\nOperacao cancelada pelo usuario")


def scanNetwork(
        network: str, 
        protocol: str, 
        ip_proto: int,
        start_port: int = 1, 
        end_port: int = 1000,
        start_ip: int = 1, 
        end_ip: int = 255, 
    ):
    
    print(f"Rede a ser escaneada: {network}")
    
    for ip in range(start_ip, end_ip + 1):
        hostname = network + "." + str(ip)
        
        scanner(hostname, protocol, ip_proto, start_port, end_port)

    print(f"Escaneamento da rede finalizada")
    

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-u", "-U"]:
            protocol = "udp"
        elif sys.argv[1] in ["-t", "-T"]:
            protocol = "tcp"
        else:
            raise Exception("Sintaxe incorreta: primeiro argumento (protocolo) deve ser -t para TCP ou -u para UDP")
        
        if sys.argv[3] in ["-v4", "-V4"]:
            version = socket.AF_INET
        elif sys.argv[3] in ["-v6", "-V6"]:
            version = socket.AF_INET6
        else:
            raise Exception("Sintaxe invalida: o argumento do protocolo IP deve ser -v4 ou -v6")
        
    if len(sys.argv) == 5:
        if sys.argv[2] in ["-n", "-N"]:
            network = sys.argv[4]

            scanNetwork(network, protocol, version)

        elif sys.argv[2] in ["-h", "-H"]:
            hostname = sys.argv[4]

            scanner(hostname, protocol, version)

    elif len(sys.argv) == 6:
        if sys.argv[5].startswith("port_range="):
            port_range = sys.argv[5][11:].split(",")

            try:
                start_port = int(port_range[0])
                end_port = int(port_range[1])
            except:
                raise Exception("Sintaxe invalida: verifique se os valores do port_range sao inteiros")

            if sys.argv[2] in ["-n", "-N"]:
                network = sys.argv[4]

                scanNetwork(network, protocol, version, start_port, end_port)

            elif sys.argv[2] in ["-h", "-H"]:
                hostname = sys.argv[4]

                scanner(hostname, protocol, version, start_port, end_port)

        elif sys.argv[5].startswith("ip_range=") and sys.argv[2] in ["-n", "-N"]:
            ip_range = sys.argv[5][9:].split(",")

            try:
                start_ip = int(ip_range[0])
                end_ip = int(ip_range[1])
            except:
                raise Exception("Sintaxe invalida: verifique se os valores do ip_range sao inteiros")

            network = sys.argv[4]

            scanNetwork(network, protocol, start_ip=start_ip, end_ip=end_ip)
        else:
            raise Exception("Sintaxe invalida: o ip_range so pode ser utilizado para escaneamento de rede")
        
    elif len(sys.argv) == 7 and sys.argv[2] in ["-n", "-N"]:
        if sys.argv[5].startswith("port_range="):
            port_range = sys.argv[5][11:].split(",")

            try:
                start_port = int(port_range[0])
                end_port = int(port_range[1])
            except:
                raise Exception("Sintaxe invalida: verifique se os valores do port_range sao inteiros")
            
            if sys.argv[6].startswith("ip_range="):
                ip_range = sys.argv[6][9:].split(",")

                try:
                    start_ip = int(ip_range[0])
                    end_ip = int(ip_range[1])
                except:
                    raise Exception("Sintaxe invalida: verifique se os valores do ip_range sao inteiros")

                network = sys.argv[4]

                scanNetwork(network, protocol, start_port, end_port, start_ip, end_ip)
            else:
                raise Exception("Sintaxe invalida: verifique se o ip_range foi utilizado corretamente")
        else:
            raise Exception("Sintaxe invalida: verifique se foi utilizada a flag -n")
    else:
        raise Exception("Quantidade incorreta de argumentos")
    return 0


if __name__ == "__main__":
    main()
