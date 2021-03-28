from Events import Events
from Database import Database


class User:
    def __init__(self, data={}):
        self.data = data

        Events.connect("coin_picked", self, self.coin_picked)
        Events.connect("level_completed", self, self.level_completed)

    def set_data(self, data):
        self.data = data

    def update_data(self, data):
        for key in data:
            if key in self.data:
                self.data[key] = data[key]

    def coin_picked(self, *args):
        new_data = {
            "coins": self.data["coins"] + 1
        }
        self.update_data(new_data)

    def level_completed(self, level):
        new_data = {
            "completed_levels": self.data["completed_levels"] + [level]
        }
        self.update_data(new_data)
        Database.update_user(self.data)
        # Database.save_database() # already in update user
