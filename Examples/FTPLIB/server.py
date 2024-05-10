from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Instantiate a dummy authorizer for managing 'virtual' users
authorizer = DummyAuthorizer()

# Add a new user with a given username, password, and directory
authorizer.add_user("user", "password", "/", perm="elradfmw")

# Instantiate FTP handler object
handler = FTPHandler
handler.authorizer = authorizer

# Create an FTP server instance, listening on localhost, port 21
server = FTPServer(("127.0.0.1", 21), handler)

# Start the FTP server
server.serve_forever()
