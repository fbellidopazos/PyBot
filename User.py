class User():
    def __init__(self,name,nick,mainRole,roles=[]):
        self.name=name
        self.nick=nick
        self.main_role = mainRole
        self.roles = [mainRole]+roles
    def add_role(self,role):
        self.roles=self.roles+[role]
    def remove_role(self,role):
        self.roles.remove(role)
    def set_main_role(self,mainRole):
        self.main_role=mainRole
    def set_nick(self,nick):
        self.nick=nick
    def to_string(self):
        return ("Name: "+str(self.name)+"\nNick: "+self.nick+"\nmainRole: "+self.main_role+"\nRoles: "+str(self.roles)+"\n\n")

