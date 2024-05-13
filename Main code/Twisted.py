from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm



checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("user1", "password")
checker.addUser("ali", "yassin")
portal = Portal(FTPRealm("./public", "./myusers"), [AllowAnonymousAccess(), checker])

factory = FTPFactory(portal)

reactor.listenTCP(2121, factory)
reactor.run()