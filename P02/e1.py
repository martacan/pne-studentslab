from Client0 import Client


print(f"-----| Practice 2, Exercise 1 |------")

# -- Parameters of the server to talk to
IP = "192.168.1.45" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.ping()
