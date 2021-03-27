from Events import Events


class User:
    def __init__(self, data={}):
        self.data = data

        Events.connect("coin_picked", self, self.coin_picked)

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
