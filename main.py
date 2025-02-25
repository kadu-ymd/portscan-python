import sys
import socket


def main():
    hostname = sys.argv[1]

    target = socket.gethostbyname(hostname) # traduz o endereço para IPv4

    try:
        for port in range(1, 65535):
            with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
                print(s.connect_ex((target, port)))
                if s.connect((target, port)) == 0:
                    print(f"A porta {port} está aberta para comunicações")
    except:
        pass

    return 0


if __name__ == "__main__":
    main()
