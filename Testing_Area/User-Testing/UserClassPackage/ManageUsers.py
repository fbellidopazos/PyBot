import pickle



class ManageUsers:
    def __init__(self):
        self.user_list = []
        self.load_pickle()

    def load_pickle(self):
        f = open("Users.pkl", "rb")
        res = pickle.load(f)
        f.close()
        self.user_list = res

    def backup_pickle(self):
        f = open("Users.pkl", "wb")
        pickle.dump(self.user_list, f)
        f.close()

    def add_user(self, name: str, nick, role="Regular"):
        user = User(name, nick, role)
        self.user_list.append(user)
        self.backup_pickle()

    def add_user(self, name: str, role="Regular"):
        user = User(name, name[-5], role)
        self.user_list.append(user)
        self.backup_pickle()

    def remove_user(self, name):
        index=self.find_nick(name)
        if 0 <= index < len(self.user_list):
            self.user_list.remove(self.user_list[index])
        self.backup_pickle()

    def to_string(self):
        res = ""
        for i in self.user_list:
            res = res + i.to_string()
        return (res)

    def add_role(self, nick, role):
        index = self.find_nick(nick)
        if (index != -1 and not (role in self.user_list[index].roles)):
            self.user_list[index].add_role(role)
        self.backup_pickle()

    def remove_role(self, nick, role):
        index = self.find_nick(nick)
        if (index != -1 and role in self.user_list[index].roles):
            self.user_list[index].remove_role(role)
        self.backup_pickle()

    def find_nick(self, nick):
        res = -1
        for i in range(len(self.user_list)):
            res += 1
            if (self.user_list[i].nick == nick):
                break
        return res

    def find_name(self, name):
        res = -1
        for i in range(len(self.user_list)):
            res += 1
            if (self.user_list[i].name == name):
                break
        return res

    def count(self):
        return self.user_list.__len__()