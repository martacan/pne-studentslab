import socket
from termcolor import cprint





IP = "127.0.0.1"
PORT = 8082





def start_player():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((IP, PORT))

        # Recibir bienvenida
        welcome = client_socket.recv(2048).decode("utf-8")
        print(f"\n[SERVER]: {welcome}")

        while True:

            guess = input("Enter your number: ")

            if not guess:
                continue

            # Enviar al servidor
            client_socket.send(guess.encode("utf-8"))

            # Recibir respuesta
            response = client_socket.recv(2048).decode("utf-8").strip()

            # Colores sin negritas (bold)
            if "won" in response:
                cprint(response, "green")
                break
            elif "Higher" in response:
                cprint(response, "blue")
            elif "Lower" in response:
                cprint(response, "yellow")
            else:
                cprint(response)

    except ConnectionRefusedError:
        cprint("Error: Servidor no disponible", "red")
    finally:
        print("Conexión cerrada.")
        client_socket.close()


if __name__ == "__main__":
    start_player()