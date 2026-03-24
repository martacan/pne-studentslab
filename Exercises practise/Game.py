import random
import socket
class NumberGuesser:
    def __init__(self):
       self.secret_number = random.randint(1, 100)
       self.attempts = []

    def guess(self, number):
        number = int(number)
        self.attempts.append(number)
        if number == self.secret_number:
            return(f"Congrats you have won after {len(self.attempts)} attempts")
        elif number > self.secret_number:
            return "Lower"
        elif number < self.secret_number:
            return "Higher"


IP = "127.0.0.1"
PORT = 8082
MAX_OPEN_REQUESTS = 5
number_con = 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen(MAX_OPEN_REQUESTS)

    while True:
        print(f"Waiting for connections at {IP}, {PORT}")
        (clientsocket, address) = server_socket.accept()

        number_con += 1
        print(f"CONNECTION: {number_con} from the IP: {address}")

        game = NumberGuesser()

        clientsocket.send("Welcome! Guess the number (1-100):\n".encode("utf-8"))

        while True:
            msg = clientsocket.recv(2048).decode("utf-8").strip()
            if not msg:
                break
            try:
                response = game.guess(msg)

                clientsocket.send(f"{response}\n".encode("utf-8"))
                if "won" in response:
                    break
            except ValueError:
                clientsocket.send("Please, send only integers.\n".encode("utf-8"))

        clientsocket.close()

except socket.error:
    print(f"Problems using ip {IP} port {PORT}.")
except KeyboardInterrupt:
    print("\nServer stopped by the user")
    server_socket.close()