import json
import os
from pathlib import Path  # Used to know the directory of the file

os.chdir(Path(__file__).parent)  # Changes terminal directory to the one that has the file


def jsonR(loc):
    if os.path.exists(loc):
        file = open(loc, "r")
        info = json.load(file)
        file.close
        return info
    else:
        file = open(loc, "w")
        file.write("{}")
        file.close
        return {}


def jsonW(loc, info):
    file = open(loc, "r")
    if os.path.getsize(loc) > 0:
        info.update(json.load(file))
    file.close

    file = open(loc, "w")
    json.dump(info, file)
    file.close


global allusers
if os.path.exists("users.json"):
    allusers=jsonR("users.json")
else:
    jsonW("users.json",{})
    allusers=jsonR("users.json")

#-----------------------------<user Functions Begin>--------------------------------
#Adding a new user to database
def adduser(inusername,inname,password):
    if inusername not in allusers:
        allusers[inusername] = {"username":inusername,"password":password}
        jsonW("users.json",allusers)
        return True
    else:
        return False

#Edit basic info
#edit, value neeed to be put inside "" marks to function, and if they are buttons that works
def edituser(inusername,oldusername,inpass):
    if oldusername == "none":
        allusers[inusername]["username"] = inusername
        allusers[inusername]["password"] = inpass
        jsonW("users.json",allusers)
        return True
    else:
        if inusername not in allusers:
            allusers[inusername] = {"username":inusername,"password":inpass}
            del allusers[oldusername]
            jsonW("users.json",allusers)
            return True
        else:
            return False

#Delete user information
def deleteuser(inusername):
    del allusers[inusername]
    jsonW("users.json",allusers)

#This function was supposed to be named readfile but I don't want to change it to not break features again
def readuser(info):
    if info=="users":
        return allusers

def finduser(info):
    if info in allusers:
            return allusers[info]
    else:
        return "none"

#-----------------------------<user Functions End>--------------------------------
