class User():
    def __init__(self,name,nick,mainRole):
        self.name=name
        self.nick=nick
        self.mainRole=mainRole
        self.roles=[mainRole]
    def addRole(self,role):
        self.roles=self.roles+[role]
    def removeRole(self,role):
        self.roles.remove(role)
    def setMainRole(self,mainRole):
        self.mainRole=mainRole
    def setNick(self,nick):
        self.nick=nick
    def toString(self):
        return ("Name: "+str(self.name)+"\nNick: "+self.nick+"\nmainRole: "+self.mainRole+"\nRoles: "+str(self.roles)+"\n\n")

