from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import os

class CustomFTPHandler(FTPHandler):
    def on_connect(self):
        print(f"{self.remote_ip}:{self.remote_port} connected")

    def on_disconnect(self):
        print(f"{self.remote_ip}:{self.remote_port} disconnected")

    def on_login(self, username):
        print(f"{username} logged in")

    def on_logout(self, username):
        print(f"{username} logged out")

    def on_file_sent(self, file):
        print(f"sent {file}")

    def on_file_received(self, file):
        print(f"received {file}")

    def on_incomplete_file_sent(self, file):
        print(f"sent incomplete {file}")

    def on_incomplete_file_received(self, file):
        print(f"received incomplete {file}")

def main():
    handler = CustomFTPHandler
    handler.passive_ports = range(60000, 65535)
    authorizer = DummyAuthorizer()
    authorizer.add_user('ali', 'ali', "./imgs", perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())
    server = FTPServer(("localhost", 2121), handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5
    server.serve_forever()

if __name__ == '__main__':
    main()