from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor, defer
from twisted.protocols.ftp import FTP, FTPFactory, FTPRealm
from user_management import *

def start_server():
    checker = InMemoryUsernamePasswordDatabaseDontUse()

    ftp_users = jsonR("users.json")
    for key in ftp_users:
        checker.addUser(key, ftp_users[key])

    portal = Portal(FTPRealm("./public", "./myusers"), [AllowAnonymousAccess(), checker])

    factory = FTPFactory(portal)

    reactor.listenTCP(21, factory)
    reactor.run()
start_server()