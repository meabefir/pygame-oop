from Events import Events
import sqlite3
from copy import deepcopy


class Database:
    connection = None
    cursor = None

    @staticmethod
    def init():
        Database.connection = sqlite3.connect('users.db')
        Database.cursor = Database.connection.cursor()


        #Database.delete_database()
        # Database.init_tables()

    @staticmethod
    def delete_database():
        with Database.connection:
            Database.cursor.execute(f"delete from users")
            Database.cursor.execute(f"delete from level_completed")

    @staticmethod
    def init_tables():
        # users table
        Database.cursor.execute("""
                    create table users(
                        username text,
                        password text,
                        coins integer,
                        level integer,
                        xp float
                    )
                """)
        # levels completed table
        Database.cursor.execute("""
                    create table level_completed(
                        username text,
                        level text
                    )
        """)

    @staticmethod
    def get_user(username):
        with Database.connection:
            Database.cursor.execute(f"select * from users where username=?", (username,))
            res = Database.cursor.fetchone()
            if res is None:
                return None
            user_data = {
                "username": res[0],
                "password": res[1],
                "coins": res[2],
                "level": res[3],
                "xp": res[4],
                "completed_levels": []
            }
            Database.cursor.execute(f"select * from level_completed where username=:username", {'username': username})
            completed_levels = Database.cursor.fetchall()
            if completed_levels is not None:
                for level_completed in completed_levels:
                    user_data["completed_levels"].append(level_completed[1])
            return deepcopy(user_data)

    @staticmethod
    def register_user(user_data):
        with Database.connection:
            Database.cursor.execute(f"insert into users values (:username, :password, 0, 0, 0)", user_data)

    @staticmethod
    def attempt_login(login_data):
        _user, _pass = login_data["username"].strip(), login_data["password"].strip()

        with Database.connection:
            Database.cursor.execute(f"select * from users where username=:username and password=:password", login_data)
            if Database.cursor.fetchone() is None:
                Events.emit("login_fail")
                return None
            # Events.emit("login_success", Database.get_user(_user))
            return Database.get_user(_user)

    @staticmethod
    def attempt_register(register_data):
        _user, _pass = register_data["username"].strip(), register_data["password"].strip()
        with Database.connection:
            Database.cursor.execute(f"select * from users where username=:username",
                                    register_data)
            if Database.cursor.fetchone() is None:
                Database.register_user(register_data)
                # Events.emit("register_success", Database.get_user(_user))
                return Database.get_user(_user)
            else:
                # Events.emit("register_fail")
                return None

    @staticmethod
    def update_user(user_data):
        # we dont check anything, we just update
        with Database.connection:
            Database.cursor.execute(f"""update users set coins= :coins,
                                                         level= :level,
                                                         xp= :xp
                                        where username=:username""",
                                    user_data)
            # create new entries of level_completed if needed
            for level in user_data['completed_levels']:
                Database.cursor.execute(
                    f"select * from level_completed where username=:username and level=:level",
                    {'username': user_data['username'], 'level': level})
                if Database.cursor.fetchone() is None:
                    Database.cursor.execute(f"insert into level_completed values (:username, :level)",
                                            {"username": user_data['username'], 'level': level})

    # delete example
    # with Database.connection:
    #     Database.cursor.execute(f"delete from users where username={_user} and password={_pass}")


Database.init()
