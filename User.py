from Events import Events
from Database import Database
from copy import deepcopy

class User:
    def __init__(self, data={}):
        self.data = deepcopy(data)
        self.xp_per_level = 20

        Events.connect("coin_picked", self, self.coin_picked)
        Events.connect("level_completed", self, self.level_completed)
        Events.connect("give_xp", self, self.give_xp)

    def set_data(self, data):
        self.data = deepcopy(data)

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
        print("level completed")
        if level in self.data["completed_levels"]:
            return

        new_data = {
            "completed_levels": self.data["completed_levels"] + [level]
        }
        self.update_data(new_data)
        Database.update_user(self.data)
        # Database.save_database() # already in update user

    def give_xp(self, amm):
        new_xp = self.data["xp"] + amm
        new_data = {
            'xp': new_xp
        }
        if new_xp >= self.xp_per_level:
            new_level = self.data["level"] + new_xp // self.xp_per_level
            new_xp = new_xp % self.xp_per_level

            new_data = {
                'xp': new_xp,
                'level': new_level
            }

        self.update_data(new_data)

        Events.emit("set_xp", self.data['xp'], self.data['level'])
        # Database.save_database() # already in update user
