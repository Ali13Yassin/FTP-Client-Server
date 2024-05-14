from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor, defer
from twisted.protocols.ftp import FTPFactory, FTPShell, FTPRealm

checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("someuser", "12345")
checker.addUser("anonymos", "12345")
checker.addUser("anotheruser", "password")

portal = Portal(FTPRealm("./public/", "./myusers/"), [AllowAnonymousAccess(), checker])


factory = FTPFactory(portal)

reactor.listenTCP(21, factory)
reactor.run()
