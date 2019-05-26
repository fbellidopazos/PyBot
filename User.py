class User():
    def __init__(self,name,mainRole):
        self.name=name
        self.mainRole=mainRole
        self.roles=[mainRole]
    def addRole(self,role):
        self.roles=self.roles+[role]
    def removeRole(self,role):
        self.roles.remove(role)

    def setMainRole(self,mainRole):
        self.mainRole=mainRole
    def toString(self):
        return ("Name: "+str(self.name)+"\nmainRole: "+self.mainRole+"\nRoles: "+str(self.roles)+"\n\n")

