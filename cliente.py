import sys
from socketTCP import SocketTCP

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Modo de uso: cliente-prov [IP] [puerto]")

    end_sequence = b"end-of-message"
    server_address = (sys.argv[1], int(sys.argv[2]))

    print("Creando socket - Cliente")

    client_socket = SocketTCP()

    print("Conectando Socket")
    client_socket.connect(server_address)

    print("Enviando mensaje")
    message = input().encode() + end_sequence
    client_socket.send(message, mode="go_back_n")

    print("Cerrando Socket")
    client_socket.close()

    print("confirmando cierre")
    try:
        client_socket.send(message, mode="go_back_n")
    except Exception as e:
        print(f"se reportó el error {e}")

    