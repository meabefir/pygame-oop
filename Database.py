import json
from Events import Events


class Database:
    file_path = "database.txt"
    data = None

    @staticmethod
    def load_data():
        r_file = open(Database.file_path, "r")
        Database.data = json.load(r_file)
        r_file.close()

    @staticmethod
    def get_user(username):
        if username in Database.data:
            return Database.data[username]
        return None

    @staticmethod
    def register_user(user_data):
        _user, _pass = user_data["username"], user_data["password"]
        if Database.get_user(_user) is None:
            Database.data[_user] = user_data
            Database.data[_user]["coins"] = 0
            Database.data[_user]["level"] = 0
            Database.data[_user]["xp"] = 0
            Database.data[_user]["completed_levels"] = []

    @staticmethod
    def attempt_login(login_data):
        _user, _pass = login_data["username"].strip(), login_data["password"].strip()
        if Database.get_user(_user) and Database.data[_user]["password"] == _pass:
            Events.emit('login_success', Database.data[_user])
            return Database.data[_user]
        else:
            Events.emit('login_fail')
            return None

    @staticmethod
    def attempt_register(register_data):
        _user, _pass = register_data["username"].strip(), register_data["password"].strip()
        if Database.get_user(_user) is None:
            Database.register_user(register_data)
            Events.emit("register_success", Database.data[_user])
            Database.save_database()
            return Database.data[_user]
        else:
            Events.emit("register_fail")
            return None

    @staticmethod
    def update_user(user_data):
        username = user_data["username"]
        if username in Database.data:
            for key in user_data:
                Database.data[username][key] = user_data[key]
        Database.save_database()

    @staticmethod
    def save_database():
        w_file = open(Database.file_path, 'w')
        json.dump(Database.data, w_file)
        w_file.close()

    def __str__(self):
        return str(self.data)


Database.load_data()
